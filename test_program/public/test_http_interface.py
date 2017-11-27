import unittest
from public.http_request import HttpRequest
from public.readdata import ReadData
from public.savedata import SaveExcel
from public.config import Config
from public.log import Log

log = Log('TestHttpInterface')

class TestHttpInterface(unittest.TestCase):
    def __init__(self,methodName,row, case_id, case_description, url, data, expect_result, save_sheet_obj):
        super(TestHttpInterface,self).__init__(methodName)
        self.row = row
        self.case_id = case_id
        self.case_description = case_description
        self.url = url
        self.data = data
        self.expect_result = expect_result
        self.save_sheet_obj = save_sheet_obj



    def setUp(self):
        log.info('测试用例开始执行')


    def runTest(self):
        hr = HttpRequest()
        actual_result = None
        result = ''
        try:
            response_get = hr.post(self.url, self.data)
            response_post = hr.post(self.url, self.data)
        except Exception as e:
            result = 'error'
            log.error(e)
            raise e
        else:
            output_get = response_get['code']
            output_post = response_post['code']
            if output_get == output_post:
                actual_result = output_get
            else:
                actual_result = "GET和POST方法响应结果不一致:" + "GET方法结果" + output_get + "POST方法结果" + output_post
            try:
                self.assertEqual(actual_result, self.expect_result)
                result = 'pass'
            except AssertionError as e:
                result = 'fail'
                raise e

        finally:
            self.save_sheet_obj.write(self.row, 0, self.case_id)
            self.save_sheet_obj.write(self.row, 1, self.case_description)
            self.save_sheet_obj.write(self.row, 2, self.expect_result)
            self.save_sheet_obj.write(self.row, 3, actual_result )
            self.save_sheet_obj.write(self.row, 4, result)
            self.save_sheet_obj.save()



    def tearDown(self):
        log.info('测试用例结束执行')