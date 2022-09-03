from selenium import webdriver
import time
# 启动浏览器驱动服务器
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(5)
driver.close()
