import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
def requestUrl(url):
    requestManager = requests.get(url, headers=headers, verify=False)
    requestManager.encoding = 'UTF-8'
    return BeautifulSoup(requestManager.text, 'html.parser')

def loadHTTP():
    ips = []
    for i in range(1,6):
        url = 'https://www.xicidaili.com/wt/'+str(i)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        ip_list = soup.select('#ip_list')
        if len(ip_list):
            odd = ip_list[0].select('.odd')
            for o in odd:
                td = o.select('td')
                if len(td):
                    ip = td[1].text
                    port = td[2].text
                    d = {'http':'http://'+ip+':'+port}
                    ips.append(d)
                    print(d)
    with open('/Users/zh/Desktop/http.json', 'w') as file_obj:
        json.dump(ips, file_obj)
        print("写入json文件：")


def loadHTTPS():
    ips = []
    for i in range(1,6):
        url = 'https://www.xicidaili.com/wn/'+str(i)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        ip_list = soup.select('#ip_list')
        if len(ip_list):
            odd = ip_list[0].select('.odd')
            for o in odd:
                td = o.select('td')
                if len(td):
                    ip = td[1].text
                    port = td[2].text
                    d = {'https':'https://'+ip+':'+port}
                    ips.append(d)
                    print(d)
    with open('/Users/zh/Desktop/https.json', 'w') as file_obj:
        json.dump(ips, file_obj)
        print("写入json文件：")

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

if __name__ == '__main__':
    loadHTTP()
    loadHTTPS()