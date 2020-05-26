# coding=utf-8

import sys
import json
import base64
import requests


# 保证兼容python2以及python3

# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 百度云控制台获取到ak，sk以及
# EasyDL官网获取到URL

# ak
API_KEY = '8fDpGzXIkeRbdgNnG6hSjVIE'

# sk
SECRET_KEY = 'g6fGEFAT2H6V270aGe3DCMlGVPndIdq1'

"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
# post_data = urlencode(params)
# post_data = post_data.encode('utf-8')
def gettoken():
    result= requests.post(TOKEN_URL, params)
    # try:
    #     f = urlopen(req, timeout=5)
    #     result_str = f.read()
    # except URLError as err:
    #     print(err)

    # result_str = result_str.decode()
    result.encoding='utf-8'
    result=result.text
    result = json.loads(result)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

    """
        读取文件
    """
if __name__=='__main__':
    tt=gettoken()
    print (tt)



