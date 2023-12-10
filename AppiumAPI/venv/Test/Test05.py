class InputOutString(object):
    def __int__(self):
        self.s=""

    def getString(self):
        print("请输入字符串：")
        self.s=input()
    def printString(self):
        print(self.s.upper())


strObj=InputOutString()
strObj.getString()
strObj.printString()

