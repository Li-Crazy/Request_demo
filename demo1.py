import requests

response = requests.get("https://www.baidu.com")
print(type(response.text))
print(response.text)#查看响应内容
print(type(response.content))
print(response.content.decode('utf-8'))#查看响应内容

print(response.url)#查看网址
print(response.encoding)#查看网页字符编码
print(response.status_code)#查看状态响应码

params = {
    "wd":"中国"
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400"
}
response = requests.get("https://www.baidu.com/s",params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))

print(response.url)
