import requests
from config import Config
from mylog import Log

log = Log('Http_requests')


class Http_requests:
    def __init__(self):
        self.ip = Config().getConfig("server","address")

    def get(self,url,data):
        url = self.ip + url
        try:
            response = requests.get(url, data)
        except Exception as e:
            log.error(e)
        else:
            return response.json()

    def post(self, url,data):
        url = self.ip + url
        try:
            response = requests.post(url, data)
        except Exception as e:
            log.error(e)
        else:
            return response.json()


def main():
    url = '/futureloan/mvc/api/member/recharge'
    data = {'mobilephone':'13667692121','amount':1000}
    result = Http_requests().get(url,data)
    for i in result:
        print(i,':',result[i])

if __name__ == '__main__':
    main()