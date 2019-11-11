import requests
import re
import json

def get_token(url0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    
    html = requests.get(url=url0,headers=headers).content.decode()
    roominfo = re.findall('var roomInfo = (.*?);',html,re.S)[0]
    roodid = json.loads(roominfo)['RoomId']
    
    url = f'http://mbgo.longzhu.com/zhongtai/checkRoom?roomid={roodid}&wangsu=1&lzv=1'
    headers['Referer'] = url0
    request_data = json.loads(requests.get(url=url,headers=headers).content.decode())['data']
    token = request_data['zhongtaiToken']
    appId = request_data['appId']
    # print(appId,roodid,token)
    return appId,roodid,token

if __name__ == '__main__':

    url0 = 'http://star.longzhu.com/m172502?from=filivehot2'
    get_token(url0)
