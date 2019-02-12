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

proxies = [{'https': 'https://115.155.122.148:8118',
            'https':'https://119.101.115.93:9999',
            'https':'https://119.101.114.119:9999',
            'https':'https://119.101.117.215:9999'}]
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
    h = httpPorxies[random.randint(0,len(httpPorxies) - 1)]
    print('当前使用代理为',h)
    requestManager = requests.get(url, headers=headers,proxies=h, verify=False)
    requestManager.encoding = None
    return BeautifulSoup(requestManager.text, 'html.parser')

def biquge():
    main_url = 'https://www.biqiuge.com'
    chapter_list = []
    for i in range(1, 46500):
        while True:
            try:
                json_data = {}
                info_arr = []
                book_url = 'https://www.biqiuge.com/book/' + str(i) + '/'
                print('loading', book_url)
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(book_url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                # 书本信息
                small = soup.select('.small')
                if len(small):
                    span = small[0].select('span')
                    for s in span:
                        info_arr.append(s.text)

                intro = soup.select('.intro')
                if len(intro):
                    info_arr.append(intro[0].text)

                json_data['info'] = info_arr
                lists = soup.select('.listmain')

                # 名字 图片地址
                book_info = soup.select('.cover')
                name = ''
                if len(book_info):
                    info = book_info[0].select('img')
                    if len(info):
                        name = info[0]['alt']
                        img_url = main_url + info[0]['src']
                        json_data['name'] = name
                        json_data['img_url'] = img_url
                        print(name, img_url)
                        chapter_list.append(json_data)
                else:
                    print('当前URL不存在')
                    continue

                #获取详情

                lists = soup.select('.listmain')
                json_data = {}
                chapter_list = []
                book_info = soup.select('.cover')
                name = ''
                if len(book_info):
                    info = book_info[0].select('img')
                    if len(info):
                        name = info[0]['alt']
                        img_url = main_url + info[0]['src']
                        json_data['name'] = name
                        json_data['img_url'] = img_url
                        print(name, img_url)
                # 读取本地文件
                cs = {}
                try:
                    with open('/Users/zh/Desktop/Book/' + name + '.json', 'r') as file_obj:
                        cs = json.load(file_obj)
                except IOError:
                    print('IO error')

                chapters = []

                try:
                    chapter_list = cs['chapter_list']
                    for c in chapter_list:
                        cn = ''
                        try:
                            cn = c['chapter_name']
                            chapters.append(cn)
                        except KeyError:
                            print('NO search key chapter_name')
                except KeyError:
                    print('No search key chapter_list')

                if len(lists):
                    dd = lists[0].select('a')
                    for d in dd:
                        print(d['href'], d.text)
                        chapter_name = d.text
                        chapter_url = main_url + d['href']

                        if chapter_name in chapters:
                            print('当前章节已存在')
                            continue

                        chrome_options = webdriver.ChromeOptions()
                        chrome_options.add_argument('--headless')
                        driver = webdriver.Chrome(options=chrome_options)
                        driver.get(chapter_url)
                        time.sleep(4)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        div = soup.select('.showtxt')
                        content = 'loading...... \n 在浏览器上打开吧'
                        if len(div):
                            content = div[0].text
                            print(div[0].text)
                        else:
                            continue

                        chapter_list.append({
                            'chapter_name': chapter_name,
                            'chapter_url': chapter_url,
                            'content': content
                        })

                        json_data['chapter_list'] = chapter_list
                        with open('/Users/zh/Desktop/Book/' + name + '.json', 'w') as file_obj:
                            '''写入json文件'''
                            json.dump(json_data, file_obj)
                            print("写入json文件：")
                        driver.quit()


                with open('/Users/zh/Desktop/Book/index.json', 'w') as file_obj:
                    json.dump(chapter_list, file_obj)
                    print("写入index.json文件：")
            except requests.exceptions.ConnectTimeout:
                print('TimeOut')
                continue
            break





if __name__ == '__main__':
    biquge()