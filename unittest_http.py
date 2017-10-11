import unittest
from http_requests import Http_requests

class TestHttp(unittest.TestCase):

    def test_http_get(self):
        ip = 'http://119.23.241.154:8080/'
        url = '/futureloan/mvc/api/member/recharge'
        data = {'mobilephone':'13667692121','amount':1000}
        r = Http_requests(ip)
        result = r.get(url,data)
        try:
            self.assertEqual(result,"10001")
        except AssertionError as e:
            pass

    def test_http_post(self):
        ip = 'http://119.23.241.154:8080/'
        url = '/futureloan/mvc/api/member/register'
        data = {'mobilephone':'13667692121','pwd':'987654321'}
        r = Http_requests(ip)
        result = r.post(url,data)
        self.assertEqual(result,"10001")

if __name__ == '__main__':
    unittest.main()


