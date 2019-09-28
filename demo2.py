#encoding: utf-8
import time
import json
import requests

start_url = "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC"
url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400',
}
data = {
    'first': 'true',
    'pn':'1',
    'kd': 'python'
}
s = requests.Session()
s.get(start_url, headers=headers, timeout=3)  # 请求首页获取cookies
cookie = s.cookies  # 为此次获取的cookies
response = requests.post(url=url,headers=headers,data=data,cookies=cookie, timeout=3)
print(type(response.json()))
print(response.json())
print(response.text)