import sys,os,time
import unittest
from public.log import Log
from public.config import Config
from public.globalpath import savedata_path
from public.sendmail import Mail
from source.recharge.recharge_test import TestRecharge
from source.register.register_test import TestRegister

now = time.strftime('%Y-%m-%d_%H_%M_%S')


class runner:
    def __init__(self,test_interface_list):
        self.test_interface_list = test_interface_list
        self.path = savedata_path


    def run(self):
        interface = eval(Config().getTest("classname","interface"))
        reportpath_list = []
        for i in self.test_interface_list:
            reportpath = path + i + "Result" + now + ".html"
            fp = open(reportpath, 'wb')
            suite = unittest.TestLoader().loadTestsFromTestCase(interface[i]())
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report',description='This  is Python  Report')
            runner.run(suite)
            fp.close()
            reportpath_list.append(reportpath)
        return reportpath_list



def main():
    log = Log("run")
    run_list = eval(Config().getTest("run","runlist"))
    r = runner(run_list)
    log.debug("主程序run开始运行")
    filelist = r.run()
    log.debug("主程序run结束运行")

    # 邮件发送测试报告
    subject = "项目接口测试报告"
    content = "请查收测试报告，谢谢！"
    msg_to = "204893985@qq.com"
    # Mail().send(msg_to,subject,content,filelist)

if __name__ == '__main__':
    main()




