# -*- coding: UTF-8 -*-

import json
import requests
from bs4 import BeautifulSoup
import time
import re


path = 'https://porn87.com/main/all_models'
data = {}
arr_list = list()
r = requests.get(path)
base_url = 'https://porn87.com'


def secondLayerCrawler(video_list,url):
    url_2 = base_url+url
    request_2 = requests.get(url_2)
    if request_2.status_code == requests.codes.ok:
        soup = BeautifulSoup(request_2.text, 'html.parser')
        porns = soup.find_all('div', class_='column column-block')
        
    
    for porn in porns :
        video = {}
        video['actress'] = url.replace('/main/search?name=','')
        video['video'] = base_url+porn.div.a['href']
        video['img'] = porn.div.a.img['src']
        video['name'] = porn.div.span.getText()
        video_list.append(video)
    # print(video_list)
    return video_list

    # print(porns)
    # pornList = soup.findAll('div',class_='columns small-12')


def writeFile (video_data) :
    fo = open("video.json", "w")
    fo.write( json.dumps(video_data) )
    fo.close()
    


if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    pornList = soup.findAll('div', class_='columns small-12')
    a = list()

    for porn in pornList:
        # data[porn.find('a')['href'].replace("/main/search?name=", "")] = porn.find('a')['href']
        # print(porn.find('a')['href'].replace("/main/search?name=", ""))
        # data[porn.getText()] = porn.find('a')['href']
        arr_list.append(porn.find('a')['href']) 
    
    for index, url in enumerate(arr_list, start=0):
        if index != 0 :
            a = secondLayerCrawler(a,url)


    writeFile(a)

    print('crawler success!!!')







