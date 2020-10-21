import requests
from selenium import webdriver
import pandas as pd
import time
import os
import csv
f = open('save_ming_PID.csv')
L=list(csv.reader(f))
browser = webdriver.Chrome()
browser.implicitly_wait(3)
PaintingInfos=[]
ImgUrls=[]
for i in range(1000):
        url='https://www.allhistory.com/painting/detail?paintingType=all&paintingId='+str(L[i][0])+'&pageNum='+str(int(i/40+1))+'&period=%E6%98%8E%E4%BB%A3'
        browser.get(url)
        try:
            title=browser.find_element_by_xpath('//*[@id="painting-detail-content"]/div/div[2]/div/div[1]/div/div[1]/div[1]/h2').text
        except:
            title=''
        try:
            PanitingInformation=browser.find_element_by_xpath('//*[@id="painting-detail-content"]/div/div[2]/div/div[1]/div/div[2]/div[2]/table').text.replace('\n',' ')
        except:
            PanitingInformation=''
        try:
            Tags=browser.find_element_by_xpath('//*[@id="painting-detail-content"]/div/div[2]/div/div[2]/div/div[1]/div[2]/div').text.replace('\n',' ')
        except:
            Tags=''
        try:
            Desc=browser.find_element_by_xpath('//*[@id="painting-detail-content"]/div/div[2]/div/div[1]/div/div[3]/div[2]/p').text
        except:
            Desc=''
        PaintingInfo={'名称':title,'图画信息':PanitingInformation,'图画标签':Tags,'图片信息':Desc}
        try:
            imgurl=browser.find_element_by_xpath('//*[@id="painting-detail-content"]/div/div[1]/div/div[2]/div[3]/img').get_attribute('src')
        except:
            imgurl=''
        PaintingInfos.append(PaintingInfo)
        ImgUrls.append(imgurl)

paintingInfos= pd.DataFrame(PaintingInfos)
paintingInfos.to_csv('paintingInfos.csv')

with open("save_ming_Purl.csv", "w", newline='') as csvfile:
    for i in ImgUrls:
        csvfile.write(i)
        csvfile.write('\n')



