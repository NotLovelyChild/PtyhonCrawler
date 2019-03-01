import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pathlib
import urllib3
import http
import selenium
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:64.0) Gecko/20100101 Firefox/64.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60Opera/8.0 (Windows NT 5.1; U; en)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'

}


def getHTTP():
    data = []
    try:
        with open('/Users/zh/Desktop/http.json', 'r') as file_obj:
            data = json.load(file_obj)
    except IOError:
        print('IO error')

    return data

def getHTTPS():
    data = []
    try:
        with open('/Users/zh/Desktop/https.json', 'r') as file_obj:
            data = json.load(file_obj)
    except IOError:
        print('IO error')

    return data

def requestUrl(url):
    while True:
        try:
            httpPorxies=getHTTP()
            h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]
            print('当前使用代理为', h, '访问地址为', url)
            requests.packages.urllib3.disable_warnings()
            requestManager = requests.get(url, headers=headers, verify=False, proxies=h)
            requestManager.encoding = None
            return BeautifulSoup(requestManager.text, 'html.parser')
        except requests.exceptions.ConnectionError:
            print('Connection Error try retry')
            continue

def requestUrlWithChrome(url):
    while True:
        try:
            print('Chrome 访问地址为', url)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            return soup
        except selenium.common.exceptions.TimeoutException:
            print('Connection Error try retry')
            continue

def download(data):
    fileName = data['name'] + '.' + data['url'].split('.')[-1]
    print('To prepare download',fileName)
    print('Check if the file exists')

    address = "/Users/zh/Pictures/R" + "/" + fileName
    path = pathlib.Path(address)
    if path.is_file():
        print('The current file already exists')
        return
    else:
        print('The current file does not exist\n Start download ',fileName)

    try:
        httpPorxies = getHTTP()
        h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]
        print('当前使用代理为', h)
        imgresponse = requests.get(data['url'], stream=True, proxies=h)
        image = imgresponse.content
        try:
            with open(address, "wb") as jpg:
                jpg.write(image)
                print ('download ok',fileName)
        except IOError:
            print("IO Error\n")
            pass
        except UnboundLocalError:
            print('UnboundLocalError')
            pass
        finally:
            jpg.close
    except requests.exceptions.ChunkedEncodingError:
        print('requests.exceptions.ChunkedEncodingError')
        pass
    except requests.exceptions.ChunkedEncodingError:
        print('ChunkedEncodingError -- please wait 3 seconds')
        pass
    except urllib3.exceptions.ProtocolError:
        print('urllib3.exceptions.ProtocolError')
        pass
    except http.client.IncompleteRead:
        print('http.client.IncompleteRead')
        pass
    except selenium.common.exceptions.TimeoutException:
        print('selenium.common.exceptions.TimeoutException')
    finally:
        pass

# xhamster
# 图片
def getXhamsterPictures():
    for i in range(1,46000):
        soup=requestUrl('https://xhamster.com/photos/'+str(i))
        picture_list=soup.select('.gallery-thumb__link.thumb-image-container')
        for picture in picture_list:
            img=picture['href']
            soup=requestUrl(img)
            picture_list=soup.select('.photo-container.photo-thumb')
            for picture in picture_list:
                img = picture['href']
                soup=requestUrlWithChrome(img)
                img_name=img.split('/')[-2]+'_'+img.split('/')[-1]
                img_div=soup.select('.fotorama__stage__frame.fotorama__loaded.fotorama__loaded--img.fotorama__active')
                if len(img_div):
                    img_div=img_div[0].select('img')
                    if len(img_div):
                        img_url=img_div[0]['src']
                        download({
                            'name':img_name,
                            'url':img_url
                        })


if __name__ == '__main__':
    # soup=requestUrlWithChrome('https://xhamster.com/videos/schoolgirl-besties-fucking-and-blowjob-in-facial-3way-11003138')
    # video_div = soup.select('.player-container__no-player.xplayer.xplayer-fallback-image.xh-helper-hidden')
    # if len(video_div):
    #     href = video_div[0]['href']
    #     video_url = href.replace(';','&')
    #     print(video_url)
    #     download({
    #         'name':'123',
    #         'style':'.mp4',
    #         'url':video_url
    #     })
    getXhamsterPictures()