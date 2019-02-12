import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import csv

proxies = [{'https': 'https://211.99.26.183:808'}]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

def requestUrl(url):
    requestManager = requests.get(url, headers=headers,proxies=proxies[random.randint(0,len(proxies) - 1)], verify=False)
    requestManager.encoding = 'UTF-8'
    return BeautifulSoup(requestManager.text, 'html.parser')

if __name__ == '__main__':
    dataArr = []
    for i in range(1,6):
        soup = requestUrl('https://www.juhe.cn/docs/index/page/'+str(i))
        list = soup.select('.api-list-li')
        for api in list:
            if len(api.select('.api-name')) > 0 and len(api.select('.api-price')) > 0:
                name = api.select('.api-name')[0].text
                price = api.select('.api-price')[0].text
                print(name, price)
                dataArr.append({
                    'name':str(name),
                    'price':str(price)
                })


    with open('/Users/zh/Desktop/JH.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', 'Api名字', 'Api价格'])
        index = 1
        for api in dataArr:
            writer.writerow([str(index), api['name'], api['price']])
            index += 1