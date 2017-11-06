import unittest
import time
import HTMLTestRunner
from unittest_http import TestHttp,out
from sendmail import MailCreator
from mylog import Log
from savedata import SaveExcel

# 引用ddt后无法使用
# suite = unittest.TestSuite()
# suite.addTest(TestHttp("test_http"))

suite = unittest.TestLoader().loadTestsFromTestCase(TestHttp)
now = time.strftime('%Y-%m-%d_%H_%M_%S')
log = Log('testsuite')

if __name__ == '__main__':
    # html报告输出设置
    filePath = "HttpTestResult" + now + ".html"
    fp = open(filePath,'wb')

    log.info("测试报告开始...")

    # 生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
    runner.run(suite)

    fp.close()

    # excel输出保存
    out.save()

    log.info("测试报告完成...")

    # 发送邮件信息
    subject = "小黑的测试邮件"
    content = "请查收20171010作业测试报告，谢谢！"
    # msg_to = "215603651@qq.com"
    msg_to = "204893985@qq.com"
    filelist = []
    filelist.append(filePath)
    # MailCreator().send(msg_to,subject,content,filelist)