import pymysql
db=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='db')
cursor=db.cursor()
cursor.execute('')
data=cursor.fetall()
print()

str1='kdslkfkd'
str1[::-1]