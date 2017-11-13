import unittest
from public.http_request import HttpRequest
from public.readdata import ReadData
from public.savedata import SaveExcel
from public.config import Config
from public.log import Log
from source.recharge.test_recharge import TestRecharge

log = Log('Recharge')

class Recharge:
    def __init__(self):
        self.input_file = Config().getTest("rechargefile","input_file")
        self.input_sheet = Config().getTest("rechargefile","input_sheet")
        self.output_file = Config().getTest("rechargefile","output_file")
        self.output_sheet = Config().getTest("rechargefile","output_sheet")

    def run(self):
        log.debug("run开始执行")
        test_data = ReadData().read_excel(self.input_file, self.input_sheet)
        ws = SaveExcel(self.output_file, self.output_sheet)
        ws.write(0, 0, test_data[0][0])
        ws.write(0, 1, test_data[0][1])
        ws.write(0, 2, 'expect_result')
        ws.write(0, 3, 'actual_result')
        ws.write(0, 4, 'result')
        mode = Config().getTest("rechargemode", "mode")
        if mode == '1':
            run_list = range(1, len(test_data))
        elif mode == '0':
            run_list = eval(Config().getTest("rechargemode", "caselist"))
        else:
            run_list = []
            log.error("mode配置有误")
        suite = unittest.TestSuite()
        row = 1
        for i in run_list:
            case_id = test_data[i][0]
            case_description = test_data[i][1]
            url = test_data[i][3]
            data = {'mobilephone': test_data[i][4], 'amount': test_data[i][5]}
            expect_result = str(test_data[i][6])
            suite.addTest(TestRecharge("test_recharge",row,case_id,case_description,url,data,expect_result,ws))
            row += 1

        unittest.TextTestRunner(verbosity=2).run(suite)
        return ws.path

        log.debug("run结束执行")


