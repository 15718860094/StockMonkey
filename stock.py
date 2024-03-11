# https://akshare.akfamily.xyz/index.html
import akshare as ak  
from fastapi.templating import Jinja2Templates
from datetime import datetime,timedelta
templates = Jinja2Templates(directory="templates") # 实例化Jinja2对象，并将文件夹路径设置为以templates命令的文件夹

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker  

  
engine = create_engine('sqlite:///stock.db', echo=True)  
  
Base = declarative_base()
class Stock(Base):  
    __tablename__ = 'stocks'  

    id = Column(Integer, primary_key=True, autoincrement=True)  
    code = Column(String, unique=True, nullable=False)  
    name = Column(String, nullable=False)  
    favorite = Column(Boolean, default=False) 



class StockInfo(Base):  
    __tablename__ = 'stock_info'  
    
    id = Column(Integer, primary_key=True, autoincrement=True)  
    code = Column(String, nullable=False)  
    date = Column(String(10), nullable=False)  
    open_price = Column(Float, nullable=False)  
    close_price = Column(Float, nullable=False)  
    high_price = Column(Float, nullable=False)  
    low_price = Column(Float, nullable=False)  
    volume = Column(Integer, nullable=False)  
    turnover = Column(Float, nullable=False)  
    amplitude = Column(Float, nullable=False)  
    change_percent = Column(Float, nullable=False)  
    change_amount = Column(Float, nullable=False)  
    turnover_rate = Column(Float, nullable=False)  


Base.metadata.create_all(engine)  


class StockAkShare():  
    def __init__(self):  
        today = datetime.today()  
        self.today_date = today.date().strftime("%Y%m%d") 
        self.start_date = '20200101'
        self.session = sessionmaker(bind=engine)()  # 创建session对象  
        self._code_name_df()  
        self._history_df()
        self.session.close()  # 关闭session      
        
        
    def _code_name_df(self):
        self.code_name_df = ak.stock_zh_a_spot_em()  
        existing_codes = set(stock.code for stock in self.session.query(Stock.code))  
        count =0 
        for index, row in self.code_name_df.iterrows():  
            code = row['代码']  
            name = row['名称']  
            if code not in existing_codes:  
                new_stock = Stock(code=code, name=name, favorite=False)  
                self.session.add(new_stock)  
                count += 1
        print('新增 stock 数量:%s' % count)
        self.session.commit() 

    def _history_df(self, symbol=None):
        if not symbol:
            favorite_stock_code = [code[0] for code in self.session.query(Stock.code).filter_by(favorite=True).all()]
        else:
            favorite_stock_code = [symbol]
            
        for symbol in favorite_stock_code:
            self.stock_df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=self.start_date, end_date=self.today_date, adjust="hfq")  
            existing_dates = [date[0] for date in self.session.query(StockInfo.date).all()] 
            count = 0
            for index, row in self.stock_df.iterrows():  
                code = symbol
                date = row['日期'].strftime('%Y%m%d') 
                open_price = row['开盘']  
                close_price = row['收盘']  
                high_price = row['最高']  
                low_price = row['最低']  
                volume = row['成交量']  
                turnover = row['成交额']  
                amplitude = row['振幅']  
                change_percent = row['涨跌幅']  
                change_amount = row['涨跌额']  
                turnover_rate = row['换手率']  
                if date not in existing_dates:  
                    new_stock = StockInfo(
                        code=code, 
                        date=date,
                        open_price=open_price,
                        close_price=close_price,
                        high_price=high_price,
                        low_price=low_price,
                        volume=volume,
                        turnover=turnover,
                        amplitude=amplitude,
                        change_percent=change_percent,
                        change_amount=change_amount,
                        turnover_rate=turnover_rate
                        )  
                    self.session.add(new_stock)  
                    count +=1 
        self.session.commit() 
        print('新增 stock info 数量:%s' % count)
        
        
    def d_monkey_search(self, search_codes=None, search_days=None, ):
        if not search_codes:
            search_codes = [code[0] for code in self.session.query(Stock.code).filter_by(favorite=True).all()]
        
        if not search_days:
            search_days = 5
        
        fit_stocks = {}
        for search_code in search_codes:
            results = []
            delta_day = 0
            while len(results) < search_days:
                target_day = (datetime.now() - timedelta(days=delta_day)).strftime('%Y%m%d') 
                query = self.session.query(StockInfo).filter(StockInfo.date == target_day, StockInfo.code==search_code)  
                result = query.first()  
                if result:  
                    print('查询到结果 results +1')
                    results.append(result)  
                delta_day += 1
            fit_stocks[search_code] = results
            print('查询到结果 fit_stocks +1')

        print(fit_stocks)
        

StockAkShare().d_monkey_search()