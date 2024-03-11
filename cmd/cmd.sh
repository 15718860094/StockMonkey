# 替换mongodb
sed -i 's/10.10.32.163/10.10.32.239/g' appsettings.json
sed -i 's/10.10.32.164/10.10.32.240/g' appsettings.json
sed -i 's/10.10.32.166/10.10.32.241/g' appsettings.json

# 替换es
sed -i 's/10.10.32.168/10.10.32.238/g' appsettings.json
sed -i 's/10.10.32.170/10.10.32.237/g' appsettings.json
sed -i 's/10.10.32.173/10.10.32.236/g' appsettings.json

# redis
sed -i 's/10.10.81.117/10.10.81.198/g' appsettings.json

# MQ
sed -i 's/10.10.32.162/10.10.32.242/g' appsettings.json
# "HostNames": ["10.10.32.242","10.10.32.243","10.10.32.244"],


# 积分平台

# 替换mongodb
sed -i 's/10.10.32.171/10.10.32.223/g' appsettings.json
sed -i 's/10.10.32.172/10.10.32.224/g' appsettings.json
sed -i 's/10.10.32.174/10.10.32.225/g' appsettings.json

# 替换es
sed -i 's/10.10.32.165/10.10.32.220/g' appsettings.json
sed -i 's/10.10.32.167/10.10.32.221/g' appsettings.json
sed -i 's/10.10.32.169/10.10.32.222/g' appsettings.json

# redis
sed -i 's/10.10.81.133/10.10.81.149/g' appsettings.json

#Orleans
sed -i 's/10.10.32.179/10.10.32.234/g' appsettings.json


# MQ
        # "HostNames": ["10.10.32.226","10.10.32.227","10.10.32.228"],

# ----- 待执行 -----

# 替换全部合约
# cat
sed -i 's/2XzwWQheubxtBsEfwumosCYaqsVdtdptC82BooLQtgpDusPZg7/29kLxbvrax1ZuXUUq17TKtb1S5wJR1howDWpLb3A2SqDs8EvMQ/g' appsettings.json
# point
sed -i 's/pSSmizkBRm4s5VXUrdTziBLgVAdpbZdN5GtwzAA2gdWReSM7R/2XAbeyYp7pHwty8DnLi7tFG7y7Sd5sYrHhzwf5r4CXiy6HdS18/g' appsettings.json
# ca
sed -i 's/2UthYi7AHRdfrqc1YCfeQnjdChDLaas65bW4WxESMGMojFiXj9/238X6iw1j8YKcHvkDYVtYVbuYk2gJnK8UoNpVCtssynSpVC8hb/g' appsettings.json


# 替换所有的dappID
sed -i 's/3bb4c2d22cdda3eededcbe9016a28a4cc45a72bdd5b9d0771b11e0ada73e4bf9/4b1689025d9437098bde69ef38f02df2487742da640e8670b4efe22292d955e0/g' appsettings.json
sed -i 's/把我更新成不删档薛定谔的dappid/4b1689025d9437098bde69ef38f02df2487742da640e8670b4efe22292d955e0/g' appsettings.json

# pointservice 
sed -i 's/pixiepoints.io/10.10.32.217\:5588/g' appsettings.json

# 扫链插件
sed -i 's/indexer.10.10.32.217\:5588/test-indexer.pixiepoints.io/g' appsettings.json
sed -i 's/172.31.8.176\:8113/test-indexer.pixiepoints.io/g' appsettings.json

#Orleans
sed -i 's/10.10.32.161/10.10.32.218/g' appsettings.json


# 链信息
# cms config 
sed -i 's/public-node/test-node/g' appsettings.json
sed -i 's/aa-portkey/aa-portkey-test/g' appsettings.json


