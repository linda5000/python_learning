import unittest
import HTMLTestRunner
import time
from public.http_request import HttpRequest
from public.readdata import ReadData
from public.savedata import SaveExcel
from public.config import Config
from public.log import Log
from source.register.test_register import TestRegister
from public.globalpath import savedata_path

log = Log('Register')

class Register:
    def __init__(self):
        self.input_file = Config().getTest("registerfile","input_file")
        self.input_sheet = Config().getTest("registerfile","input_sheet")
        self.output_file = Config().getTest("registerfile","output_file")
        self.output_sheet = Config().getTest("registerfile","output_sheet")

    def run(self):
        log.debug("run开始执行")
        test_data = ReadData().read_excel(self.input_file, self.input_sheet)
        ws = SaveExcel(self.output_file, self.output_sheet)
        ws.write(0, 0, test_data[0][0])
        ws.write(0, 1, test_data[0][1])
        ws.write(0, 2, 'expect_result')
        ws.write(0, 3, 'actual_result')
        ws.write(0, 4, 'result')
        mode = Config().getTest("registermode", "mode")
        if mode == '1':
            run_list = range(1, len(test_data))
        elif mode == '0':
            run_list = eval(Config().getTest("registermode", "caselist"))
        else:
            run_list = []
            log.error("mode配置有误")

        suite = unittest.TestSuite()

        row = 1
        for i in run_list:
            case_id = test_data[i][0]
            case_description = test_data[i][1]
            url = test_data[i][3]
            data = {'mobilephone': test_data[i][4], 'pwd': test_data[i][5],'regname':test_data[i][6]}
            expect_result = str(test_data[i][7])
            suite.addTest(TestRegister("test_register",row,case_id,case_description,url,data,expect_result,ws))
            row += 1

        # unittest.TextTestRunner(verbosity=2).run(suite)

        repoert_path = savedata_path + "test_recharge_Result" + time.strftime('%Y-%m-%d_%H_%M_%S') + ".html"
        fp = open(repoert_path, 'wb')

        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='Python Test Report',
                                               description='This  is Python  Report')
        runner.run(suite)
        fp.close()

        log.debug("run结束执行")

        return repoert_path



