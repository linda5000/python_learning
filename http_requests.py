import requests
from mylog import Log

log = Log('Http_requests')

class Http_requests:
    def __init__(self, ip):
        self.ip = ip

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