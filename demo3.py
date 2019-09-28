#encoding:utf-8

import requests
#在requests中添加代理，向请求方法传递proxies参数
proxy = {
    'http':"111.77.197.147:9999"
}
response = requests.get("http://httpbin.org/ip",proxies = proxy)
print(response.text)