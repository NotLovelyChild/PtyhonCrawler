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
import selenium

proxies = [{'https': 'https://115.155.122.148:8118',
            'https':'https://119.101.115.93:9999',
            'https':'https://119.101.114.119:9999',
            'https':'https://119.101.117.215:9999'}]
httpPorxies = [{'http': 'http://119.101.115.5:9999',
            'http':'http://119.101.116.144:9999',
            'http':'http://119.101.115.25:9999',
            'http':'http://119.101.117.190:9999'}]
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

# main_url = 'https://www.manhuatai.com'
# main_turl = 'https://www.tohomh.com'

def requestUrl(url):
    requestManager = requests.get(url, headers=headers,proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    requestManager.encoding = 'UFT-8'
    return BeautifulSoup(requestManager.text, 'html.parser')

# def loadComic():
#     data = {}
#     list = []
#     for i in range(1,60):
#         print('加载第' + str(i) + '页')
#         soup = requestUrl('https://www.manhuatai.com/all_p' + str(i) + '.html')
#         comic = soup.select('.mhlist2.mhlist2_fix_top.clearfix')
#         if len(comic):
#             comic_list = comic[0].select('.sdiv')
#             for c in comic_list:
#                 name = c['title']
#                 href = main_url + c['href']
#                 img = c.select('img')
#                 img_url = ''
#                 if len(img):
#                     img_url = img[0]['data-url']
#
#                 list.append({
#                     'name':name,
#                     'href':href,
#                     'img_url':img_url
#                 })
#                 print(name, href, img_url)
#             data['list'] = list
#
#     with open('/Users/zh/Desktop/BookJson/' + 'index' + '.json', 'w') as file_obj:
#         json.dump(data, file_obj)
#         print("写入json文件：")
#
#     for l in list:
#        loadComicDetail(l['href'])

# def loadComicDetail(url):
#     comic_name = url.split('/')[-2]
#     print(comic_name)
#     data = {}
#     #读取本地文件
#     try:
#         with open('/Users/zh/Desktop/BookJson/' + comic_name + '.json', 'r') as file_obj:
#             data = json.load(file_obj)
#     except IOError:
#         print('IO error')
#
#     soup = requestUrl(url)
#     #基本信息
#     info_arr = []
#
#     info = soup.select('.jshtml')
#     if len(info):
#         li = info[0].select('li')
#         for l in li:
#             print(l.text)
#             info_arr.append(l.text)
#
#     data['info'] = info_arr
#
#     img = soup.select('.fm')
#     if len(img):
#         img_url = img[0]['data-url']
#         name = img[0]['title']
#         print(name,img_url)
#         data['name'] = name
#         data['img_url'] = img_url
#
#
#     #章节列表
#     c_list = []
#     try:
#         c_list = data['list']
#     except KeyError:
#         print('data key error (list)')
#
#     titles = []
#     for l in c_list:
#         try:
#             titles.append(l['title'])
#         except KeyError:
#             continue
#
#     list = soup.select('#topic1')
#     if len(list):
#         li = list[0].select('li')
#         for l in li:
#             a = l.select('a')
#             if len(a):
#                 href = main_url + a[0]['href']
#                 title = a[0]['title']
#                 if title in titles:
#                     print(title,'章节已存在')
#                     continue
#                 print(title,href)
#                 c_list.append({
#                     'title':title,
#                     'href':href,
#                     'info':loadChapter(href)
#                 })
#             data['list'] = c_list
#             with open('/Users/zh/Desktop/BookJson/' + comic_name + '.json', 'w') as file_obj:
#                 '''写入json文件'''
#                 json.dump(data, file_obj)
#                 print("写入json文件：")
#
# def loadChapter(url):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     driver.find_element_by_xpath('/html/body/div[3]/div[3]/select[2]/option[3]').click()
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     mh_comicpic = soup.select('.mh_comicpic')
#
#     for i in range(0,int(len(mh_comicpic)*1500/50)):
#         y = i * 50
#         js = "var q=document.documentElement.scrollTop=" + str(y)
#         driver.execute_script(js)
#         time.sleep(0.1)
#     img_url = []
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     mh_comicpic = soup.select('.mh_comicpic')
#     for m in mh_comicpic:
#         img = m.select('img')
#         if len(img):
#             try:
#                 img_url.append(img[0]['src'])
#                 print(img[0]['src'])
#             except KeyError:
#                 print('KeyError')
#
#     driver.quit()
#     return img_url
#
# def loadTComic():
#     data = {}
#     list = []
#     for i in range(1,324):
#         soup = requestUrl('https://www.tohomh.com/f-1------updatetime--' + str(i) + '.html')
#         comic = soup.select('.box-body')
#         if len(comic):
#             li = comic[0].select('li')
#             for l in li:
#                 c = l.select('.mh-item')
#                 if len(c):
#                     a = c[0].select('a')
#                     img = c[0].select('.mh-cover')
#                     if len(a):
#                         href = main_turl + a[0]['href']
#                         name = a[0]['title']
#                         print(name,href)
#                         list.append({
#                             'name': name,
#                             'href': href
#                         })
#                         comic_name = href.split('/')[-2]
#                         list.append({'comic_name':comic_name})
#                     if len(img):
#                         img_info = img[0]['style']
#                         img_url = img_info[img_info.find('(') + 1:img_info.find(')')]
#                         print(img_url)
#                         list.append({
#                             'img_url': img_url
#                         })
#             data['list'] = list
#
#         with open('/Users/zh/Desktop/BookJson/' + 'index' + '.json', 'w') as file_obj:
#             json.dump(data, file_obj)
#             print("写入json文件：")
#
#     for l in list:
#         loadTComicDetail(l['href'])
#
# def loadTComicDetail(url):
#     comic_name = url.split('/')[-2]
#     print(comic_name)
#     data = {}
#     #读取本地文件
#     try:
#         with open('/Users/zh/Desktop/BookJson/' + comic_name + '.json', 'r') as file_obj:
#             data = json.load(file_obj)
#     except IOError:
#         print('IO error')
#
#     soup = requestUrl(url)
#
#     #基本信息
#
#     # 章节列表
#     c_list = []
#     try:
#         c_list = data['list']
#     except KeyError:
#         print('data key error (list)')
#
#     titles = []
#     for l in c_list:
#         try:
#             titles.append(l['title'])
#         except KeyError:
#             continue
#
#     list = soup.select('#detail-list-select-1')
#     if len(list):
#         li = list[0].select('li')
#         for l in li:
#             a = l.select('a')
#             if len(a):
#                 href = main_turl + a[0]['href']
#                 title = a[0].text
#                 if title in titles:
#                     print(title,'章节已存在')
#                     continue
#                 print(title,href)
#                 c_list.append({
#                     'title':title,
#                     'href':href
#                 })
#             data['list'] = c_list
#             with open('/Users/zh/Desktop/BookJson/' + comic_name + '.json', 'w') as file_obj:
#                 '''写入json文件'''
#                 json.dump(data, file_obj)
#                 print("写入json文件：")
#
# def loadTChapter(url):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     page = '50'
#     title = soup.select('h1')
#     if len(title):
#         span = title[0].select('span')
#         if len(span):
#             pageStr = span[0].text.replace('(','').replace(')','')
#             page = pageStr.split('/')[-1]
#             print(page,'页')
#     for i in range(0,int(int(page)*1500/50)):
#         y = i * 50
#         js = "var q=document.documentElement.scrollTop=" + str(y)
#         driver.execute_script(js)
#         time.sleep(0.1)
#     img_url = []
#     mh_comicpic = soup.select('.comicpage')
#     if len(mh_comicpic):
#         imgs = mh_comicpic[0].select('img')
#         print(imgs)

url96 = 'http://www.96mh.com'

def getCoimc():
    data = {}
    list = []
    # for i in range(1,35):
    #     soup = requestUrl('http://www.96mh.com/all/' + str(i) + '.html')
    #     cy_list_mh = soup.select('.cy_list_mh')
    #     if len(cy_list_mh):
    #         li = cy_list_mh[0].select('.pic')
    #         for l in li :
    #             href = url96 + l['href']
    #             comic_name = href.split('/')[-2]
    #             name = ''
    #             img_url = ''
    #             img = l.select('img')
    #             if len(img):
    #                 name = img[0]['alt']
    #                 img_url = img[0]['src']
    #             list.append({
    #                 'name': name,
    #                 'href': href,
    #                 'img_url': img_url,
    #                 'comic_name': comic_name
    #             })
    #             print(name, comic_name, href, img_url)
    #         data['list'] = list
    #
    #     with open('/Users/zh/Desktop/BookJson/' + 'index' + '.json', 'w') as file_obj:
    #         json.dump(data, file_obj)
    #         print("写入json文件：")
    with open('/Users/zh/Desktop/BookJson/' + 'index' + '.json', 'r') as file_obj:
        list = json.load(file_obj)


    for l in list['list']:
        getComicDetail(l['href'])


def getComicDetail(url):
    soup = requestUrl(url)
    data = {}
    # 基本信息
    info_arr = []
    #名字
    if len(soup.select('.cy_title')):
        print(soup.select('.cy_title')[0].text)
        info_arr.append(soup.select('.cy_title')[0].text)

    xinxi = soup.select('.cy_xinxi')
    for x in xinxi:
        print(x.text)
        info_arr.append(x.text)

    data['info'] = info_arr

    comic_name = url.split('/')[-2]
    print(comic_name)

    #读取本地文件
    try:
        with open('/Users/zh/Desktop/BookJson/' + comic_name + '.json', 'r') as file_obj:
            data = json.load(file_obj)
    except IOError:
        print('IO error')

    #章节列表
    c_list = []
    try:
        c_list = data['list']
    except KeyError:
        print('data key error (list)')

    titles = []
    for l in c_list:
        try:
            titles.append(l['title'])
        except KeyError:
            continue

    list = soup.select('#mh-chapter-list-ol-0')
    if len(list):
        li = list[0].select('li')
        for l in li:
            a = l.select('a')
            if len(a):
                href = url96 + a[0]['href']
                title = ''
                p = a[0].select('p')
                if len(p):
                    title = p[0].text
                if title in titles:
                    print(title,'章节已存在')
                    continue
                print(title,href)
                c_list.append({
                    'title':title,
                    'href':href,
                    'info':getChapter(href)
                })
            data['list'] = c_list
            with open('/Users/zh/Desktop/BookJson/' + comic_name + '.json', 'w') as file_obj:
                '''写入json文件'''
                json.dump(data, file_obj)
                print("写入json文件：")

def getChapter(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    k_pageSelect = soup.select('#k_pageSelect')

    img_url = []

    if len(k_pageSelect):
        values = k_pageSelect[0].select('option')
        for value in values:
            while True:
                try:
                    print('页', value['value'])
                    driver.find_element_by_xpath('/html/body/div[3]/div/select/option[' + value['value'] +']').click()
                    time.sleep(1)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    img = soup.select('#qTcms_pic')
                    if len(img):
                        url = img[0]['src'][2:]
                        print(url)
                        img_url.append(url)
                except selenium.common.exceptions.NoSuchElementException:
                    print('未找到对应元素')
                    time.sleep(5)
                    continue
                except selenium.common.exceptions.TimeoutException:
                    print('Time out')
                    time.sleep(5)
                    continue
                break


    driver.quit()
    return img_url

if __name__ == '__main__':
    getCoimc()