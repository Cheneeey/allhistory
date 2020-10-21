import os
import requests
import csv

f = open('save_ming_Purl.csv')
ImgUrls=list(csv.reader(f))
print(ImgUrls)
print(ImgUrls[1][0])

f = open('paintingInfos.csv')
PaintingInfos=list(csv.reader(f))


for i in range(0,1000):
    if 'MingPaintCollection' in os.listdir(r'/Users/zhangqian/PycharmProjects/allhistory'):
        pass
    else:
        os.mkdir('MingPaintCollection')
    os.chdir(r'/Users/zhangqian/PycharmProjects/allhistory/MingPaintCollection')
    try:
        img=requests.get(ImgUrls[i][0]).content
        with open(PaintingInfos[i+1][1].replace('/','')+'.jpg', 'wb') as f:
            print('正在下载： %s'%ImgUrls[i][0])
            f.write(img)
    except:
        print(PaintingInfos[i][1].replace('/','')+'.jpg not found.')

