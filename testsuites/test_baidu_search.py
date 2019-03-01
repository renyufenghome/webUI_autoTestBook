import unittest
from testsuites.Base_testcase import Base_testcase
from pageobjects.baidu_homepage import HomePage
class BaiDuSearch(Base_testcase):
    def test_baidu(self):
        h=HomePage(self.driver)
        h.get("")
        h.shuru("")
        h.shuimian()


if __name__=='__main__':
    unittest.main()