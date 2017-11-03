import unittest
from http_requests import Http_requests
from mylog import Log
import ddt

log = Log('unittest')

test_data = [['/futureloan/mvc/api/member/recharge',{'mobilephone':'13667692121','amount':1000},'10001'],\
             ['/futureloan/mvc/api/member/recharge',{'mobilephone':'13667692121','amount':1000},'10001']]

@ddt.ddt
class TestHttp(unittest.TestCase):
    def setUp(self):
        # Log('unittest').info('测试用例开始')  # 如果不在开始就创建日志对象，而是使用时才创建会error
        log.info('测试用例TestHttp开始...')

    @ddt.data(*test_data)
    @ddt.unpack
    def test_http_get(self,request_list):
        r = Http_requests()
        url = request_list[i][1]
        data = {request_list[0][3]: request_list[i][3], request_list[0][4]: request_list[i][4]}
        response = r.get(url,data)
        result =  response['code']
        self.assertEqual(result,expectresult)
        log.info('TestHttp get方法...')


    @ddt.data(*test_data)
    @ddt.unpack
    def test_http_post(self,url,data,expectresult):
        r = Http_requests()
        response = r.post(url,data)
        result = response['code']
        self.assertEqual(result,expectresult)
        log.info('TestHttp post方法...')


    def tearDown(self):
        log.info('测试用例TestHttp结束...')


if __name__ == '__main__':
    unittest.main()


