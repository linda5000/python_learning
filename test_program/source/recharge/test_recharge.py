import unittest
from public.http_request import HttpRequest
from public.readdata import ReadData
from public.savedata import SaveExcel
from public.config import Config
from public.log import Log

log = Log('RechargeTest')

class TestRecharge(unittest.TestCase):
    def __init__(self,methodName,id, row,url,data,expectresult,save_sheet_obj):
        super(TestRecharge,self).__init__(methodName)
        self.id = id
        self.row = row
        self.url = url
        self.data = data
        self.expectresult = expectresult
        self.save_sheet_obj = save_sheet_obj



    def setUp(self):
        log.info('测试用例开始执行')


    def test_recharge(self):
        hr = HttpRequest()
        result = ''
        try:
            response_get = hr.post(self.url, self.data)
            response_post = hr.post(self.url, self.data)
        except Exception as e:
            output = {}
        else:
            output_get = response_get['code']
            output_post = response_post['code']

        if output_get == output_post:
            output = output_get
        else:
            output = "GET和POST方法响应结果不一致:" + "GET方法结果" + output_get + "POST方法结果" + output_post

        try:
            self.assertEqual(output, self.expectresult)
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            self.save_sheet_obj.write(self.row, 0, self.id)
            self.save_sheet_obj.write(self.row, 1, output )
            self.save_sheet_obj.write(self.row, 2, result)
            self.save_sheet_obj.save()


    def tearDown(self):
        log.info('测试用例结束执行')