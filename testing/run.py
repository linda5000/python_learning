# encoding = UTF-8

from http_requests import Http_requests
from readdata import ReadData
from savedata import SaveData,SaveExcel
from mylog import Log
from config import Config
from mysqlconnect import Mysql

log = Log('batch_http_test')

def batch_http_test(request_list):
    mode = Config().getConfig("flag","mode")
    if mode == '1':
        run_list = range(1,len(request_list))
    elif mode == '0':
        run_list = eval(Config().getConfig("flag","caselist"))
    else:
        run_list = []
        print("mode配置有误")

    hr = Http_requests()
    result = []
    db = Mysql()
    ws = SaveExcel('output.xls', 'output')
    ws.write(0, 0, 'id')
    ws.write(0, 1, 'run_result')
    ws.write(0, 2, 'test_result')
    row = 1
    for i in run_list:
        params = {request_list[0][3]: request_list[i][3], request_list[0][4]: request_list[i][4]}
        if request_list[i][2] == 'GET':
            s = hr.get(request_list[i][1], params)
        elif request_list[i][2] == 'POST':
            s = hr.post(request_list[i][1], params)
        else:
            s = '请求方法有误'
        result.append(s)
        ws.write(row,0,request_list[i][0])
        ws.write(row,1,s)
        row = row + 1
        db.insert((request_list[i][0],s))
    ws.save()

    return result


test_data = ReadData().read_excel('input.xls','input')
log.debug(str(test_data))
result = batch_http_test(test_data)



