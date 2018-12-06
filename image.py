import urllib.request
import os
from bs4 import BeautifulSoup
from selenium import webdriver

def imagecr():
    base_url = 'http://shop.tworld.co.kr'
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(3)
    driver.get('http://shop.tworld.co.kr/handler/Mobile-MobileMain?category_id=20010001')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.findAll('a', {'class': 'prod_link'}):
        spanimg = link.find('span',{'class' : 'img_wrap'})
        spanna = link.find('span',{'class' : 'name'})
        spani = spanimg.find('img')
        imgc = spani.get('src')
        print(base_url+imgc)
        filename = os.path.splitext(imgc)[1]
        tempname = spanna.text.replace('HOT','').replace('NEW','').strip()
        urllib.request.urlretrieve(base_url+imgc, './images/'+tempname+filename)
        print("complete!")


imagecr()