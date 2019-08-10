import requests

headers = {"Content-Type": "application/json"}
data={
		"msgtype": "text",
		"text": {
			"content": "hello world"
		}
   }
r = requests.post(
		url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d4602d39-1620-4a0f-acf2-d85c4c3990fe',
		headers=headers, json=data)
print(r.text)