# 我们要在百度首页找到所有的链接，并输出链接文字。
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


driver=webdriver.Chrome("./chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(6)

driver.get("http://www.baidu.com")

elements=driver.find_element_by_tag_name("a")

print("共找到a标签%d个"%len(elements))

for ele in elements:
    print(ele.text)

driver.quit()



