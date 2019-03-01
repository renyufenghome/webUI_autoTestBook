from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

dir=os.path.dirname(__file__)
chrome_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
try:
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1/forum.php')
    username=driver.find_element_by_name("username")
    username.send_keys('admin')
    password=driver.find_element_by_name("password")
    password.send_keys('admin'+Keys.RETURN)
    login=driver.find_element_by_tag_name("em")
    login.click()
    moreng=driver.find_element_by_xpath("//td/h2/a")
    moreng.click()
    fatie=driver.find_element_by_id("newspecial")
    fatie.click()
    # faabioa=driver.find_elements_by_css_selector(".hidefocus")
    # ActionChains(driver).move_to_element(fatie).click(faabioa).perform()
    content1=driver.find_element_by_name('subject')
    content1.send_keys("发帖")
    frame=driver.switch_to.frame(0)
    time.sleep(5)
    content2=driver.find_element_by_xpath("//body[@spellcheck='false']")
    content2.send_keys("发帖")
    frame1=driver.switch_to.window(driver.current_window_handle)
    fatiesub=driver.find_element_by_name("topicsubmit")
    fatiesub.click()
    huifu=driver.find_element_by_css_selector(".fastre")
    huifu.click()
    huifucontent=driver.find_element_by_id("postmessage")
    time.sleep(5)
    huifucontent.send_keys('回复')
    time.sleep(5)
    huifutitle=driver.find_element_by_xpath("//button/span")
    huifucontent.click()
    exit=driver.find_element_by_link_text("退出")
    exit.click()



finally:
    time.sleep(5)
    driver.quit()
