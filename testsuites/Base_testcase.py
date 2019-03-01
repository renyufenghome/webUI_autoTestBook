import unittest
from selenium import webdriver
# from framework.base import BasePage
from framework.browser_engine import BrowserEngine
class Base_testcase(unittest.TestCase):
    def setUp(self):
        self.browserengine=BrowserEngine()
        # self.driver=self.browserengine.open_browser()
        self.driver=self.browserengine.open_browser()
        # self.driver=webdriver.Chrome('../tools/chromedrivere.exe')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(6)
    def tearDown(self):
        self.driver.quit()