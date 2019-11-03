import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import os
from contextlib import closing
import pathlib
import urllib3
import http
import selenium

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

user_agents = [
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:64.0) Gecko/20100101 Firefox/64.0',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60Opera/8.0 (Windows NT 5.1; U; en)',
	'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
	'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
	'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',
	'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
	'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
]

def getHTTP():
	data = []
	try:
		with open('http.json', 'r') as file_obj:
			data = json.load(file_obj)
	except IOError:
		print('IO error')
	return data[random.randint(0,len(data))]

def getHTTPS():
	data = []
	try:
		with open('https.json', 'r') as file_obj:
			data = json.load(file_obj)
	except IOError:
		print('IO error')
	return data[random.randint(0,len(data))]
	
def loadHttpProxy():
	ips = []
	for i in range(1,10):
		url = 'https://www.xicidaili.com/wt/'+str(i)
		soup = requestUrlWithChrome(url)
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
	with open('http.json', 'w') as file_obj:
		json.dump(ips, file_obj)
		print("写入json文件：")
	
	ips = []
	for i in range(1,10):
		url = 'https://www.xicidaili.com/wn/'+str(i)
		soup = requestUrlWithChrome(url)
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
	with open('https.json', 'w') as file_obj:
		json.dump(ips, file_obj)
		print("写入json文件：")
		
def requestUrl(url):
	while True:
		try:
			requests.packages.urllib3.disable_warnings()
			requestManager = requests.get(url, headers=headers, verify=False, proxies=getHTTP())
			requestManager.encoding = None
			return BeautifulSoup(requestManager.text, 'html.parser')
		except requests.exceptions.ConnectionError:
			print('Connection Error try retry')
			continue

def requestUrlWithChrome(url):
	while True:
		try:
			chrome_options = webdriver.ChromeOptions()
#			chrome_options.add_argument('--headless')
			chrome_options.add_argument('lang=zh_CN.UTF-8')
			#设置user-agent
			user_agent="user-agent="+user_agents[random.randint(0,len(user_agents))]
			chrome_options.add_argument(user_agent)
			#禁用图片
			prefs = {"profile.managed_default_content_settings.images": 2}
			chrome_options.add_experimental_option("prefs", prefs)
			#设置ip
			driver = webdriver.Chrome(options=chrome_options)
			driver.get(url)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			driver.quit()
			return soup
		except selenium.common.exceptions.TimeoutException:
			driver.quit()
			print('Connection Error try retry')
			continue
			
def downloadFile(savePath='',filePath='',fileName=''):
	#判断文件名是否存在
	if not len(fileName):
		fileName = filePath.split("/")[-1]
	print("开始下载文件: "+fileName)
	#判断保存文件夹是否存在
	if not os.path.exists(savePath):
		os.makedirs(savePath)
	#判断文件是否存在
	path=pathlib.Path(savePath+"/"+fileName)
	if path.is_file():
		print(fileName+' 已存在')
		return
	#开始下载
	try:
		with closing(requests.get(filePath,headers=headers,stream=True, proxies=getHTTP())) as response:
#		with closing(requests.get(filePath,headers=Config.headers,stream=True)) as response:
			chunk_size = 1024  # 单次请求最大值
			content_size = int(response.headers['content-length'])  # 内容体总大小
			data_count = 0
			try:
				with open(path, "wb") as file:
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