from pageobjects.discuz_homepage import *
import unittest
from testsuites.Base_testcase import Base_testcase

class DisuzSearch2(Base_testcase):
    def test_discez2(self):
        h = HomePage(self.driver)

        h = HomePage(self.driver)
        # h.get("http://127.0.0.1/forum.php")
        h.denglu("admin", "admin")
        h.shuimian(5)

        #删除帖子
        h.shantie()
        # 板块部分

        h.bankuai("这是一个新板块")
        #退出


        h.tuich()

        #普通用户登录
        h.denglu("ryf", "13233344305yl")
        h.shuimian(5)

        # 发帖 标题和正文
        h.faxintie("任宇峰", "111111111111111111111")
        h.shuimian(3)
        # logout=TuichuPage  回帖
        h.huitie("5555555555555555555")
        h.shuimian(5)
        # 退出
        h.tuich()




