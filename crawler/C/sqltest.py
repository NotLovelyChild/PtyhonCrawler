import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")
db.close()