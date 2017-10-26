import unittest
import time
import HTMLTestRunner
from unittest_20171010 import TestMath


suite = unittest.TestSuite()
suite.addTest(TestMath("test_add"))
suite.addTest(TestMath("test_sub"))
print(suite)
runner = unittest.TextTestRunner()
runner.run(suite)

now = time.strftime('%Y-%m-%d_%H_%M_%S')

if __name__ == '__main__':
    # 执行测试集合
    filePath = "pyResult" + now + ".html"
    # fp = open(filePath,'wb')

    # 生成报告的Title,描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
    # runner.run(suite)

