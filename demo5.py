# encoding: utf--8
import requests
from urllib import parse

url = "http://www.renren.com/Plogin.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ("
                  "KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 "
                  "Core/1.70.3650.400 QQBrowser/10.4.3341.400"
}
data = {
    "email": "18854889585",
    "password": "1234567890"
}
data = parse.urlencode(data)
session = requests.Session()
session.post(url, data=data.encode('utf-8'), headers=headers)
response = session.get("http://www.renren.com/259452569/profile")
with open('renren.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
