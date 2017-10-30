# encoding = UTF-8

from http_requests import Http_requests
from readdata import ReadData
from savedata import SaveData
from mylog import Log
from config import Config

log = Log('batch_http_test')

def batch_http_test(request_list):
    mode = Config().getConfig("flag","mode")
    print(mode)
    hr = Http_requests()
    result = []
    if mode == '1':
        for i in request_list:
            params = {'mobilephone': i[1], 'amount': i[2]}
            if i[3] == 'GET':
                s = hr.get(i[0], params)
            elif i[3] == 'POST':
                s = hr.post(i[0], params)
            else:
                s = '请求方法有误'
            result.append(s)
    elif mode == '0':
        run_list = eval(Config().getConfig("flag","caselist"))
        for i in run_list:
            params = {'mobilephone': request_list[i-1][1], 'amount': request_list[i-1][2]}
            if request_list[i-1][3] == 'GET':
                s = hr.get(request_list[i-1][0], params)
            elif request_list[i-1][3] == 'POST':
                s = hr.post(request_list[i-1][0], params)
            else:
                s = '请求方法有误'
            result.append(s)
    else:
        print("mode配置有误")

    return result


test_data = ReadData().read_excel('input.xls','input')
# test_data = ReadData().read_cvs('input.txt')
log.debug(str(test_data))
result = batch_http_test(test_data)
log.debug(str(result))
SaveData().save_excel('output.xls',result,'output')


