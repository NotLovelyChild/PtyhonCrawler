import Config

def search(name):
	data=[]
	#http://www.36dm.club/show-45ddaab867fe81485a098beb982a7b8026b4ec05.html
	url="http://www.36dm.club/search.php?keyword="+name
	soup=Config.requestUrlWithChrome(url)
	items=soup.select(".alt1")+soup.select(".alt2")
	for item in items:
		print(item)


if __name__ == "__main__":
	search("鬼灭之刃")