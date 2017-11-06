import unittest
import ddt
from http_requests import Http_requests
from mylog import Log
from loaddata import LoadData
from savedata import SaveExcel

test_data = LoadData().test_data
log = Log('unittest')
row = 0
out = SaveExcel('output.xls', 'Output')
out.write(row, 0, 'id')
out.write(row, 1, 'result')
out.write(row, 2, 'output')

@ddt.ddt
class TestHttp(unittest.TestCase):
    def setUp(self):
        # Log('unittest').info('测试用例开始')  # 如果不在开始就创建日志对象，而是使用时才创建会error
        log.info('测试用例TestHttp开始...')


    def http_get(self,id,url,data,expectresult):
        global row
        global out
        log.info('TestHttp get方法...')
        r = Http_requests()
        response = r.get(url,data)
        output =  response['code']
        try:
            self.assertEqual(output,expectresult)
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            row += 1
            out.write(row, 0, id)
            out.write(row, 1, result)
            out.write(row, 2, output)



    def http_post(self,id,url,data,expectresult):
        global row
        global out
        log.info('TestHttp post方法...')
        r = Http_requests()
        response = r.post(url,data)
        output = response['code']
        try:
            self.assertEqual(output,expectresult)
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            row += 1
            out.write(row, 0, id)
            out.write(row, 1, result)
            out.write(row, 2, output)

    @ddt.data(*test_data)
    # @ddt.unpack
    def test_http(self,test_data):
        global row
        global out
        id = test_data[0]
        url = test_data[1]
        data = {'mobilephone': test_data[3], 'amount': test_data[4]}
        expectresult = str(test_data[5])
        if test_data[2] == 'GET':
            self.http_get(id,url,data, expectresult)
        elif test_data[2] == 'POST':
            self.http_post(id,url,data,expectresult)
        else:
            row += 1
            out.write(row, 0, id)
            out.write(row, 1, 'error')
            log.error("请求方法错误")
            raise Exception("请求方法错误")



    def tearDown(self):
        log.info('测试用例TestHttp结束...')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHttp)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    out.save()



