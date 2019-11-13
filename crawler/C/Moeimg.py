import Config

if __name__ == '__main__':
	soup=Config.requestUrlWithChrome("http://moeimg.net/taglist")
	taglist=soup.select('.taglist')
	if len(taglist):
		tds=taglist[0].select('td')
		for td in tds:
			a=td.select('a')
			if len(a):
				title=a[0].text
				href=a[0]['href']
				