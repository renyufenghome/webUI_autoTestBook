# from selenium import webdriver
# import os



# dirver=webdriver.Chrome("./chromedriver.exe")
# dirver.get("https://www.baidu.com")

# dir = os.path.dirname(__file__)
# chrome_driver_path=dir + "\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("http://www.python.org")
# assert "Python" in driver.title




# from selenium import webdriver
# import os
#
# dir =os.path.dirname(__file__)
# chrome_driver_path=dir +"\chromedriver.exe"
# driver=webdriver.Chrome(chrome_driver_path)
# driver.get("http://www.python.org")
# assert "python" in driver.title   # 验证所打开的网页title是否有python关键字
# from selenium import webdriver
# import os
#
# dir=os.path.diname(__file__)
# chrome_driver_path=dir +"\chromedriver.exe"
# driver=webdriver.Chrome(chrome_driver_path)
# driver.get()
# assert "" in driver.title

# import os
# from selenium import webdriver

# dir =os.path.dirname(__file__)
# firefox_driver_path=dir + "\geckodriver.exe"
# driver=webdriver.Firefox(executable_path=firefox_driver_path)
# driver.get("http://www.python.org")
# assert  "Python" in driver.title

#
#
#
# dir = os.path.dirname(__file__)
# ie_driver_path = dir + "\IEDriverServer.exe"
# driver = webdriver.Ie(ie_driver_path)
# driver.get("http://www.python.org")
# assert "Python" in driver.title

from selenium import  webdriver
import os

dir = os.path.dirname(__file__)
chrome_driver_path =dir + "\chromedriver.exe"
driver= webdriver.Chrome(chrome_driver_path)
driver.get("http://www.yahoo.com")
assert "YaHoo" in driver.title

elem=driver.find_element_by_name()
elem.clear()
elem.send_keys("seleniumhq"+Keys.RETURN)


assert "ERR_CONNECTION_TIMED_OUT" in driver.page_source.ENTER
elem_search=driver.find_element_by_id("uh-search-button")

