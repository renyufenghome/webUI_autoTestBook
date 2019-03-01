from selenium import webdriver
import os

# 打开一个chorme浏览器，python官网

# dir = os.path.dirname(__file__)
# chrome_driver_path = dir + "\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("http://www.python.org")
# assert "Python" in driver.title


from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time
driver=os.path.dirname(__file__)
chrome_driver_path=+"\chromedriver.exe"
dir=webdriver.Chrome("chrome_driver_path")
dir.implicitly_wait(5)
dir.get("https://www.qiushibaike.com/text/")
dd=dir.find_element_by_css_selector('.pagination li:nth-last-child(2)').text
for qq in range(1,int(dd)+1):
    print("************************************************这里是：", qq)
    mingzi=dir.find_elements_by_css_selector('.author h2')
    content = dir.find_elements_by_css_selector('.content')
    haoxiao=dir.find_elements_by_css_selector('.stats')
    for i in range(0,len(mingzi)):
        print("作者是：",mingzi[i].text)
        print("内容是：",content[i].text)
        print(haoxiao[i].text)
        print("------------------------")
    if dir.find_element_by_css_selector('.pagination li:last-of-type').text=="下一页":
        g=dir.find_element_by_css_selector('.next')
        g.click()