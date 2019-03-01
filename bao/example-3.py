import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(5)  # 操作等待超时时间，10秒，默认等待  5 秒
    driver.get("http://www.baidu.com")

    # 激活当前窗口
    driver.switch_to.window(driver.current_window_handle)

    # 控制台输出信息
    print('百度首页已打开：', driver.title)

    # 查找 搜索框, 通过 id=kw
    search_input = driver.find_element_by_id('kw')

    # 找到后，键入 java 并提交搜索
    search_input.send_keys('java')
    search_input.submit()

    # 获取页面中 "百度为您找到相关结果约55,800,000个" 相关文字的元素
    nums = driver.find_element_by_class_name('nums')

    # 控制台打印信息
    print("----------",nums.text)
    #百度工具$为您找到相关结果约55, 800, 000个

    # 再次激活窗口
    driver.switch_to.window(driver.current_window_handle)

    # 执行脚本，显示一个框提示用户
    wait_seconds = 10
    driver.execute_script("window.alert('{}, {}秒后关闭')".format(nums.text.replace("\n", "$"), wait_seconds))

    time.sleep(wait_seconds)
    # self.assertTrue(True, '成功')
finally:
    driver.quit()