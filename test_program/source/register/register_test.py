from public.http_request import HttpRequest
from public.readdata import ReadData
from public.savedata import SaveExcel
from public.config import Config
from public.log import Log

log = Log('RegisterTest')

class RegisterTest:
    def __init__(self):
        c = Config()
        self.input_file = c.getTest("registerfile","input_file")
        self.input_sheet = c.getTest("registerfile","input_sheet")
        self.output_file = c.getTest("registerfile","output_file")
        self.output_sheet = c.getTest("registerfile","output_sheet")

    def run(self):
        log.debug("run开始执行")
        hr = HttpRequest()
        test_data = ReadData().read_excel(self.input_file, self.input_sheet)
        ws = SaveExcel(self.output_file, self.output_sheet)
        ws.write(0, 0, 'id')
        ws.write(0, 1, 'output')
        mode = Config().getTest("registermode", "mode")
        if mode == '1':
            run_list = range(1,len(test_data))
        elif mode == '0':
            run_list = eval(Config().getTest("registermode","caselist"))
        else:
            run_list = []
            log.error("mode配置有误")
        row = 1
        for i in run_list:
            url = test_data[i][4]
            method = test_data[i][5].upper()
            data = {'mobilephone': test_data[i][1], 'pwd': test_data[i][2],'regname':test_data[i][3]}
            if method == 'GET':
                s = hr.get(url, data)
            elif method == 'POST':
                s = hr.post(url, data)
            else:
                s = '请求方法有误'
            log.debug("测试用例" + str(test_data[i][0]) + "执行结果：" + str(s))
            ws.write(row,0,test_data[i][0])
            ws.write(row,1,str(s))
            ws.save()
            row += 1
        log.debug("run结束执行")
