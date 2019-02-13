import requests
from bs4 import BeautifulSoup
import time
import urllib3
import http
import pathlib
import random
import socket
from selenium import webdriver
import json
import HttpProxy
import selenium
import threading


httpPorxies = HttpProxy.getHTTP()
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

def requestUrl(url):
    while True:
        try:
            h = httpPorxies[random.randint(0,len(httpPorxies) - 1)]
            print('当前使用代理为',h,'访问地址为',url)
            requests.packages.urllib3.disable_warnings()
            requestManager = requests.get(url, headers=headers,proxies=h, verify=False)
            requestManager.encoding = None
            return BeautifulSoup(requestManager.text, 'html.parser')
        except requests.exceptions.ConnectionError:
            print('Connection Error try retry')
            continue

def requestUrlWithChrome(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup

#美剧天堂
meijutt_main_url='https://www.meijutt.com'
def meijutt():
    dataArr = {}
    try:
        with open('/Users/zh/Desktop/VideoJson/' + 'index' + '.json', 'r') as file_obj:
            dataArr = json.load(file_obj)
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print("IO Error!!")
    for i in range(1,100000):
        url = 'https://www.meijutt.com/content/meiju' + str(i) + '.html'
        print('Loading url = ',url)
        data = meijutt_detail(url,i)
        if len(data['info']):
            video_id = i
            dataArr[str(i)] = {
                'video_id':video_id,
                'video_info':data['info'],
                'video_data':data['video_data'],
                'baidu_data':data['baidu_data'],
                'video_name':data['name'],
                'video_desc':data['desc'],
                'video_img':data['video_img']
            }
            with open('/Users/zh/Desktop/VideoJson/' + 'index' + '.json', 'w') as file_obj:
                json.dump(dataArr, file_obj)
                print("写入json文件：")
        else:
            print('id = ',i,'unknow')

def meijutt_detail(url,videoId):
    dataArr = {}
    try:
        with open('/Users/zh/Desktop/VideoJson/' + 'index' + '.json', 'r') as file_obj:
            dataArr = json.load(file_obj)
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print("IO Error!!")


    video_data = []
    soup = requestUrl(url)

    name = ''
    if len(soup.select('.info-title')):
        name = soup.select('.info-title')[0].text
        print(name)

    o_big_img_bg_b = ''
    if len(soup.select('.o_big_img_bg_b')):
        if len(soup.select('.o_big_img_bg_b')[0].select('img')):
            o_big_img_bg_b = soup.select('.o_big_img_bg_b')[0].select('img')[0]['src']


    names = []
    #检查本地
    try:
        video_data = dataArr[str(videoId)]['video_data']
        for vd in video_data:
            names.append(vd['title'])
    except KeyError:
        print('KeyError')
    # for da in dataArr:
    #     if da['video_name'] == name:
    #         video_data = da['video_data']
    #         for vd in video_data:
    #             names.append(vd['title'])

    info = []
    c = soup.select('.o_r_contact')
    if len(c):
        li = c[0].select('li')
        for l in li:
            print(l.text)
            info.append(l.text)

    des = ''
    if len(soup.select('.des')):
        des = soup.select('.des')[0].text
        print(des)

    list = soup.select('.mn_list_li_movie')
    if len(list):
        infos = list[-1].select('a')
        for a in infos:
            href = meijutt_main_url + a['href']
            title = a['title']
            if title in names:
                print(title,'本集已存在')
                continue
            video_url = meijutt_video_url(href)
            print(href,title,video_url)
            video_data.append({
                'href':href,
                'title':title,
                'video_url':video_url
            })

    baidu_data = []
    baidu_list = soup.select('.wp-list')
    if len(baidu_list):
        li = baidu_list[0].select('li')
        for l in li:
            d = {}
            strong = l.select('strong')
            span = l.select('span')
            a = l.select('a')
            if len(strong):
                baidu_title = strong[0].text
                d['baidu_title'] = baidu_title
            if len(span):
                baudi_password = span[0].text.split('：')[-1]
                d['baudi_password'] = baudi_password
            if len(a):
                baudi_url = a[0]['href']
                d['baudi_url'] = baudi_url
            print(d)
            baidu_data.append(d)

    return {'video_data':video_data,'baidu_data':baidu_data,'info':info,'name':name,'desc':des,'video_img':o_big_img_bg_b}

def meijutt_video_url(url):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        try:
            driver.switch_to.frame("player-frame")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            iframe = soup.select('iframe')
            if len(iframe):
                src = iframe[0]['src']
                driver.quit()
                return src
        except selenium.common.exceptions.NoSuchFrameException:
            driver.quit()
            return '数据丢失'
        driver.quit()
        return '数据丢失'
    except selenium.common.exceptions.TimeoutException:
        print('time out')

video_main_url = 'https://www.ahu.cc'
# 电影
def getMoive():
    jsonData = {}

    try:
        with open('/Users/zh/Desktop/VideoJson/' + 'movie' + '.json', 'r') as file_obj:
            jsonData = json.load(file_obj)
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print("IO Error!!")

    for i in range(1,1000000):
        isshow = True
        try:
            ios = jsonData[str(i)]
            print('当前id已经存在')
        except KeyError:
            isshow = False

        if isshow:
            continue

        data = {}
        data['video_id']=i
        url = 'https://www.ahu.cc/vod/'+ str(i) + '/'
        soup = requestUrl(url)
        vod_l = soup.select('.vod_l')
        info_arr = []
        if len(vod_l):
            vod = vod_l[0]
            #名字
            title_w = vod.select('.title.w')
            if len(title_w):
                name = title_w[0].text
                print(name)
                data['video_name'] = name
            # 图片地址
            pic = vod.select('.pic')
            if len(pic):
                img = pic[0].select('img')
                if len(img):
                    img_src = img[0]['data-original']
                    print(img_src)
                    data['video_img'] = img_src

            # 信息
            w_space = vod.select('.w.space')
            if len(w_space):
                info_arr.append(w_space[0].text)

            ws = vod.select('.w')
            for w in ws:
                info_arr.append(w.text)

            up = vod.select('.up')
            if len(up):
                info_arr.append(up[0].text)

        print(info_arr)

        play_list = soup.select('.playlist.wbox')
        video_data = []
        for play in play_list:
            list_a = play.select('a')
            for a in list_a:
                href = video_main_url + a['href']
                title = a.text
                video_url = getVideoUrl(href)
                if video_url != 'unknow':
                    video_data.append({
                        'title':title,
                        'video_url':video_url
                    })
                    data['video_data'] = video_data
                    data['video_info'] = info_arr
                    print(title,href,video_url)
                    jsonData[str(i)] = data
                    with open('/Users/zh/Desktop/VideoJson/' + 'movie' + '.json', 'w') as file_obj:
                        json.dump(jsonData, file_obj)
                        print("写入json文件：")

def getVideoUrl(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        iframes = soup.select('iframe')
        for i in iframes:
            try:
                video_url = i['src']
                if '/share/' in video_url:
                    print(video_url)
                    return video_url
            except IOError:
                print('IO error')
    except selenium.common.exceptions.TimeoutException:
        print('time out')
    driver.quit()
    return 'unknow'

#6V电影
def get6v():
    soup=requestUrl('https://www.66s.cc')
    items=soup.select('.menu-item ')
    dataArr={}
    key=1
    urls=[]
    for item in items:
        if len(item.select('a')):
            href=item.select('a')[0]['href']
            if '66s' in href:
                urls.append(href)

    for url in urls:
        index = 1
        while 1:
            address = url
            if index != 1:
                address=url+'index_'+str(index)+'.html'
            index+=1
            soup = requestUrl(address)
            zooms = soup.select('.zoom')
            if len(zooms):
                print(address)
                for z in zooms:
                    data = {}
                    data['video_id']=key
                    data['href'] = z['href']
                    data['video_name']=z['title']
                    if len(z.select('img')):
                        img = z.select('img')[0]
                        data['video_img'] = img['src']
                    detail=get6vDetail(z['href'])
                    data['video_data'] = detail['video_data']
                    data['baidu_data'] = detail['baidu_data']
                    data['video_info'] = detail['video_info']
                    print(data)
                    dataArr[str(key)] = data
                    with open('/Users/zh/Desktop/VideoJson/' + '6v' + '.json', 'w') as file_obj:
                        json.dump(dataArr, file_obj)
                        print("写入json文件：")
                        key+=1
            else:break

def get6vDetail(url):
    if 'www.66s.cc' not in url:
        url = 'https://www.66s.cc' + url
    soup=requestUrl(url)
    tbody=soup.select('tbody')
    baidu_data=[]
    if len(tbody):
        for body in tbody:
            for a in body.select('a'):
                baidu_title=a.text
                baudi_url=a['href']
                baidu_data.append({
                    'baidu_title':baidu_title,
                    'baudi_url':baudi_url
                })

    content=soup.select('#post_content')
    video_info=[]
    if len(content):
        video_info=content[0].text.split('\n')

    lBtn=soup.select('.lBtn')
    video_url_arr=[]
    for l in lBtn:
        href = l['href']
        if 'www.66s.cc' not in href:
            href = 'https://www.66s.cc' + href
        soup=requestUrl(href)
        iframe=soup.select('iframe')
        if len(iframe):
            video_url=iframe[0]['src']
            video_url_arr.append({
                'video_url':video_url,
                'title':l['title']
            })
        else:
            soup=requestUrlWithChrome(href)
            video = soup.select('#ckplayer_a1')
            if len(video):
                sources = video[0].select('source')
                for source in sources:
                    video_url = source['src']
                    title = source['type']
                    video_url_arr.append({
                        'video_url': video_url,
                        'title': title
                    })
    return {
        'video_data':video_url_arr,
        'baidu_data':baidu_data,
        'video_info':video_info
    }



if __name__ == '__main__':
    # threads = []
    # threads.append(threading.Thread(target=meijutt))
    # threads.append(threading.Thread(target=getMoive))
    # threads.append(threading.Thread(target=get6v()))
    # for t in threads:
    #     t.start()
    get6v()