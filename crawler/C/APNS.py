import APNSWrapper
import binascii

# 请替换为自己的设备的deviceToken
deviceToken = binascii.unhexlify("4d8f0de0b2ce0e3e326a4948606e5ac65397d8654c1ffad85774dac20d3971f9")

#创建通知对象
notification = APNSNotification()
notification.token(deviceToken)
notification.alert("土豪，我们做朋友吧")
notification.badge(5)
notification.sound()

#创建发送通知的这个wrapper
pem_cert_name = "/Users/jackmacbook/Downloads/apns_prod.pem"  # 需要使用自己应用的P12证书
wrapper = APNSNotificationWrapper(pem_cert_name, True) # 默认为连接正式环境，修改为True时连接沙盒环境
wrapper.append(notification)
wrapper.notify()