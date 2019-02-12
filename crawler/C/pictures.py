import requests
from bs4 import BeautifulSoup
import time
import urllib3
import http
import pathlib
import random
import socket

proxies = [{'https': 'https://122.4.44.66:22300',
            'https':'https://119.101.118.109:9999',
            'https':'https://119.101.117.226:9999',
            'https':'https://115.221.112.90:808'}]

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
pro = {'https': 'https://124.205.143.212:38768'}

def requestUrl(url):
    requestManager = requests.get(url, headers=headers,proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    requestManager.encoding = 'UTF-8'
    return BeautifulSoup(requestManager.text, 'html.parser')


def downloadImg(name,url):
    print('download start')
    style = url.split('.')[-1]
    address = "/Users/zh/Desktop/iPad" + "/" + name.replace(' ','') + '.' + style
    path = pathlib.Path(address)
    if path.is_file():
        print('当前文件已存在')
        return

    try:
        imgresponse = requests.get(url, stream=True, proxies=proxies[random.randint(0,len(proxies) - 1)],timeout=10)
        image = imgresponse.content
        try:
            with open(address, "wb") as file:
                file.write(image)
                print ('download ok',name)
        except IOError:
            print("IO Error\n")
            pass
        except UnboundLocalError:
            print('UnboundLocalError')
            pass
        except socket.timeout:
            print('socket.timeout')
            pass
        except urllib3.exceptions.ReadTimeoutError:
            print('urllib3.exceptions.ReadTimeoutError')
            pass
        except OSError:
            print('OSError')
            pass
        finally:
            file.close
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
    except requests.exceptions.Timeout:
        print('requests.exceptions.Timeout')
        pass
    except socket.timeout:
        print('socket.timeout')
        pass
    except urllib3.exceptions.ReadTimeoutError:
        print('urllib3.exceptions.ReadTimeoutError')
        pass
    except requests.exceptions.ConnectionError:
        print('requests.exceptions.ConnectionError')
        pass
    except UnboundLocalError:
        print('UnboundLocalError')
        pass
    except OSError:
        print('OSError')
        pass
    finally:
        print()

# 美卓
#美卓 得到类型
def meizhuo(mainUrl):
    dataArr = []
    index = 0
    soup = requestUrl(mainUrl)
    main_cont = soup.select('.main_cont')
    for m in main_cont:
        tit_clearfix = m.select('.tit.clearfix')
        for t in tit_clearfix:
            group_title = t.select('h2')
            href = t.select('.tit_more')
            title = ''
            a = ''
            if len(group_title) > 0:
                title = group_title[0].text
            if len(href) > 0:
                a = href[0]['href']
            if len(title) > 0 and len(a) > 0:
                dataArr.append({
                    'name':title,
                    'href':a
                })

    for i in dataArr:
        print(index,i['name'],i['href'])
        index += 1
    print('请选择')
    select = input()
    if select == '0' or select == '1':
        meizhuo_get_classification(dataArr[int(select)])
    elif select == '2' or select == '3':
        meizhuo_get_group_list(dataArr[int(select)])

#根据不同的分类获取
def meizhuo_get_group_list(data):
    dataArr = []
    index = 0
    soup = requestUrl(data['href'])
    main_cont = soup.select('.main_cont')
    for m in main_cont:
        tit_clearfix = m.select('.tit.clearfix')
        for t in tit_clearfix:
            group_title = t.select('h2')
            href = t.select('.tit_more')
            title = ''
            a = ''
            if len(group_title) > 0:
                title = group_title[0].text
            if len(href) > 0:
                a = href[0]['href']
            if len(title) > 0 and len(a) > 0:
                dataArr.append({
                    'name':title,
                    'href':a
                })

    for i in dataArr:
        print(index,i['name'],i['href'])
        index += 1
    print('请选择')
    select = input()
    meizhuo_get_picture_group(dataArr[int(select)])

#美卓 得到类型分类
def meizhuo_get_classification(data):
    dataArr = []
    index = 0
    soup = requestUrl(data['href'])
    cont = soup.select('.cont2') + soup.select('.cont1')
    if len(cont) > 0:
        a = cont[0].select('a')
        for i in a:
            title = i.text
            href = i['href']
            if len(title) > 0 and len(href) > 0:
                dataArr.append({
                    'name': title,
                    'href': href
                })

    for i in dataArr:
        print(index, i['name'], i['href'])
        index += 1
    print('请选择')
    select = input()
    meizhuo_get_picture_group(dataArr[int(select)])

#美卓 根据分类得到图片组地址
def meizhuo_get_picture_group(data):
    dataArr = []
    url = data['href']
    while 1:
        soup = requestUrl(url)
        left_list = soup.select('.list_cont.Left_list_cont') + soup.select('.list_cont.Left_list_cont.Left_list_cont2')
        if len(left_list) > 0:
            clearfix = left_list[0].select('.clearfix')
            if len(clearfix) > 0:
                lis = clearfix[0].select('li')
                print(lis)
                for li in lis:
                    a = li.select('a')
                    p = li.select('p')
                    if len(a) > 0:
                        title = a[0]['title']
                        if len(title) <= 0 and len(p) > 0:
                            title = p[0].text
                        href = a[0]['href']
                        print(title,href)
                        if len(title) > 0 and len(href) > 0:
                            dataArr.append({
                                'name': title,
                                'href': href
                            })
        #获取下一页地址
        next_page = soup.select('.next')
        if len(next_page) > 0:
            next_url = next_page[0]['href']
            url = next_url
        else:
            break
    print('共',len(dataArr),'组')
    for i in  dataArr:
        meizhuo_get_picutrl_urls(i)

#美卓 获得每组图片的URL组
def meizhuo_get_picutrl_urls(data):
    index = 1
    dataArr = []
    soup = requestUrl(data['href'])
    current = soup.select('.scroll-img.clearfix')
    for c in current:
        hrefs = c.select('a')
        for h in hrefs:
            href = h['href']
            name = data['name'] + str(index)
            index += 1
            dataArr.append({
                'name': name,
                'href': href
            })

    for i in dataArr:
        meizhuo_get_picture_url(i)

#美卓 获取图片URL
def meizhuo_get_picture_url(data):
    soup = requestUrl(data['href'])
    pic = soup.select('.pic-meinv')
    if len(pic) > 0:
        img = pic[0].select('img')
        if len(img) > 0:
            src = img[0]['src']
            print(data['name'],src)
            downloadImg(data['name'],src)


#5858壁纸站
#获取分类
def f_get_style_list():
    while 1:
        main_url = ''
        print('请选择类型\n'
              '1:电脑壁纸\n'
              '2.平板壁纸\n'
              '3.手机壁纸\n'
              '4.精选一图\n'
              '5.热门壁纸\n'
              '6.动态壁纸\n'
              '-1.退出')
        select = input()
        if select == '1':
            main_url = 'http://www.5857.com/pcbz/'
        elif select == '2':
            main_url = 'http://www.5857.com/pad/'
        elif select == '3':
            main_url = 'http://www.5857.com/sjbz/'
        elif select == '4':
            main_url = 'http://www.5857.com/pcbz/36.html'
            f_get_img_group({'name':'精选一图','href':main_url})
            continue
        elif select == '5':
            main_url = 'http://www.5857.com/html/hotlist-1.html'
            continue
        elif select == '6':
            main_url = 'http://www.5857.com/list-42-0-0-0-0-0-1.html'
        elif select == '-1':
            break
        else:
            print('输入有误，请重新输入。')
            continue

        f_get_group_detail(main_url)


#获取详细分类
def f_get_group_detail(url):
    dataArr = []
    index = 0
    soup = requestUrl(url)
    first = soup.select('.filter_item.first')
    if len(first) > 0:
        dd = first[0].select('a')
        for d in dd:
            title = d.text
            href = d['href']
            dataArr.append({
                'name':title,
                'href':href
            })

    for i in dataArr:
        print(index,i['name'],i['href'])
        index += 1
    print('请选择')
    select = input()
    print(dataArr[int(select)])
    f_get_img_group(dataArr[int(select)])
#获取图片组
def f_get_img_group(data):
    dataArr = []
    url = data['href']
    index = 1
    is_continue = 1
    while is_continue:
        print('获取第',str(index),'页')
        print(url)
        soup = requestUrl(url)
        listbox = soup.select('.listbox')
        for box in listbox:
            img = box.select('a')
            if len(img) > 0:
                title = img[0]['title']
                href = img[0]['href']
                if {'name': title, 'href': href} in dataArr:
                    is_continue = 0
                else:
                    print(title, href)
                    dataArr.append({
                        'name': title,
                        'href': href
                    })


        #获取下一页地址
        pages = soup.select('.page')
        if len(pages) > 0:
            next = pages[-1].select('a')
            if len(next) > 0:
                next_url = next[-1]['href']
                index += 1
                url = 'http://www.5857.com/' + next_url
            else:break
        else:break

    print('共有',len(dataArr),'组')
    time.sleep(3)
    for d in dataArr:
        f_get_img_url_group(d)

#获取每组图片的URL
def f_get_img_url_group(data):
    dataArr = []
    url = data['href']
    index = 1
    soup = requestUrl(url)
    img_box = soup.select('.img-box')
    if len(img_box) > 0:
        hrefs = img_box[0].select('a')
        for a in hrefs:
            img = a.select('img')
            if len(img) > 0:
                href = img[0]['src']
                name = data['name'] + str(index)
                alt = img[0]['alt']
                if '公众号' not in alt:
                    print(name,href)
                    index += 1
                    dataArr.append({
                        'name': name,
                        'href': href
                    })

    for d in dataArr:
        downloadImg(d['name'],d['href'])

if __name__ == '__main__':
    while 1:
        print('请选择要抓取的网站\n'
              '1:美卓\n'
              '2.5857壁纸站\n'
              '-1.退出')
        i = input()
        if i == '1':
            meizhuo('http://www.win4000.com/')
        elif i == '2':
            f_get_style_list()
        elif i == '-1':
            break
        else:
            print('输入有误，请重新输入。')
            continue