#encoding:utf-8

import requests
#从响应中的cookies属性获取cookie值,get_dict()以字典形式返回cookie
response = requests.get("https://www.baidu.com")
print(response.cookies)
print(response.cookies.get_dict())