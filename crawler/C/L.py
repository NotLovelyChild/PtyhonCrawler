import requests
from bs4 import BeautifulSoup
import time

dataArr = []

proxies = [{'https': 'https://183.129.207.73:14823'}]

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
pro = {'https': 'https://124.205.143.212:38768'}

def requestUrl(url):
    requestManager = requests.get(url, headers=headers,proxies=proxies[-1], verify=False)
    requestManager.encoding = 'GB2312'
    return BeautifulSoup(requestManager.text, 'html.parser')

def loadList( url ):
    soup = requestUrl(url)
    imgs = soup.select('.list')[0].select('li')
    for img in imgs:
        if len(img.select('div')) <= 0:
            href = 'http://www.netbian.com' + img.select('a')[0]['href']
            title = img.select('a')[0]['title']
            d = {'url': href,
                 'title': title}
            dataArr.append(d)
    return dataArr

def loadAllList():
    i = 1
    while 1:
        i += 1
        print('loading page = ' + str(i))
        url = 'http://www.netbian.com/chaogaoqingdongman/index_' + str(i) + '.htm'
        lists = loadList(url)
        time.sleep(3)
        if len(lists) > 0 and i < 100:
            dataArr + lists
        else:
            break

def getBigImgUrl(data):
    s = requestUrl(data['url'])
    a = s.select('.pic-down')
    if len(a) <= 0:
        return
    if len(a[0].select('a')) > 0:
        bigHtmlUrl = 'http://www.netbian.com' + (a[0].select('a')[0]['href'])
        img = requestUrl(bigHtmlUrl)
        if len(img.select('#endimg')) > 0:
            u = img.select('#endimg')[0].select('a')[0]['href']
            name = img.select('#endimg')[0].select('a')[0]['title']
            print(name, u)
            downloadImg(name=name, url=u)


def downloadImg(name,url):
    print('download start')
    imgresponse = requests.get(url, stream=True, proxies=proxies[-1])
    image = imgresponse.content
    address = "/Users/zh/Desktop/pictures" + "/"
    try:
        with open(address + name + ".jpg", "wb") as jpg:
            jpg.write(image)
            print ('download ok',name)
    except IOError:
        print("IO Error\n")
    finally:
        jpg.close





if __name__ == '__main__':
    loadAllList()
    for data in dataArr:
        time.sleep(3)
        getBigImgUrl(data)