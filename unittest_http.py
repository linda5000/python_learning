import unittest
import json
from http_requests import Http_requests

class TestHttp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('set up class ran')

    def test_http_get(self):
        ip = 'http://119.23.241.154:8080/'
        url = '/futureloan/mvc/api/member/recharge'
        data = {'mobilephone':'13667692121','amount':1000}
        r = Http_requests(ip)
        response = r.get(url,data)
        result =  json.loads(response)['code']
        self.assertEqual(result,"10001","The result is False")


    def test_http_post(self):
        ip = 'http://119.23.241.154:8080/'
        url = '/futureloan/mvc/api/member/register'
        data = {'mobilephone':'13667692122','pwd':'987654321'}
        r = Http_requests(ip)
        response = r.post(url,data)
        result = json.loads(response)['code']
        self.assertEqual(result,"10001","The result is False")

    @classmethod
    def tearDownClass(cls):
        print('tear down class ran')


if __name__ == '__main__':
    unittest.main()


