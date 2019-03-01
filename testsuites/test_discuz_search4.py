from pageobjects.discuz_homepage import *
import unittest
from testsuites.Base_testcase import Base_testcase

class DisuzSearch4(Base_testcase):
    def test_discez4(self):
        h = HomePage(self.driver)
        h.denglu("admin", "admin")
        h.shuimian(5)



        h.toupiao("任宇峰","这是第一个","这是第二个")



        h.tuich()
if __name__=='__main__':
    unittest.main()