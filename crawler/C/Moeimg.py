import Config

if __name__ == '__main__':
#	Config.loadHttpProxy()
	soup=Config.requestUrlWithChrome("http://moeimg.net/taglist")
	taglist=soup.select('.taglist')
	if len(taglist):
		tds=taglist[0].select('td')
		for td in tds:
			a=td.select('a')
			if len(a):
				groupTitle=a[0].text
				groupHref=a[0]['href']
				print("tag =",groupTitle,"\n","href =",groupHref)
				soup=Config.requestUrlWithChrome(groupHref)
				lists=soup.select('.box.list')
				for l in lists:
					a=l.select('a')
					if len(a):
						listTitle=a[0]['title']
						listHref=a[0]['href']
						print("group =",listTitle,"\n","href =",listHref)
						soup=Config.requestUrlWithChrome(listHref)
						imgs=soup.select('.thumbnail_image')
						for img in imgs:
							imgName=img['alt']+'.jpg'
							imgHref=img['src']
							Config.downloadFile(savePath="/Volumes/J/moeimg/"+groupTitle+"/"+listTitle,filePath=imgHref,fileName=imgName,isHTTPS=True)
	