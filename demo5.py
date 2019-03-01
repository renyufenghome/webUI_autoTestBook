#拉勾网 页面转换

from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


dir=os.path.dirname(__file__)    #根目录
chrome_path_driver=dir+"\chromedriver.exe"   #
driver=webdriver.Chrome(chrome_path_driver)     #

try:
      driver.maximize_window()    #使窗口最大化
      driver.implicitly_wait(6)    #隐性等待
      driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")    #通过get方法得到这个页面
      driver.switch_to.window(driver.current_window_handle)    #激活这个窗口

      while True:
          main_yemian=driver.find_elements_by_css_selector(".position_link h3")
          for i in range(0, 1):
              main_yemian[i].click()
              driver.switch_to.window(driver.window_handles[1])
              jobs=driver.find_element_by_css_selector(".job-name .name")
              money=driver.find_element_by_css_selector(".job_request .salary")
              jingyan=driver.find_element_by_css_selector(".job_request p:nth-child(3)")

              print("工作为：",jobs.text)
              print("薪资为：",money.text)
              print("工作经验为：",jingyan.text)
              driver.close()
              driver.switch_to.window(driver.window_handles[0])
          page_nums = \
              WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pager_container:last-child')))    # 显性等待
          page_num = page_nums.get_attribute("class")

          if "pager_next_disabled" in page_num:
              break
          else:
            page_nums.click()
            time.sleep(3)



finally:
    time.sleep(5)
    driver.quit()


