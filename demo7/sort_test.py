import  unittest
from ddt import *
from demo7.sort import sort

@ddt
class SortTest(unittest.TestCase):
    def setUp(self):
        print("开始")
    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack

    def test_sort(self,num,type,expect_value):
        result=sort(num,type)
        self.assertEqual(result,expect_value,msg= result)
    def tearDown(self):
        print("结束测试")

if __name__=='__main__':
    unittest.main(verbosity=2)


