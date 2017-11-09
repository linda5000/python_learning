from test_program.public.http_request import HttpRequest
from test_program.readdata import ReadData
from test_program.savedata import SaveData,SaveExcel

class RechargeTest:
    def __init__(self,input_data,output_data):
        self.input_data = "recharge_data"
        self.output_data = "recharge_result"

    def run(self):
        hr = HttpRequest()
        test_data = read_excel(self.input_file, input_sheet)
        run_list = range(1, len(test_data))
        for i in run_list:
            row = 1
            url = test_data[i][3]
            method = test_data[i][4]
            data = {'mobilephone': test_data[i][1], 'amount': test_data[i][2]}
            if method == 'get':
                s = hr.get(url, data)
            elif method == 'post':
                s = hr.post(url, data)
            else:
                s = '请求方法有误'

            ws.write(row,0,request_list[i][0])
            ws.write(row,1,s)
            row = row + 1
