import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

browser= webdriver.Chrome()
browser.get("https://www.allhistory.com/painting?period=明代")
time.sleep(1)
js = "return action=document.body.scrollHeight"
height = 0
new_height = browser.execute_script(js)
while height < new_height:
    for i in range(height, new_height, 500):
        browser.execute_script('window.scrollTo(0, {})'.format(i))
        time.sleep(1)
    height = new_height
    time.sleep(2)
    new_height = browser.execute_script(js)
soup = BeautifulSoup(browser.page_source,'lxml')
browser.close()

opt=soup.find_all(attrs={'class':"image-element-class"})
pattern = re.compile(r'mid="(.*?)"')
result = pattern.findall(str(opt))
with open("save_ming_PID.csv", "w", newline='') as csvfile:
    for i in result:
        csvfile.write(i)
        csvfile.write('\n')
