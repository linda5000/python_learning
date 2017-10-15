import unittest
import time
import HTMLTestRunner
from unittest_http import TestHttp
from sendmail import MailCreator
from mylog import Log


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
    Log('testsuite').info("测试报告开始...")
    runner.run(suite)
    Log('testsuite').info("=测试报告完成...")

    fp.close()

    mail = MailCreator()

    # 发送邮件信息
    subject = "小黑的测试邮件"
    content = "请查收20171010作业测试报告，谢谢！"
    # msg_to = "215603651@qq.com"
    msg_to = "204893985@qq.com"
    filelist = ['tx.gif']
    filelist.append(filePath)
    mail.send(msg_to,subject,content,filelist)