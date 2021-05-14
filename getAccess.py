#获取access_key
import urllib.request
API_key="yours"#输入你的api_key
SECRET_KEY="yours"
host="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+API_key+"&client_secret="+SECRET_KEY
request=urllib.request.Request(host)
request.add_header('Content-Type','application/json;charset=utf-8')
response=urllib.request.urlopen(request)
print(response.read())
