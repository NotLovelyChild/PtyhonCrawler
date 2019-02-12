import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib3
import random
agents = [
    {'http':'http://222.186.45.123:62222'},
    {'http':'http://110.40.13.5:80'},
    {'http':'http://118.190.95.35:9001'},
    {'http':'http://61.135.217.7:80'},
    {'http':'http://218.14.115.211:3128'},
    {'http':'http://119.4.173.88:8118'},
    {'http':'http://175.148.72.195:1133'},
    {'http':'http://222.221.11.119:3128'},
    {'http':'http://183.129.207.81:10800'},
    {'http':'http://222.186.45.154:60443'},
    {'http':'http://114.113.126.86:80'},
    {'http':'http://124.235.181.175:80'},
    {'http':'http://183.129.244.14:10080'},
    {'http':'http://121.69.37.6:9797'},
    {'http':'http://115.154.1.195:8118'},
    {'http':'http://182.88.188.22:8123'},
    {'http':'http://171.37.163.197:8123'},
    {'http':'http://117.85.222.118:8123'},
    {'http':'http://122.246.53.134:8010'},
    {'http':'http://110.86.15.46:58945'},
    {'http':'http://111.72.154.96:53128'},
    {'http':'http://175.155.24.11:808'},
    {'http':'http://119.5.0.41:808'},
    {'http':'http://117.66.166.202:8118'},
    {'http':'http://182.88.212.85:8123'},
    {'http':'http://36.33.25.184:808'},
    {'http':'http://221.220.67.246:8118'},
    {'http':'http://115.219.109.67:8010'},
    {'http':'http://182.88.255.165:8123'},
    {'http':'http://111.155.124.84:8123'},
    {'http':'http://60.191.57.78:10800'},
    {'http':'http://42.55.252.63:1133'},
    {'http':'http://116.238.157.234:9797'},
    {'http':'http://180.118.240.207:808'},
    {'http':'http://114.225.168.235:53128'},
    {'http':'http://221.226.68.194:30442'},
    {'http':'http://118.190.159.219:80'},
    {'http':'http://163.125.250.234:8118'},
    {'http':'http://163.125.250.228:8118'},
    {'http':'http://120.31.131.83:36885'},
    {'http':'http://14.152.101.5:44588'},
    {'http':'http://175.175.219.172:1133'},
    {'http':'http://182.88.135.33:8123'},
    {'http':'http://58.35.202.209:1080'},
    {'http':'http://112.115.57.20:3128'},
    {'http':'http://60.24.142.126:8118'},
    {'http':'http://221.232.195.2:8010'},
    {'http':'http://115.223.90.185:8010'},
    {'http':'http://219.157.147.115:8118'}
]
imgArray = []
proxies = [{'http': 'http://222.94.144.132:808'},
           {'http': 'http://222.186.45.57:62386'},
           {'http': 'http://61.178.238.122:63000'},
           {'http': 'http://202.199.159.130:40670'},
           {'http': 'http://182.88.160.148:8123'},
           {'http': 'http://58.251.229.235:9797'},
           {'http': 'http://210.72.14.142:80'},
           {'http': 'http://221.7.255.167:8080'},
           {'http': 'http://125.46.0.62:53281'},
           {'http': 'http://111.72.154.23:53128'},
           {'http': 'http://116.19.96.131:9797'}]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

def loadData(url):
    print('Loading......',url)
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    s = BeautifulSoup(driver.page_source, 'html.parser')
    for i in range(0,1000000000000):
        time.sleep(0.02)
        js = 'window.scrollTo(0,' + str(i*10) + ')'
        driver.execute_script(js)
        s = BeautifulSoup(driver.page_source, 'html.parser')
        isContinue = 0
        for title in s.select('.listpages'):
            if title.text == '已没有更多内容可显示':
                isContinue = 1
        if isContinue == 1:
            break

    imgs = s.select('.egeli_pic_dl')
    data = []
    for i in imgs:
        dd = i.select('dd')
        if len(dd) > 0:
            a = dd[0].select('a')
            if len(a) > 0:
                name = a[0].select('img')[0]['alt']
                href = a[0]['href']
                data.append({
                    'url':href,
                    'name':name
                })
    driver.quit()
    for d in data:
        getLists(d)

def getLists(data):
    print('Loading......',data['url'])
    requestManager = requests.get(data['url'], headers=headers, proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    requestManager.encoding = 'UFT-8'
    s = BeautifulSoup(requestManager.text, 'html.parser')
    lists = s.select('.swiper-slide')
    if len(lists) == 0:
        getImgHref({
            'name':data['name'],
            'href':data['url']
        })
    index = 1
    for i in lists:
        a = i.select('a')
        if len(a) > 0:
            href = 'https://www.enterdesk.com' + a[0]['href']
            print(href)
            getImgHref({
                'name':data['name'] + str(index),
                'href':href
            })
            index += 1

def getImgHref(href):
    requestManager = requests.get(href['href'], headers=headers, proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    requestManager.encoding = 'UFT-8'
    s = BeautifulSoup(requestManager.text, 'html.parser')
    d = s.select('#images_show_zoom')
    if len(d) > 0:
        a = d[0].select('a')
        if len(a) > 0:
            imgHtmlUrl = 'https:' + a[0]['href']
            img_u_url = getImgUrl(imgHtmlUrl)
            style = '.' + img_u_url.split('.')[-1]
            data = {
                'name':href['name'],
                'url':img_u_url,
                'style':style
            }
            print(data)
            download(data)

def getImgUrl(imgHtmlUrl):
    requestManager = requests.get(imgHtmlUrl, headers=headers, proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    requestManager.encoding = 'UFT-8'
    s = BeautifulSoup(requestManager.text, 'html.parser')
    img = s.select('#down_main_pic')
    if len(img) > 0:
        url = img[0]['src']
        return url
    else:
        return ''


def download(data):
    print('start download',data['name'])
    mp3response = requests.get(data['url'], stream=True, proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    image = mp3response.content
    address = "/Users/zh/Desktop/photos" + "/"
    try:
        with open(address +data['name'] + data['style'], "wb") as f:
            f.write(image)
            print ('download ok',[data['name']])
    except IOError:
        print("IO Error\n")
    finally:
        f.close
    imgArray.append(data)


if __name__ == '__main__':
    urllib3.disable_warnings()
    print('回车桌面')
    print('请输入关键词')
    key = input()
    loadData('https://www.enterdesk.com/search/1-0-6-0-0-0/' + key)
    print(imgArray)
    print('共',len(imgArray),'张')