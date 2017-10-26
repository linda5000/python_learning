import requests
from output import Output

class Config:
    def __init__(self,config):
        self.ip_config = config

# 从文件读取测试数据
    def load(self,file_name):
        list = []
        try:
            f = open(file_name,'r+',encoding='utf8')
        except IOError as e:
            print('文件读取失败：%s'%e)
        else:
            for line in f:
                list.append(line.replace('\n','').split(','))
            f.close()
        return list

# HTTP请求
class Http_requests:
    def __init__(self, ip_config):
        self.ip = ip_config

    def get(self,method,data):
        url = self.ip + method
        try:
            response = requests.get(url, data)
        except Exception as e:
            print(e)
        else:
            return response

    def post(self, method,data):
        url = self.ip + method
        try:
            response = requests.post(url, data)
        except Exception as e:
            print(e)
        else:
            return response




class Batch_http_test:
    def __init__(self,config):
        self.config = config


    def exec(self,input_file,output_file):
        request_list = Config(self.config).load(input_file)
        hr = Http_requests(self.config)
        context = []
        for i in request_list:
            params = {'mobilephone': i[1], 'amount': i[2]}

            if i[3] == 'GET':
                try:
                    response = hr.get(i[0], params)
                except Exception as e:
                    s = '请求异常：' + str(e)
                else:
                    s = response.text
            elif i[3] == 'POST':
                try:
                    response = hr.post(i[0], params)
                except Exception as e:
                    s = '请求异常：' + str(e)
                else:
                    s = response.text
            else:
                s = '请求异常：方法有误'
            print(s)
            context.append(s)
        Output().write_list(output_file,context)



# 配置参数
config = 'http://119.23.241.154:8080/'
input_file = 'request.txt'
output_file = 'result.txt'

Batch_http_test(config).exec(input_file,output_file)















