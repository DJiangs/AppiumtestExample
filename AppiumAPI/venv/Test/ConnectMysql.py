import MySQLdb.cursors

conn=MySQLdb.connect(host='',user='root',passwd='root')
cursor=conn.cursor()

cursor.execute('select  ')
r=cursor.fetchall()
print(r)

def fn():
    try:
        for i in range(5)   :
            if i>2:
                raise  Exception('number big 2')
    except Exception as ret:
        print(ret)