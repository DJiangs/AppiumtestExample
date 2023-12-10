list1=[2,5,8,9,3,21,23,44]
def paixu(data,reverse=False):
    if not reverse:
        for i in range(len(data)-1):
            for j in range(len(data)-1-i):
                if data[j]>data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
        return data
    else:
        for i in range(len(data)-1):
            for j in range(len(data)-1-i):
                if data[j]<data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
        return data
print((paixu(list1,reverse=False)))



