import Config
#safe all
#questionable 15
#explicit 18
if __name__ == '__main__':
#	Config.loadHttpProxy()
	print("1. all age\n2. 15 age\n3. 18 age")
	t=input("选择分级：")
	tag='safe'
	if t=="1": tag="safe"
	if t=="2": tag="questionable"
	if t=="3": tag="explicit"
	path="safe"
	if t=="1": path="safe"
	if t=="2": path="questionable"
	if t=="3": path="explicit"
	p=1
	while True:
		soup=Config.requestUrlWithChrome("http://konachan.wjcodes.com/?tag=rating:"+tag+"&p="+str(p))
		images=soup.select(".am-btn.am-btn-success.am-btn-xs")
		if not len(images):
			break;
		for image in images:
			image_str=image['onclick']
			image_url=image_str.replace("addUrl('","").replace("',this)","")
			image_name=image_str.split("/")[4]
			Config.downloadFile(savePath="/Volumes/J/konachan/"+path,filePath=image_url,fileName=image_name+".png",minSize=5)
		p=p+1
	