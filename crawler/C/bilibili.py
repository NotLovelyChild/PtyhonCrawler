import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from contextlib import closing
import json
import pathlib
import urllib3
import http
import selenium
import random
import time


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
			httpPorxies=getHTTP()
			h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]
			print('The proxies = ', h, 'The url = ', url)
			requests.packages.urllib3.disable_warnings()
			requestManager = requests.get(url, headers=headers, verify=False, proxies=h)
			requestManager.encoding = None
			return BeautifulSoup(requestManager.text, 'html.parser')
		except requests.exceptions.ConnectionError:
			print('Connection Error try retry')
			continue

def requestUrlWithChrome(url):
	while True:
		try:
			print('Chrome request url = ', url)
			chrome_options = webdriver.ChromeOptions()
			chrome_options.add_argument('--headless')
			driver = webdriver.Chrome(options=chrome_options)
			driver.get(url)
			time.sleep(10)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			driver.quit()
			return soup
		except selenium.common.exceptions.TimeoutException:
			driver.quit()
			print('Connection Error try retry')
			continue

def download(data,header):
		print(data['url'])
		fileName=''
		if data['type'] == 'img':
				fileName = data['name'] + '.' + data['url'].split('.')[-1]
		elif data['type'] == 'xhamsterVideo':
				fileName=data['name']+'.mp4'
		elif data['type'] == 'mp4':
				fileName=data['name']+'.mp4'
		elif data['type'] == 'flv':
				fileName=data['name']+'.flv'
		print('To prepare download\n',fileName)
		print('Check if the file exists')

		address = "/Users/jackmacbook/Pictures/E" + "/" + fileName
		path = pathlib.Path(address)
		if path.is_file():
				print('The current file already exists')
				return
		else:
				print('The current file does not exist\n Start download ',fileName)

		try:
				httpPorxies = getHTTP()
				h = httpPorxies[random.randint(0, len(httpPorxies) - 1)]
				with closing(requests.get(data['url'],headers=header,stream=True)) as response:
					chunk_size = 1024  # 单次请求最大值
					content_size = int(response.headers['content-length'])  # 内容体总大小
					data_count = 0
					try:
						with open(address, "wb") as file:
							for data in response.iter_content(chunk_size=chunk_size):
								file.write(data)
								data_count = data_count + len(data)
								now_jd = (data_count / content_size) * 100
								print("\r Downloading progress ：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, fileName), end=" ")
					except IOError:
							print("IO Error")
							pass
					except UnboundLocalError:
							print('UnboundLocalError')
							pass
					finally:
							print('Download OK!!!!!!!!!!!!!!!!')
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


def getHTTP():
	data = []
	try:
		with open('/Users/jackmacbook/Desktop/http.json', 'r') as file_obj:
			data = json.load(file_obj)
	except IOError:
		print('IO error')

	return data

def getHTTPS():
	data = []
	try:
		with open('/Users/jackmacbook/Desktop/https.json', 'r') as file_obj:
			data = json.load(file_obj)
	except IOError:
		print('IO error')

	return data

def getbilibili():
	print('输入番号')
	av=input()
	url='https://www.bilibili.com/video/av'+av
	header={'Referer':url,
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
	cid=getbilibilicid(av)
	for c in cid:
		title=str(c['title'])
		videoPath=getBilibiliVideoUrl(av, c['cid'],c['p'])
		download({'name':title,'type':'flv','url':videoPath}, header)

def getbilibilicid(aid):
	url='https://api.bilibili.com/x/web-interface/view?aid='+aid
	jsonData=json.loads(str(requestUrl(url)))
	pages=jsonData['data']['pages']
	title=jsonData['data']['title']
	isList=jsonData['data']['subtitle']['allow_submit']
	cids=[]
	if isList == False:
		for page in pages:
			cid=page['cid']
			p=page['page']
			title=page['part']
			print(title,p,cid)
			cids.append({
				'cid':cid,
				'p':p,
				'title':str(p)+'.'+title
			})
		return cids
		
	cid='0'
	resolution=0
	for page in pages:
		dimension=page['dimension']
		width=int(dimension['width'])
		height=int(dimension['height'])
		if width*height > resolution:
			resolution=width*height
			cid=page['cid']
	print('cid =',cid)
	return [{'title':title,'cid':cid,'p':0}]
		
def getBilibiliVideoUrl(aid,cid,p):
	url='https://api.bilibili.com/x/player/playurl?avid='+str(aid)+'&cid='+str(cid)+'&qn=112&type=&fnver=0&fnval=16&otype=json&p='+str(p)
	jsonData=json.loads(str(requestUrl(url)))
	videos=jsonData['data']['dash']['video']
	videoPath=''
	resolution=0
	for video in videos:
		width=int(video['width'])
		height=int(video['height'])
		if width*height > resolution:
			resolution=width*height
			videoPath=video['baseUrl']
	print('videoPath =',videoPath)
	return videoPath


if __name__ == "__main__":
#	14184325
	getbilibili()