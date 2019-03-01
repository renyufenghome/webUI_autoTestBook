import unittest
from testsuites.Base_testcase import Base_testcase
# from testsuites.Base_testcase import Base_testcase
from pageobjects.discuz_homepage import *
import HTMLTestRunner
class DiscuzSearch1(Base_testcase):
    def test_discuz1(self):
        h=HomePage(self.driver)
        # h.get("http://127.0.0.1/forum.php")
        h.denglu("admin","admin")
        h.shuimian(5)
        # 发帖 标题和正文
        h.fatie("任宇峰","11111111111111111111111")
        h.shuimian(3)
        # logout=TuichuPage  回帖
        h.huitie("5555555555555555555")
        h.shuimian(5)
        # 退出
        h.tuich()
if __name__=='__main__':
    unittest.main()

# HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="测试报告",description="用例执行情况")
# unittest.main()
