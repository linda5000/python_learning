import unittest
import json
from http_requests import Http_requests
from mylog import Log

log = Log('unittest')

class TestHttp(unittest.TestCase):
    def setUp(self):
        # Log('unittest').info('测试用例开始')  # 如果不在开始就创建日志对象，而是使用时才创建会error
        log.info('测试用例开始...')

    def test_http_get(self):
        ip = 'http://119.23.241.154:8080/'
        url = '/futureloan/mvc/api/member/recharge'
        data = {'mobilephone':'13667692121','amount':1000}
        r = Http_requests(ip)
        response = r.get(url,data)
        result =  json.loads(response)['code']
        self.assertEqual(result,"10001")


    def test_http_post(self):
        ip = 'http://119.23.241.154:8080/'
        url = '/futureloan/mvc/api/member/register'
        data = {'mobilephone':'13667692122','pwd':'987654321'}
        r = Http_requests(ip)
        response = r.post(url,data)
        result = json.loads(response)['code']
        try:
            self.assertEqual(result,"10001")
        except AssertionError as e:
            log.error('断言异常')
            print(e) # 有这个print用例会error，没有则为false
            raise e


    def tearDown(self):
        log.info('测试用例结束...')


if __name__ == '__main__':
    unittest.main()


