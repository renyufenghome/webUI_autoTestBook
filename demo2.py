# import os
# from selenium import webdriver
# import time
# driver=webdriver.Chrome("./chromedriver.exe")
# try:
#     driver.implicitly_wait(5)  #操作等待时间，10秒，默认等待  5秒
#     driver.get("http://www.baidu.com")
#
#     #激活当前窗口
#     driver.switch_to.window(driver.current_window_handle)
#
#
#     # 控制台输出信息
#     print("百度首页已经打开：", driver.title)
#
#     #查找  搜索框，  通过 id=kw
#     search_input =driver.find_element_by_id("kw")
#
#     #找到后，键入 java 并提交搜索
#     search_input.send_keys("java")
#     search_input.submit()
#
#     #获取页面中  “百度为您找到相关结果约55，888，000个”相关文字的元素
#     nums =driver.find_element_by_class_name("nums")
#
#     #控制台打印信息
#     print("-----------",nums.text)
#
#     #再次激活窗口
#     driver.switch_to.window(driver.current_window_handle)
#
#     #执行脚本，显示一个框提示用户
#     wait_second= 10
#     driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","$"),wait_second))
#     time.sleep(wait_second)
#
# finally:
#     driver.quit()






























import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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