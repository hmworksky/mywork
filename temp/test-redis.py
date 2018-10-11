import redis
import pymysql
r = redis.Redis(host='127.0.0.1', port=6379)
r.set('test', 1)
print(r.get('test'))
db = pymysql.connect(host='127.0.0.1', user='root', passwd='test1324', port=3306, db='first')
cursor = db.cursor()
cursor.execute('show tables')
data = cursor.fetchall()
print(data)
db.close()
