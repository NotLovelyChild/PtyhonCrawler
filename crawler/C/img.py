# import unittest
# from selenium import webdriver
# from PIL import Image, ImageEnhance
# import pytesseract
# import time
#
# url = "http://test.chexiao.co:9025/#/login"  # 网站路径
# screenImg = "E:/png/screenImg.png"
# username = "cxadmin"
# password = "111111"
# png = "ew"
#
#
# class TestLogin(unittest.TestCase):
#         def setUp(self):
#                 self.driver = webdriver.Chrome()  # 打开chrome浏览器
#                 self.driver.maximize_window()  # 浏览器窗口最大化
#                 self.driver.get(url)  # 地址栏输入测试地址
#
#         # 登录的操作
#         def test_login(self):
#                 self.driver.find_element_by_id("username").send_keys(username)  # 输入用户名
#                 print('用户名：'+username)
#                 self.driver.find_element_by_id("password").send_keys(password)  # 输入密码
#                 print('密码：'+password)
#                 # 验证码输入框元素
#                 # self.driver.find_element_by_xpath("/html/body/div/form/div/div[3]/div/div/input").send_keys(png)
#                 # print('验证码：'+png)
#
#                 self.driver.save_screenshot('D://aa.png')  #截取当前网页，该网页有我们需要的验证码
#                 imgelement = self.driver.find_element_by_id("imgObj") #定位验证码
#                 location = imgelement.location  #获取验证码x,y轴坐标
#                 size = imgelement.size  #获取验证码的长宽
#                 rangle=(print(int(location['x']), int(location['y']), int(location['x']+size['width']),int(location['y']+size['height']))) #写成我们需要截取的位置坐标
#                 i=Image.open("D://aa.png") #打开截图
#                 frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
#                 frame4.save('D://frame4.png')
#                 img = Image.open('D://frame4.png')
#                 print(img.load())
#                 aa = pytesseract.image_to_string(img)
#                 print(u"识别的验证码为：")
#                 print(aa)
#                 if aa == "":               #如果识别为空，则再一次识别
#                     self.driver.find_element_by_id("imgObj").click()
#                     self.test_login()
#                 self.driver.find_element_by_xpath("/html/body/div/form/div/div[3]/div/div/input").send_keys(aa)
#                 time.sleep(3)
#                 # 点击登录按钮，进行登录
#                 self.driver.find_element_by_xpath("/html/body/div/form/div/button").click()
#                 time.sleep(3)
#         def tearDown(self):
#                 self.driver.quit()  # 关闭浏览器
#
#
# if __name__ == '__main__':
#         unittest.main()
#
#
#
