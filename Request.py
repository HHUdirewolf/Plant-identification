import urllib.request
import base64

import json
#方法
def BaiduAPI(url):
    #构造request对象
    request_url="https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
    access_token="24.61871ea8225d70a2623db95f8d1bd5d9.2592000.1622468713.282335-24100977"
    request_url=request_url+"?access_token="+access_token

    f=open(url,'rb')
    img=base64.b64encode(f.read())


    params={"image":img}
    params=urllib.parse.urlencode(params).encode('utf-8')

    request=urllib.request.Request(url=request_url,data=params)
    request.add_header('Content-Type','application/x-www-form-urlencoded')

    response=urllib.request.urlopen(request)

    #输出响应内容
    if response:
        data=json.loads(response.read())
        #字典嵌套元组，元组嵌套字典
        name=data['result'][0]['name']
        return name
                    
    


