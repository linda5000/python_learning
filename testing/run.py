# encoding = UTF-8

from http_requests import Http_requests
from readdata import ReadData
from savedata import SaveData,SaveExcel
from mylog import Log
from config import Config
from mysqlconnect import Mysql

log = Log('Http_test')

class Http_test:
    def __init__(self,input_file=None,input_sheet=None,output_file=None,output_sheet=None):
        if input_file is None:
            self.input_file = 'input.xls'
        else:
            self.input_file = input_file
        if input_sheet is None:
            self.input_sheet = 'input'
        else:
            self.input_sheet = input_sheet
        if output_file is None:
            self.output_file = 'output.xls'
        else:
            self.output_file = output_file
        if output_sheet is None:
            self.output_sheet = 'output'
        else:
            self.output_sheet = output_sheet


    def run(self):
        mode = Config().getConfig("flag","mode")
        request_list = ReadData().read_excel(self.input_file, self.input_sheet)
        if mode == '1':
            run_list = range(1,len(request_list))
        elif mode == '0':
            run_list = eval(Config().getConfig("flag","caselist"))
        else:
            run_list = []
            log.error("mode配置有误")

        hr = Http_requests()

        ws = SaveExcel(self.output_file, self.output_sheet)
        ws.write(0, 0, 'id')
        ws.write(0, 1, 'run_result')
        # ws.write(0, 2, 'test_result')

        # 数据建表准备
        db = Mysql()
        creat_table_sql = '''create  table IF NOT EXISTS
            httptest_record(
            id int(12) auto_increment  primary key,
            case_no  int(10) not null,
            url varchar(2000),
            method varchar(255),
            data1 varchar(255),
            data2 varchar(255),
            data3 varchar(255),
            data4 varchar(255),
            run_result varchar(2000),
            test_result varchar(10),
            run_date date) DEFAULT CHARSET=utf8
        '''
        db.ddl(creat_table_sql)
        row = 1
        for i in run_list:
            params = {request_list[0][3]: request_list[i][3], request_list[0][4]: request_list[i][4]}
            if request_list[i][2] == 'GET':
                s = hr.get(request_list[i][1], params)
            elif request_list[i][2] == 'POST':
                s = hr.post(request_list[i][1], params)
            else:
                s = '请求方法有误'

            log.debug(s)
            ws.write(row,0,request_list[i][0])
            ws.write(row,1,s)
            row = row + 1
            sql = '''insert into httptest_record(case_no,url,method,data1,data2,run_result,run_date) VALUES (%s,%s,%s,%s,%s,%s,now())'''
            db.insert(sql,(i,request_list[i][1],request_list[i][2],request_list[i][3],request_list[i][4],s))
        ws.save()

def main():
    Http_test().run()

if __name__ == '__main__':
    main()





