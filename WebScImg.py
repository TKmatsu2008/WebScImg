import requests
import re
import uuid
from bs4 import BeautifulSoup

url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
keyword = "猫"
html =requests.get(url%(keyword))
soup = BeautifulSoup(html.text,'lxml')
imgs_tag =soup.find_all('img',src=re.compile('^https://msp.c.yimg.jp/yjimage'))

for img in imgs_tag:
    print(img['src'])
    r =requests.get(img['src'])
    image_file= open(str("./picture/")+str(uuid.uuid4())+str(".jpeg"),"wb") 
    image_file.write(r.content)
    image_file.close()