import asyncio
import json
from aiowebsocket.converses import AioWebSocket
from gettoken import get_token

def manage_danmu(message):
    content = message['msg']['msg']
    if content.get('content'):
        print(content['user']['username'] + ':' + content['content'])
    elif content.get('userMessage'):
        print(content['user']['username'] + ':' + content['userMessage'])
    elif content.get('title'):
        if content.get('user'):
            print(content['user']['username'] + '送了:' + content['title'])
        else:
            print(content['sourceUserName'] + '送了:' + content['title'])
    elif content.get('name'):
        print(content['user']['username'] + '送了:' + content['name'])
    else:
        print(content)
        print('*' * 10)

async def startup(uri,f):
    async  with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        n = 0
        while True:
            mes = await converse.receive()
            mes = mes.decode()
            # print(mes)
            f.write(mes+'\n')
            mes_json = json.loads(mes)
            manage_danmu(mes_json)
            n += 1
            if n == 3:
                mid = mes_json['msgId']
                await converse.send('{"body":{"msgId":"%s"},"op":6,"sid":0,"seq":0} 	' % mid)
                n = 0
            else:
                await converse.send('{"body":"{}","op":2,"sid":0,"seq":0}	')
                

if __name__ == '__main__':
    url = 'http://star.longzhu.com/sk2?from=filivehot5'
    appid,roomid,token = get_token(url)
    remote = f'ws://ws52.longzhu.com:8805/?appId={appid}&roomId={roomid}&msgVersion=1.0&token={token}'
    with open('data.txt','w',encoding='utf-8')as f:
        try:
            asyncio.get_event_loop().run_until_complete(startup(remote,f))
        except KeyboardInterrupt as exc:
            print(exc)















