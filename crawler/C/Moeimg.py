import Config
import _thread

def down(gtitle,ltitle, path, name):
	Config.downloadFile(savePath="/Volumes/J/moeimg/"+gtitle+"/"+ltitle,filePath=path,fileName=name,isHTTPS=True)

if __name__ == '__main__':
#	Config.loadHttpProxy()
	soup=Config.requestUrl("http://moeimg.net/taglist", https=True)
	taglist=soup.select('.taglist')
	if len(taglist):
		tds=taglist[0].select('td')
		tds.reverse()
		for td in tds:
			a=td.select('a')
			if len(a):
				groupTitle=a[0].text
				groupHref=a[0]['href']
				print("tag =",groupTitle,"\n","href =",groupHref)
				soup=Config.requestUrl(groupHref, https=True)
				lists=soup.select('.box.list')
				for l in lists:
					a=l.select('a')
					if len(a):
						listTitle=a[0]['title']
						listHref=a[0]['href']
						print("group =",listTitle,"\n","href =",listHref)
						soup=Config.requestUrl(listHref, https=True)
						imgs=soup.select('.thumbnail_image')
						for img in imgs:
							imgName=img['alt']+'.jpg'
							imgHref=img['src']
							_thread.start_new_thread(down, (groupTitle,listTitle,imgHref,imgName))
