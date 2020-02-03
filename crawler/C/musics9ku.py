import Config
import json

if __name__ == "__main__":
	while True:
		print("输入歌曲名字:\n")
		musicName = input()
		searchUrl = "http://baidu.9ku.com/song/"+musicName
		soup=Config.requestUrlWithChrome(searchUrl)
		ul=soup.select(".songList")
		data=[]
		i=0
		if len(ul):
			for li in ul[0].select('li'):
				iddiv=li.select('.check')
				namediv=li.select('.songName')
				singerdiv=li.select('.singerName')
				if len(iddiv) and len(namediv) and len(singerdiv):
					musicId = iddiv[0]['value'].replace('@','')
					musicName = namediv[0].text
					musicSinger = singerdiv[0].text
					data.append({
						'musicId':musicId,
						'musicSinger':musicSinger,
						'musicName':musicName
					})
					print('序号:',i,'///歌手:',musicSinger,'///歌曲名:',musicName)
					i+=1
		if len(data):
			print('输入下载序号:\n')
			selectNum=input()
			if len(selectNum)<=0:
				print('输入错误，重新输入歌曲名\n\n\n')
				continue
			if int(selectNum) >= len(data):
				print('输入错误，重新输入歌曲名\n\n\n')
				continue
			musicData=data[int(selectNum)]
			url="http://www.9ku.com/html/playjs/465/"+str(musicData['musicId'])+".js"
			soup=Config.requestUrl(url,https=True)
			jsondata=json.loads(soup.text.replace('(','').replace(')',''))
			mp3Url=jsondata['wma']
			mp3Name=jsondata['mname']+'.mp3'
			Config.downloadFile(savePath="/Volumes/KINGSTON",filePath=mp3Url,fileName=mp3Name,isHTTPS=True)