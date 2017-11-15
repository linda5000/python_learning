import requests
from public.config import Config
from public.log import Log

log = Log("HttpRequest")

class HttpRequest:
    def __init__(self):
        self.ip = Config().getConfig("server","host")

    def get(self,url,params=None,timeout=0.001):
        url = self.ip + url
        try:
            response = requests.get(url, params)
        except Exception as e:
            raise e
            log.error(e)
        else:
            return response.json()

    def post(self, url,params=None,timeout=0.001):
        url = self.ip + url
        try:
            response = requests.post(url, params)
        except Exception as e:
            raise e
            log.error(e)
        else:
            return response.json()


def main():
    url = '/futureloan/mvc/api/member/recharge'
    data = {'mobilephone':'13667692121','amount':1000}
    result = HttpRequest().get(url,data)
    for i in result:
        print(i,':',result[i])

if __name__ == '__main__':
    main()