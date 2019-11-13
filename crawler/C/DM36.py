import Config

def search(name):
	data=[]
	url="http://www.36dm.club/search.php?keyword="+name
	soup=Config.requestUrlWithChrome(url)
	items=soup.select(".alt1")+soup.select(".alt2")
	for item in items:
		a=item.select("a")
		if len(a)>1:
			title=a[1].text
			href="https://www.36dm.club/"+a[1]["href"]
			print(title,href)

def get_magnet(url):
	soup=Config.requestUrlWithChrome(url)
	magnet=soup.select("#magnet")
	if len(magnet):
		return magnet[0]['href']

if __name__ == "__main__":
#	search("鬼灭之刃")
#	url="https://www.36dm.com/show-c61a99ab29570ae62b61782f7647605f3b3af5d9.html"
#	print(get_magnet(url))
	Config.loadHttpProxy()