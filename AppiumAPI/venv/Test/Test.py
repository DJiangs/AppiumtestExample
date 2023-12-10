from operator import itemgetter,attrgetter
import  copy
help(copy.copy)
l=[]
print("请输入：")
while True:
    s=input()
    if not s:
        break
    l.append(tuple(s.split(",")))
print(sorted(l,key=itemgetter(0,1,2)))