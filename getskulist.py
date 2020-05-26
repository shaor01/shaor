import gettoken
import requests
import json
header={'Content-Type':'application/json'}
token=gettoken.gettoken()
def get_sku_list():
    pam={'start':1,'num':100}
    skulisturl='https://aip.baidubce.com/rpc/2.0/easydl/retail/sku/list?access_token='+token
    return skulisturl,pam
def get_shijing_list():
    pam={'start':1,'num':100,'type':'SKU_DETECTION'}
    shijinglisturl='https://aip.baidubce.com/rpc/2.0/easydl/retail/dataset/list?access_token='+token
    return shijinglisturl,pam
def get_res(url,pam):
    res=requests.post(url=url,headers=header,json=pam) 
    return json.loads(res.text)
    
if __name__=="__main__":
    uu1,uu2=get_shijing_list()
    tt=get_res(uu1,uu2)
    print(tt)

   