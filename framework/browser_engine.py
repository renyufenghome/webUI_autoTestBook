import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger
logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chromr_driver_path=dir +'/tools/chromedriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    firefox_driver_path=dir+'/tools/geckodriver.exe'
    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.')) +'/config/config.ini'
        config.read(file_path)
        browser=config.get("browserType","browserName")
        logger.info("读取浏览器成功")
        url=config.get("testServer","url")
        logger.info("找到URL：%s"%url)
        if browser=="Firefox":
            logger.info("火狐浏览器")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chromr_driver_path)
            logger.info("谷歌浏览器")
        else:
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("IE浏览器")

        self.driver.get(url)
        logger.info("打开浏览器%s"%url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver
    def quit_brower(self):
        logger.info("关闭浏览器")
        self.driver.quit()