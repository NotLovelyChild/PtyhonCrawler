import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pathlib
import urllib3
import http

#花瓣网爬虫 使用用户ID爬取

proxies = [{'https': 'https://183.129.244.17:10010','https':'https://221.212.117.10:808','https':'https://117.114.149.66:53281','https':'https://101.132.122.230:3128'}]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

def loadMemberList(memberId,type):
    t = ''
    if type == '1':
        t=''
    elif type == '2':
        t='pins/'
    elif type == '3':
        t='likes/'
    url = 'http://huabanpro.com/' + memberId +'/' + t
    print(url)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    for i in range(0,1000000000000):
        time.sleep(0.02)
        js = 'window.scrollTo(0,' + str(i*10) + ')'
        driver.execute_script(js)
        s = BeautifulSoup(driver.page_source, 'html.parser')
        if len(s.select('.loading')) > 0:
            if len(s.select('.loading')[0].select('img')) > 0:
                if s.select('.loading')[0].select('img')[0]['src'] == '/img/end.png':
                    break

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    loadGroup(soup,type)

def loadGroup(s,type):
    data=[]
    index = 1
    list = s.select('.Board.wfc ') + s.select('.pin.wfc ') + s.select('.pin.wfc.wft') + s.select('.Board.wfc.default-board')

    for i in list:
        id = i['data-id']
        name = ''
        if type == '1':
            name = i.select('h3')[0].text
        elif type == '2':
            name = '采集' + str(index)
        elif type == '3':
            name = '喜欢' + str(index)

        data.append({
            'index': str(index),
            'id':id,
            'name':name
        })
        index += 1


    if type == '1':
        while 1:
            print('0','全部抓取（耗时严重）')
            for d in data:
                print(d['index'],d['name'])
            print('-1','退出')
            print('选择要抓取的类型')
            select = input()
            for d in data:
                if str(select) == d['index']:
                    loadGroupList([d])
                if str(select) == '0':
                    loadGroupList(data)
            if str(select) == '-1':
                break
    else:
        loadImgData(data)

def loadGroupList(data):
    index = 1
    dataArr = []
    for d in data:
        url = 'http://huabanpro.com/boards/' + d['id'] + '/'
        print(url)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        list = []
        for i in range(0,1000000000000):
            time.sleep(0.02)
            js = 'window.scrollTo(0,' + str(i*10) + ')'
            driver.execute_script(js)
            s = BeautifulSoup(driver.page_source, 'html.parser')
            if len(s.select('.loading')) > 0:
                if len(s.select('.loading')[0].select('img')) > 0:
                    if s.select('.loading')[0].select('img')[0]['src'] == '/img/end.png':
                        break
            list += s.select('.Board.wfc ') + s.select('.pin.wfc ') + s.select('.pin.wfc.wft')

        driver.quit()
        print(len(list))
        new_list = []
        for i in list:
            if not i in new_list:
                new_list.append(i)

        print(len(new_list))
        for i in new_list:
            id = i['data-id']
            name = d['name'] + str(index)
            style = ''
            if len(i.select('.gif-icon')) > 0:
                style = '.gif'
            else:
                style = '.jpg'
            print('id=', id)
            print('name=', name)
            print('style=',style)
            dataArr.append({
                'id': id,
                'name': name,
                'style':style
            })
            index += 1

        loadImgData(dataArr)

def loadImgData(data):
    for d in data:
        url = 'http://huabanpro.com/pins/' + str(d['id']) +'/'
        print('Loading......', url)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        imgdiv = soup.select('.main-image')
        if len(imgdiv) > 0:
            if len(imgdiv[0].select('img')) > 0:
                imgUrl = 'http:' + imgdiv[0].select('img')[0]['src']
                print(d['name'],imgUrl)
                download({
                    'name':d['name'],
                    'url':imgUrl,
                    'style':d['style']
                })
        print(soup.select('.main-image'))
        driver.quit()

def download(data):
    print('start download',data['name'])

    address = "/Users/zh/Desktop/L" + "/" + data['name'] + data['style']
    path = pathlib.Path(address)
    if path.is_file():
        print('当前文件已存在')
        return

    try:
        imgresponse = requests.get(data['url'], stream=True, proxies=proxies)
        image = imgresponse.content
        try:
            with open(address, "wb") as jpg:
                jpg.write(image)
                print ('download ok',[data['name']])
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



if __name__ == '__main__':
    print('请输入用户ID')
    memberid = input()
    print('请选择需要爬取的数据分类：\n'
          '1：画板； 2：采集； 3：喜欢')
    type = input()
    loadMemberList(memberid,type)
