import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from contextlib import closing
import json
import pathlib
import urllib3
import http
import selenium
import random
import time
import HttpProxy

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
    
timeoutNums=0

def requestUrl(url):
    global timeoutNums
    while True:
        try:
            httpPorxies=getHTTPS()
            h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]
            print('The proxies = ', h, 'The url = ', url)
            requests.packages.urllib3.disable_warnings()
            requestManager = requests.get(url, headers=headers, verify=False, proxies=h, timeout=4)
            requestManager.encoding = None
            return BeautifulSoup(requestManager.text, 'html.parser')
        except requests.exceptions.ConnectionError:
            print('Connection Error try retry')
            timeoutNums=timeoutNums+1
            print('timeoutNums = ',timeoutNums)
            if timeoutNums == 1000:
              HttpProxy.loadHTTPS()
              timeoutNums=0
            continue
        except requests.exceptions.ConnectTimeout:
            print('ConnectTimeout Error try retry')
            timeoutNums=timeoutNums+1
            print('timeoutNums = ',timeoutNums)
            if timeoutNums == 1000:
              HttpProxy.loadHTTPS()
              timeoutNums=0
            continue
        except requests.exceptions.ReadTimeout:
            print('ReadTimeout Error try retry')
            timeoutNums=timeoutNums+1
            print('timeoutNums = ',timeoutNums)
            if timeoutNums == 1000:
              HttpProxy.loadHTTPS()
              timeoutNums=0
            continue

def requestUrlWithChrome(url):
    while True:
        try:
            print('Chrome request url = ', url)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()
            return soup
        except selenium.common.exceptions.TimeoutException:
            driver.quit()
            print('Connection Error try retry')
            continue

def download(data):
    if int(time.time()%3600) == 0 or int(time.time()%3600) == 0.3 or int(time.time()%3600) == 0.6 :
      HttpProxy.loadHTTPS()
    print(data['url'])
    fileName=''
    if data['type'] == 'img':
        fileName = data['name'] + '.' + data['url'].split('.')[-1]
    elif data['type'] == 'xhamsterVideo':
        fileName=data['name']+'.mp4'
    print('To prepare download\n',fileName)
    print('Check if the file exists')

    address = "/Volumes/J/Nice" + "/" + fileName
    path = pathlib.Path(address)
    if path.is_file():
        print('The current file already exists')
        return
    else:
        print('The current file does not exist\n Start download ',fileName)

    try:
        httpPorxies = getHTTPS()
        h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]
        print('The Downloading proxies = ', h)
#        with closing(requests.get(data['url'],headers=headers,stream=True)) as response:
        with closing(requests.get(data['url'],headers=headers,stream=True, proxies=h)) as response:
          chunk_size = 1024  # 单次请求最大值
          try:
             content_size = int(response.headers['content-length'])  # 内容体总大小
          except KeyError:
            print("KeyError\n")
            pass
          
          data_count = 0
          try:
            with open(address, "wb") as file:
              for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r Downloading progress ：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, fileName), end=" ")
          except IOError:
              print("IO Error\n")
              pass
          except UnboundLocalError:
              print('UnboundLocalError')
              pass
          finally:
              print('\nDownload OK!!!!!!!!!!!!!!!!')
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
    except requests.exceptions.ConnectionError:
        print('requests.exceptions.ConnectionError')
    finally:
        pass

# xhamster
# 图片
def getXhamsterPictures():
    for i in range(1,46000):
        soup=requestUrl('https://xhamster.com/photos/categories/cartoon/'+str(i))
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
                            'url':img_url,
                            'type':'img'
                        })

#视频
def getXhamsterVideos():
    data_arr=[]
    for i in range(1,10):
        url='https://xhamster.com/best/'+str(i)
        soup=requestUrlWithChrome(url)
        videos_list=soup.select('.thumb-list__item.video-thumb')
        for video in videos_list:
            name_info=video.select('.video-thumb-info__name')
            video_info=video.select('.video-thumb__image-container.thumb-image-container')
            if len(name_info) and len(video_info):
                name=name_info[0].text
                video_url=video_info[0]['href']
                print(name,video_url)

                soup = requestUrl(video_url)
                video_div = soup.select('.player-container__no-player.xplayer.xplayer-fallback-image.xh-helper-hidden')
                if len(video_div):
                    href = video_div[0]['href']
                    video_url = href.replace(';', '&')
                    print(name)
                    print(video_url)
                    download({
                        'name': name,
                        'url': video_url,
                        'type': 'xhamsterVideo'
                    })
                data_arr.append({
                    'video_name':name,
                    'video_url':video_url
                })

    print('视频个数',len(data_arr))

def downBookMp3():
    i=1
    while True:
        num=str(i)
        if len(str(i))==1:
            num='00'+str(i)
        if len(str(i))==2:
            num='0'+str(i)
        url='http://mp3-2e.ting89.com:9090/2017/32/武神至尊/'+num+'.mp3'
        print(url)
        download({
            "url":url,
            "type":"img",
            "name":"武神至尊"+num
        })
        i+=1
        if i==266:
            break

def getEImg():
  mainUrl = 'https://e-hentai.org/'
  soup=requestUrlWithChrome(mainUrl)
  gl3c=soup.select('.gl3c.glname')
  for g in gl3c:
    a=g.select('a')
    if len(a):
      href=a[0]['href']
      title=a[0].text
      getEGroup(title,href)
      print(title,'\n',href)



def getEPage(soup):
  page=0
  pages=soup.select('.ptt')
  if len(pages):
    tds=pages[0].select('td')
    for t in tds:
      try:
        page=int(t.text)
      except ValueError:
        continue
    print('----------Has ',page,' pages.---------------')
  return page


def getEImgs(soup):
  urls=[]
  img_div=soup.select('.gdtm')
  for img in img_div:
    a=img.select('a')
    if len(a):
      href=a[0]['href']
      urls.append(href)
      print(href)
  return urls

def getEGroup(title,url):
  soup=requestUrlWithChrome(url)
  page=getEPage(soup)
  u=getEImgs(soup)
  if page > 1:
    for i in range(1,page):
      soup=requestUrlWithChrome(url+'?p='+str(i))
      u+=getEImgs(soup)
  print(len(u))
  i=1
  for i_u in u:
    getEImage(title+str(i),i_u)
    i+=1

def getEImage(title,url):
  soup=requestUrlWithChrome(url)
  img_div=soup.select('#img')
  if len(img_div):
    href=img_div[0]['src']
    download({
             'name':title,
             'url':href,
             'type':'img'
             })

#二次萌
def getTList():  
  i=1
  try:
    with open('TPage.json', 'r') as file_obj:
      data = json.load(file_obj)
      i=data["page"]
  except IOError:
    print('IO error')
  while True: 
    i+=1
    soup=requestUrl('http://moeimg.net/'+str(i)+'.html')
    title=''
    if len(soup.title.text.split('|')):
      title=soup.title.text.split('|')[0]
    imgs=soup.select('.thumbnail_image')
    for img in imgs:
      name=title+img['alt']
      src=img['src']
      download({
           'name':name,
           'url':src,
           'type':'img'
           })
      time.sleep(0.1)
    with open('TPage.json', 'w') as file_obj:
      json.dump({"page":i}, file_obj)
      print("写入TPage到文件：")

if __name__ == '__main__':

#     getXhamsterPictures()
#     getXhamsterVideos()
    # getKImg()
#    downBookMp3()
#  getEImg()
  getTList()
