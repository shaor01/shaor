import gettoken
import base64
import json
import requests
import os

heade={'Content-Type':'application/json'}
photodata={
'dataset_id':'99436',
'type':'SKU_DETECTION'


}
floder="d:/"

#图片编码base64
def phototobase64(path):
    with open(path,'rb') as f:
        ph=base64.b64encode(f.read()).decode('utf-8')
        return ph

#遍历图片路径
def getphoto():
    filepath=os.listdir(floder)
    for file in filepath:
        print (floder+file)
if __name__=="__main__":
    getphoto()