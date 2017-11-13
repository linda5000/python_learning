import sys,os,time
import unittest
from public.log import Log
from public.config import Config
from public.globalpath import savedata_path
from public.sendmail import Mail
from source.recharge.recharge import Recharge
from source.register.register import Register

now = time.strftime('%Y-%m-%d_%H_%M_%S')


class runner:
    def __init__(self,test_interface_list):
        self.test_interface_list = test_interface_list
        self.path = savedata_path
        self.result_list = []


    def run(self):
        interface = eval(Config().getTest("classname","interface"))
        for i in self.test_interface_list:
            self.result_list.append(interface[i]().run())
        return self.result_list



def main():
    log = Log("run")
    run_list = eval(Config().getTest("run","runlist"))
    r = runner(run_list)
    log.debug("主程序run开始运行")
    file_list = r.run()
    log.debug("主程序run结束运行")

    # 邮件发送测试报告
    subject = "项目接口测试结果"
    content = "请查收测试结果，谢谢！"
    msg_to = "204893985@qq.com"
    Mail().send(msg_to,subject,content,file_list)

if __name__ == '__main__':
    main()




