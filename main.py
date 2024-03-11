from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI() # 实例化 FastAPI对象
templates = Jinja2Templates(directory="templates") # 实例化Jinja2对象，并将文件夹路径设置为以templates命令的文件夹

app = FastAPI()

@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "id": 1})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


