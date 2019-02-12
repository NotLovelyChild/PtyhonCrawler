import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'http://www.pingju.com.cn/qupu_detail.php?id=925'
driver.get(base_url)

driver.close()
print (driver.page_source)