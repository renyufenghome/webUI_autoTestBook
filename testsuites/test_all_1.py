import unittest
import HTMLTestRunner
import os
from testsuites.test_discuz_search import DiscuzSearch1
from testsuites.test_discuz_search2 import DisuzSearch2
from testsuites.test_discuz_search3 import DisuzSearch3
from testsuites.test_discuz_search4 import DisuzSearch4

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,'report')
if not os.path.exists(report_path):os.mkdir(report_path)

suite =unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSearch1))
suite.addTest(unittest.makeSuite(DisuzSearch2))
suite.addTest(unittest.makeSuite(DisuzSearch3))
suite.addTest(unittest.makeSuite(DisuzSearch4))


if __name__=='__main__':
    html_report=report_path + r"\result.html"
    fp=open(html_report,"wb")

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,
            title="单元测试报告",description="用例执行情况")
    runner.run(suite)



