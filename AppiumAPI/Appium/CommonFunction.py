from time import sleep
import datetime
import os



# 带日期截图函数
def takeScreenShot(driver, name="ScreenShot"):
    '''
        method explain:获取当前屏幕的截图
        parameter explain：【name】 截图的名称
        Usage:
            device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2019-01-13_17_10_58_ScreenShot.png
        '''
    day = datetime.datetime.now().strftime("%Y-%m-%d")
    fq = "screenShots\\" + day
    # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
    tm = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    type = '.png'
    filename = ""
    if os.path.exists(fq):
        filename = fq + "\\" + tm + "_" + name + type
        print(filename + "exists")
    else:
        os.makedirs(fq)
        filename = fq + "\\" + tm + "_" + name + type
        print(filename + "else")
    # 实际截图api
    driver.get_screenshot_as_file(filename)


if __name__ == '__main__':
    appinumTest()
