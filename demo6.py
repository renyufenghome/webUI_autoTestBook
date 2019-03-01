from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")
time.sleep(1)
driver.execute_script("window.alert('这是一个弹出框！')")

# time.sleep(2)
# driver.switch_to.alert.accept()
