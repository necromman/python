import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time

fixTop = "https://cafe.naver.com/ArticleList.nhn?search.clubid="
cafeId = "10050813"
# 10050813 파우더룸
# 10050146 중고나라
fixBot = "&search.boardtype=L&search.questionTab=A&userDisplay=50&search.page="
endPage = 5

def trade_spider():
    start = 3
    diffArr = []
    tempArr = []
    try:
        ff = open(cafeId+'.txt', 'r')
        lines = ff.readlines()
        for line in lines:
            diffArr += [line.strip()]
        ff.close()
    except:
        print('파일없음')
    f = open(cafeId+'.txt', 'w')
    while True:
        source_code = requests.get(fixTop+cafeId+fixBot+str(start), allow_redirects=False)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        print(str(start) + '페이지')
        for link in soup.findAll('td', {'class': 'p-nick'}):
            a = link.findAll('a')
            for i in a:
                temp = i.get('onclick').split(',')
                tempArr += [temp[1].replace("'",'').strip()]
                # print("아이디 : " + temp[1].replace("'",'').strip())
                # print("닉네임 : " + temp[3].replace("'",'').strip())
                # print('=' * 30)
        start += 1
        if start == endPage:
            tempArr += diffArr
            tempArr = list(set(tempArr))
            for i in tempArr: 
                f.write(i+'\n')
            f.close()
            break
        

trade_spider()