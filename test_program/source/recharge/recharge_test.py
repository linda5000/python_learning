
from public.http_request import HttpRequest
from public.readdata import ReadData
from public.savedata import SaveExcel

class RechargeTest:
    def __init__(self):
        self.input_file = "recharge_data.xls"
        self.input_sheet = "test_data"
        self.output_file = "recharge_result.xls"
        self.output_sheet = "test_result"

    def run(self):
        hr = HttpRequest()
        test_data = ReadData().read_excel(self.input_file, self.input_sheet)
        run_list = range(1, len(test_data))
        ws = SaveExcel(self.output_file, self.output_sheet)
        ws.write(0, 0, 'id')
        ws.write(0, 1, 'run_result')
        row = 1
        for i in run_list:
            url = test_data[i][3]
            method = test_data[i][4]
            data = {'mobilephone': test_data[i][1], 'amount': test_data[i][2]}
            if method == 'get':
                s = hr.get(url, data)
            elif method == 'post':
                s = hr.post(url, data)
            else:
                s = '请求方法有误'

            ws.write(row,0,test_data[i][0])
            ws.write(row,1,str(s))
            ws.save()
            row += 1
