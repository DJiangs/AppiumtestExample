import http.client
from http.client import HTTPConnection
from http.client import HTTPResponse

conn=http.client.HTTPConnection('wwww.baidu.com',80)

conn.request('GET','/')

r=conn.getresponse()

print(r.getcode())

conn.close();

BODY="***filecontents"
conn=http.client.HTTPConnection("localhost",8080)
conn.request("PUT","/file",BODY)
res=conn.getresponse()