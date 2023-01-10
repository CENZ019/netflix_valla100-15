import bs4
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://www.cinecolombia.com/bogota'
page=urllib.request.urlopen(url)
page_soup=BeautifulSoup(page,'html.parser')
img_items=page_soup.find('div',{'class':'columns screening-columns is-multiline columns--slim'})
img_div=img_items.find_all(class_='movie-item')

i=1
for img in img_div:
    img_tag = img.find('img')
    img_src = img_tag.get('data-src')
    # #img_title=img_tag.get('title')
    if img_src[:1]=='/':
        image='https:'+img_src
    else:
        image=img_src
    file_name=str(i)
    i+=1
    img_file=open(file_name +'.jpg','wb')
    img_file.write(urllib.request.urlopen(image).read())
    img_file.close()
