# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import re


while(1):
    try:
        covid19 = BeautifulSoup(requests.get("https://covid19.saglik.gov.tr/", timeout=5).content,"html.parser")
        date = covid19.find('div', class_=['takvim']).find_all('p')
        gununtarihieski = date[0].text + " " + date[1].text + " " + date[2].text
        break
    except:
        time.sleep(0.1)

time.sleep(185)

while(1):
    try:
        covid19 = BeautifulSoup(requests.get("https://covid19.saglik.gov.tr/", timeout=5).content,"html.parser")
        date = covid19.find('div', class_=['takvim']).find_all('p')
        gununtarihiyeni = date[0].text + " " + date[1].text + " " + date[2].text
        break
    except:
        time.sleep(0.1)

todayTEST = covid19.find_all('li', class_=['baslik-k-2', 'bg-acik'])
totalTEST = covid19.find_all('li', class_=['baslik-k'])

if gununtarihiyeni != gununtarihieski:
    users = ["1"]

    totalList = [str(re.search(r'\d+', totalTEST[0].find_all('span')[-1].text.replace(".","")).group(0)),
             str(re.search(r'\d+', totalTEST[1].find_all('span')[-1].text.replace(".","")).group(0)),
             str(re.search(r'\d+', totalTEST[2].find_all('span')[-1].text.replace(".","")).group(0)),
             str(re.search(r'\d+', totalTEST[3].find_all('span')[-1].text.replace(".","")).group(0)),
             str(re.search(r'\d+', totalTEST[4].find_all('span')[-1].text.replace(".","")).group(0)),
             str(re.search(r'\d+', totalTEST[5].find_all('span')[-1].text.replace(".","")).group(0))
             ]
    
    todayList = [str(re.search(r'\d+', todayTEST[0].text.replace(".","")).group(0)),
                str(re.search(r'\d+', todayTEST[1].text.replace(".","")).group(0)),
                str(re.search(r'\d+', todayTEST[2].text.replace(".","")).group(0))
                ]

    totalvakayuzde = format(int(totalList[1])/int(totalList[0]), '0.4f')
    todayvakayuzde = format(int(todayList[1])/int(todayList[0]), '0.4f')
    totaldeathrate = format(int(totalList[2])/int(totalList[1]), '0.4f')


    sep = "\n---------------------\n"
    msg2= "Test başına vaka: " + totalvakayuzde + "\nBugün test başına vaka: " + todayvakayuzde + "\nÖlüm oranı: " + totaldeathrate
    
    msg1 = "Yapılan test: " + totalList[0] + "\n" + "Vaka sayısı: " + totalList[1] + "\nÖlü sayısı: " + totalList[2] + "\nYoğun Bakım: " + totalList[3] + "\nEntübe: " + totalList[4] + "\nİyileşen Sayısı: " + totalList[5]                            
    msgsum = "https://covid19.saglik.gov.tr" + sep + gununtarihiyeni + "\nYapılan test: " + todayList[0] + "\nVaka sayısı: " + todayList[1] + "\nÖlü sayısı: " + todayList[2] + sep + "TOPLAM \n" + msg1 + sep + msg2
    
    for user in users:
        url = "https://api.telegram.org/botAPI/sendMessage?text="+str(msgsum)+"&chat_id=" + str(user)
        r = requests.get(url)
        time.sleep(0.1)
else:
    print("same")
