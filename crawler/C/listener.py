import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

proxies = [{'https': 'https://119.101.112.97:9999'}]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
pro = {'https': 'https://124.205.143.212:38768'}

def requestUrl(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # name = soup.select('.lan')[0].text
    # url = soup.select('embed')[0]['src']
    # print(name,url)
    print(soup)
    driver.quit()

def loadData(url):
    requestManager = requests.get(url, headers=headers,proxies=proxies[-1], verify=False)
    requestManager.encoding = 'GB2312'
    return BeautifulSoup(requestManager.text, 'html.parser')

def webDriverLoadData(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.find_element_by_xpath('').text
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return driver

def download(data):
    print('start download',data['name'])
    mp3response = requests.get(data['url'], stream=True, proxies=proxies[-1])
    image = mp3response.content
    address = "/Users/zh/Desktop/K" + "/"
    try:
        with open(address + data['page'] + '.' +data['name'] + ".m4a", "wb") as f:
            f.write(image)
            print ('download ok',[data['name']])
    except IOError:
        print("IO Error\n")
    finally:
        f.close


def xitaizi():
    with open('/Users/zh/Desktop/p1.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '曲名', '语种', 'MP3地址'])
        page = 1
        for i in range(0,100000):
            d = loadData('http://www.xitaizi.com/mp3/' + str(i) + '.html')
            print('load page = ' + str(i))
            if len(d.select('.a')) > 0 and len(d.select('input')) > 0:
                name = d.select('.a')[-1].text
                style = d.select('.a')[0].select('a')[0].text
                print(name,style)
                url = d.select('input')[0]['value']
                print('Have Data')
                print('name = ' + name)
                print('style = ' + style)
                print('url = ' + url)
                writer.writerow([page, name, style,  url])
                page += 1
            else:
                print('No data')

def loveForOne():
    with open('/Users/zh/Desktop/p1.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '曲名', '分类', '音质','时长','大小','音频地址'])
        index = 1
        for i in range(1,492):
            print('load page = ' + str(i))
            if i == 1:
                list = loadData('http://www.fl5y.com/xiazai/')
            else:
                list = loadData('http://www.fl5y.com/xiazai/index_' + str(i) + '.html')
            mainUrl = 'http://www.fl5y.com/'
            for tr in list.select('tr'):
                a = tr.select('a')
                if len(a) > 0:
                    name = a[0]['title']
                    xiquurl = a[0]['href']
                    d = loadData(mainUrl + xiquurl)
                    if len(d.select('audio')) == 0:
                        continue
                    elif len(d.select('audio')[0].select('source')) == 0:
                        continue
                    url = d.select('audio')[0].select('source')[0]['src']
                    info = d.select('p.col-xs-6.col-md-12')
                    quality = ''
                    if '音质' in info[0].text:
                        quality = info[0].text

                    size = ''
                    if '大小' in info[1].text:
                        size = info[1].text

                    long = ''
                    if '长度' in info[2].text:
                        long = info[2].text

                    style = ''
                    if '分类' in info[3].text:
                        style = info[3].text
                    data = {
                        'page': str(index),
                        'name': name,
                        'quality': quality,
                        'url': url,
                        'size':size,
                        'long':long,
                        'style':style
                    }
                    download(data)
                    print(data)
                    print('write to data')
                    writer.writerow([index, name, style, quality, long, size, url])
                    index += 1

def getQuPu():


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://www.qupu123.com/xiqu/yueju/p333541.html')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print('http://www.qupu123.com' + soup.select('.imageList')[0].select('img')[0]['src'])
    time.sleep(2)
    driver.find_element_by_id('look_all').click()
    time.sleep(5)
    driver.switch_to.default_content()
    frame = driver.find_element_by_name('get_all_iframe')
    driver.switch_to.frame(frame)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    i = 1
    for s in soup.select('img'):
        imgUrl = 'http://www.qupu123.com' + s['src']
        print(imgUrl)

        mp3response = requests.get(imgUrl, stream=True)
        image = mp3response.content
        address = "/Users/zh/Desktop/L" + "/"
        try:
            with open(address + str(i) + ".jpg", "wb") as f:
                f.write(image)
                print('download ok')
        except IOError:
            print("IO Error\n")
        finally:
            f.close
        i += 1
    driver.quit()


if __name__ == '__main__':
    # getQuPu()
    loveForOne()
    # xitaizi()

