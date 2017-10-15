import unittest
import json
from http_requests import Http_requests
from mylog import Log

class TestHttp(unittest.TestCase):



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
        self.assertEqual(result,"10001")




if __name__ == '__main__':
    unittest.main()


