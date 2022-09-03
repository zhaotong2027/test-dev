import os

import requests

# # 打开浏览器
# url1 = "http://127.0.0.1:50267/session"
# data1 = {"capabilities": {"firstMatch": [{}], "alwaysMatch": {"browserName": "chrome", "platformName": "any",
#                                                               "goog:chromeOptions": {"extensions": [], "args": []}}},
#          "desiredCapabilities": {"browserName": "chrome", "version": "", "platform": "ANY",
#                                  "goog:chromeOptions": {"extensions": [], "args": []}}}
# res = requests.post(url=url1, json=data1, timeout=5)
# print(res.json())
# session_id = res.json()["sessionId"]
#
# # 启动webdriver服务
# os.system("/usr/local/bin/chromedriver")
#
# # 访问百度地址
# url2 = "http://127.0.0.1:50267/session/{}/url".format(session_id)
# data2 = {"url": "https://baidu.com"}
# res2 = requests.post(url=url2, json=data2, timeout=5)
# print(res2.json())
