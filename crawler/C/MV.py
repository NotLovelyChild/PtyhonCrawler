import json
import requests
import random

def getHTTP():
    data = []
    try:
        with open('/Users/jackmacbook/Desktop/http.json', 'r') as file_obj:
            data = json.load(file_obj)
    except IOError:
        print('IO error')

    return data

def getHTTPS():
    data = []
    try:
        with open('/Users/jackmacbook/Desktop/https.json', 'r') as file_obj:
            data = json.load(file_obj)
    except IOError:
        print('IO error')

    return data

httpPorxies=getHTTPS()
h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]

def setName(name):
    types=['netease','qq','kugou','kuwo','xiami','baidu','1ting','lizhi','qingting','ximalaya','migu','5singyc','5singfc']
    url='http://music.51yfx.com/api.php'
#    header={
#        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
#        'Accept-Encoding': 'gzip, deflate',
#        'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8',
#        'Connection': 'keep-alive',
#        'Content-Length': '68',
#        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#        'Cookie': 'UM_distinctid=1692d1d01ee69-05afc032791889-1e396652-2a3000-1692d1d02005c; CNZZDATA1260597857=822799366-1551236251-%7C1551236251; CNZZDATA1276373677=638117520-1551758257-%7C1553139149',
#        'Host': 'music.51yfx.com',
#        'Origin': 'http://music.51yfx.com',
#        'Referer': 'http://music.51yfx.com/',
#        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
#        'X-Requested-With': 'XMLHttpRequest',
#    }
    params={
        'types': 'search',
        'count': '10',
        'filter': 'name',
        'source': 'qq',
        'pages': '1',
        'name': name,
    }
    
    req=requests.post(url,data=params, proxies=h)
    print(req.text)
#    items=json.loads(req.text)
#    for item in items:
#        print(item['source'])
#        print(item['title'])
#        print(item['author'])
#        print(item['url'])


class Music:
    def __init__(self):
        name=None
if __name__ == '__main__':
    setName('周杰伦')
