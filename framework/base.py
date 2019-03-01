from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time
from framework.logger import Logger

logger= Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        logger.info("Click back on curront page")
    def get(self,url):
        self.driver.get(url)
    def frame(self,*loc):
        e1=self.find_element(*loc)
        self.driver.switch_to.frame(e1)
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logger.info("未找到页面元素")
    def sendkeys(self,text,*loc):
        e1=self.find_element(*loc)
        e1.clear()
        e1.send_keys(text)
        logger.info("输入内容")
    def jihuo(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def click(self,*loc):
        e1=self.find_element(*loc)
        e1.click()
    def shuimian(self,n):
        time.sleep(n)
    def change_window(self):
        window_list=self.driver.window_handles
        self.driver.switch_to.window(window_list[len(window_list)-1])

    def iframe(self):
        self.driver.switch_to.frame(0)

    def text(self,*loc):
        e1=self.find_element(*loc)
        logger.info("获取内容成功")
        return e1.text


