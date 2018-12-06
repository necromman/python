import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time



plancodein = []
com_name = 0
compin = ['SKT', 'KT', 'LGU']
Allservice = []
SKTservice = ['PHONE_LTE', 'PHONE_3G', 'PHONE_feature', 'TABLET', 'ETC']
KTservice = ['PHONE_LTE', 'PHONE_3G', 'TABLET_LTE', 'TABLET_3G', 'ETC_LTE_egg', 'ETC']
LGUservice = ['PHONE_LTE', 'PHONE_feature', 'TABLET', 'ETC']
home = 'http://www.smartchoice.or.kr/smc/smartlife/dantongTelList.do?'
fixto = 'searchType=danTelSearch&searchOrder=orderASC&p_Group=&dan_Service=&p_Group2=&dan_Service2=&'
company = 0
plans = 0
II = 0
plancode = 'dan_Plan_Code='
fixbo = '&dan_Mau=all&productName=all'
wb = 0
ws = 0


def trade_spider():
    global wb
    global ws
    global Allservice
    global plancodein
    global plans
    global com_name
    global compin
    global company
    global II
    j = 0
    for i in compin:
        if j == 0:
            company = 'dan_Company=' + compin[0] + '&'
            com_name = compin[0]
            Allservice = SKTservice
        elif j == 1:
            company = 'dan_Company=' + compin[1] + '&'
            com_name = compin[1]
            Allservice = KTservice
        elif j == 2:
            company = 'dan_Company=' + compin[2] + '&'
            com_name = compin[2]
            Allservice = LGUservice

        wb = Workbook()

        for II in Allservice:
            if j == 0:
                plans = 'planSKTService=' + II + '&planKTService=&planLGUService=&'
            elif j == 1:
                plans = 'planSKTService=&planKTService=' + II + '&planLGUService=&'
            elif j == 2:
                plans = 'planSKTService=&planKTService=&planLGUService=' + II + '&'

            source_code = requests.get(home + fixto + company + plans + plancode + fixbo, allow_redirects=False)
            source_code.encoding = 'utf-8'
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, 'html.parser')
            for link in soup.findAll('select', {'id': 'dan_Plan_Code'}):
                option = link.findAll('option')
                for t in option:
                    if t['value']:
                        plancodein += [t['value']]
            
            
            
            ws = wb.create_sheet(com_name + '-' + II)
            ws.append(['idx','단말기명', '제조사', '모델명', '요금제', '출고가', '지원금', '판매가', '공시일자'])
            trade_spider2()
            plancodein = []
        j += 1


def trade_spider2():
    temp = int(len(plancodein))
    idx = 1
    for i in plancodein:
        print(com_name + '-' + II + '-' + i + '진행...')
        print(temp)
        plancode = 'dan_Plan_Code=' + i
        source_code = requests.get(home + fixto + company + plans + plancode + fixbo, allow_redirects=False)
        source_code.encoding = 'utf-8'
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('tr', {'class': 'dan'}):
            th = link.findAll('th')
            for i in th:
                xlTemp = []
                xlTemp += [idx]
                xlTemp += [i.text]
                td = link.findAll('td')
                idx += 1
                for i in td:
                    xlTemp += [i.text]
                ws.append(xlTemp)
        temp -= 1
    wb.save(com_name + '.xlsx')
    print(com_name + '-' + II + '완료')
    print("60초 후에 다시 시작 됩니다.")
    time.sleep(60)

trade_spider()