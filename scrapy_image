import re
import requests
import os

word = input("Input key word: ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
i = 0
t = 0
path = 'baidu/' + word + '/'
os.mkdir(path)
while t < 500:
  url_new = url + str(t) + '&gsm=8c'
  result = requests.get(url_new)
  html = requests.get(url_new).text
  pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
  for each in pic_url:
    print(each)
    try:
        pic = requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print('Error：couldn't download')
        continue
    fp = open(path + str(t) + str(i) +'%d.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
  t += 20
