import unittest
import time
import HTMLTestRunner
from unittest_http import TestHttp


suite = unittest.TestSuite()
suite.addTest(TestHttp("test_http_get"))
suite.addTest(TestHttp("test_http_post"))


now = time.strftime('%Y-%m-%d_%H_%M_%S')

if __name__ == '__main__':
    # 执行测试集合
    filePath = "HttpTestResult" + now + ".html"
    fp = open(filePath,'wb')

    # 生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
    runner.run(suite)

