# encoding = UTF-8

from http_requests import Http_requests
from readdata import ReadData
from savedata import SaveData
from mylog import Log

log = Log('batch_http_test')

def batch_http_test(request_list):
    hr = Http_requests()
    result = []
    for i in request_list:
        params = {'mobilephone': i[1], 'amount': i[2]}
        if i[3] == 'GET':
            s = hr.get(i[0], params)
        elif i[3] == 'POST':
            s = hr.post(i[0], params)
        else:
            s = '请求方法有误'
        result.append(s)
    return result


test_data = ReadData().read_excel('input.xls','input')
# test_data = ReadData().read_cvs('input.txt')
log.debug(str(test_data))
result = batch_http_test(test_data)
log.debug(str(result))
SaveData().save_excel('output.xls',result,'output')


