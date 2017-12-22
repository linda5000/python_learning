import requests

ip = "http://120.76.42.189:8765/"

url = ip + "futureloan/mvc/api/loan/add/"

data = {'memberId':100,'title':'aaa','amount':10000,'loanRate':18.0,'loanTerm':6,'loanDateType':0,'repaymemtWay':5,'biddingDays':10}

response = requests.get(url)
print(response.text)