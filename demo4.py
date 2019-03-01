# 糗事百科文字加代码的显示以及下一页

import os
from selenium import webdriver
import time

driver=webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.qiushibaike.com/text/")
yeshu=driver.find_element_by_css_selector('.pagination li:nth-last-child(2)').text
for n in range(1,int(yeshu)+1):
    print("************************************************这里是：", n)
    zuozhe_list = driver.find_elements_by_css_selector("h2")
    zhengwen_list = driver.find_elements_by_css_selector(".content")
    haoxiao_list = driver.find_elements_by_css_selector(".stats-vote")
    for i in range(0, len(zuozhe_list) - 1):
        print("第", i + 1, "条:\n作者:", zuozhe_list[i].text, "\n笑话正文:", zhengwen_list[i].text, "\n好笑数:",
              haoxiao_list[i].text, "\n")

    if driver.find_element_by_css_selector('.pagination li:last-of-type').text=="下一页":
        g=driver.find_element_by_css_selector('.next')
        g.click()









