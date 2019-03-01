import unittest
from demo7.abs  import abs
from ddt import ddt,data,unpack

@ddt
class AbsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始------------------------")
    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_abs(self,n,expect_value):
        result=abs(n)
        self.assertEqual(result,expect_value,msg=result)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
    @classmethod
    def tearDownClass(cls):
        print("结束-------------------------")

