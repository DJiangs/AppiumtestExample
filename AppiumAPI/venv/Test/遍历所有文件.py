import  os
path="D:\\apachejmeter31"
filename="123"
result=[]

def findfiles(path):
    file_list=os.listdir(path)
    for file in file_list:
        cur_path=os.path.join(path,file)
        if os.path.isdir(cur_path):
            findfiles(cur_path)
        else:
           ## if filename in file:
            result.append(file)

if __name__=='__main__':
    findfiles(path)
    print(result)