from pageobjects.discuz_homepage import *
import unittest
from testsuites.Base_testcase import Base_testcase
from ddt import *
@ddt
class DisuzSearch3(Base_testcase):
    def test_discez3(self):
        h = HomePage(self.driver)

        h = HomePage(self.driver)
        # h.get("http://127.0.0.1/forum.php")
        h.denglu("admin", "admin")
        h.shuimian(5)


        p=h.sousuo('sdfsdfsdf')

        try:
            self.assertEqual(p,"sdfsdfsdf",msg=p)
        except AssertionError as p:
            print(u"找不到这个标题")

        h.tuich()

if __name__=='__main__':
    unittest.main()