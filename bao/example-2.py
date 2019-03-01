from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

'''
用户的浏览器行为：
open a new chrome browser
load the Yahoo homepage
search for “seleniumhq”
close the browser
'''
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.yahoo.com/')
assert 'Yahoo' in driver.title

elem = driver.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

driver.quit()