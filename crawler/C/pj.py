from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv

#中国评剧曲谱网  http://www.pingju.com.cn
#运行自动爬取网站上所有戏曲并分类
#自动创建目录、自动下载戏曲（序号对应）

def get_p_list():
    with open('/Users/zh/Desktop/p1.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '曲名', '演唱', 'MP3地址'])
        for i in range(927, 929):
            print('Loadpage ' + str(i))
            url = 'http://www.pingju.com.cn/qupu_detail.php?id=' + str(i)
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            time.sleep(5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            if len(soup.select('.son_div')) > 0 and len(soup.select('audio')) > 0:
                name = soup.select('.son_div')[0].text.split('\n')[1].lstrip().strip()
                user = soup.select('.son_div')[0].text.split('\n')[2].lstrip()
                url = soup.select('audio')[0].select('source')[0]['src']
                print(name, user, url)
                data = {
                    'page':str(i),
                    'name': name,
                    'user': user,
                    'url': url
                }
                print('write data to p.csv')
                writer.writerow([i,name,user,url])
                print('write data to p.csv success')
                driver.quit()
                if i==927:
                    download(data)
            else:
                print('当前曲目不存在')
                print('write data to p.csv')
                writer.writerow([i, '不存在', '', ''])
                print('write data to p.csv success')

def download(data):
    pr = {'https':'https://106.75.164.15:3128'}
    print('start download',data['name'])
    mp3response = requests.get(data['url'], stream=True, proxies=pr)
    image = mp3response.content
    address = "/Users/zh/Desktop/p" + "/" + data['page'] + '.' +data['name'] + '\t' + data['user'] + ".mp3"
    try:
        with open(address, "wb") as f:
            f.write(image)
            print ('download ok',[data['name']])
    except IOError:
        print("IO Error\n")
    finally:
        f.close


if __name__ == '__main__':
    # get_p_list()
    url = 'http://www.pingju.com.cn/qupu_detail.php?id=924'
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    frame = driver.switch_to.frame(driver.find_element_by_id('pic'))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.select('img'))
    time.sleep(3)
    js = 'document.pic.window.location=\'pic_pre.php?flag=1&id=924&page=1\''
    driver.execute_script(js)
    print(soup.select('img'))
    driver.quit()