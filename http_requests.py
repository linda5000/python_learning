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
            return response.text

    def post(self, url,data):
        url = self.ip + url
        try:
            response = requests.post(url, data)
        except Exception as e:
            log.error(e)
        else:
            return response.text