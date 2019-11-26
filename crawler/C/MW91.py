import Config
import _thread
import time

def downloadImg():
	for i in range(1,200):
		url="https://tu.91mw.net/page/"+str(i)+"/"
		soup=Config.requestUrl(url)
		groups=soup.select(".blog-title")
		for group in groups:
			a=group.select("a")
			if len(a):
				title=a[0].text
				href=a[0]['href']
				print(title,href)
				soup=Config.requestUrl(href)
				tab=soup.select(".blog-details-text")
				if len(tab):
					imgs=tab[0].select('img')
					num=1
					for img in imgs:
						img_name=title+str(num)+".jpg"
						img_href="https://tu.91mw.net/"+img['src']
						num+=1
						_thread.start_new_thread(down, (title,img_href,img_name))
						

def down(title, path, name):
	Config.downloadFile(savePath="/Volumes/J/mw91/"+title,filePath=path,fileName=name)
if __name__ == '__main__':
	downloadImg()