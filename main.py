# -*- codeing = utf-8 -*-
# @Time : 2021/11/09
# @Author : richard
# @Software:PyCharm

import re
import requests
import pandas as pd


#自定义爬虫对象
def main():
    for i in range(0,1):
        print(i)
        url = url_list[i]
        cid = cid_list[i]

        dmurl = 'https://comment.bilibili.com/' + str(cid) + '.xml'
        print(dmurl)
        datalist = get_Html(dmurl)
        list = datalist.content.decode("utf-8")
        filename= filename_list[i]
        print(filename)
        savelist(list,filename)

        print('数据写入成功')


def get_html(url):         #一次请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }         #请个人的User-Agent
    response = requests.get(url, headers=headers)
    return response.text
def get_Html(url):        #二次请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }         #User-Agent
    response = requests.get(url, headers=headers)
    return response
def saveurl(baseurl):     #获取cid
    findlink=re.compile(r'"cid":(.*?),"bvid":')
    cid = re.findall(findlink,baseurl)
    cid = list(cid)[1]
    print(cid)

    return cid

def savelist(list,filename):

    danmu = re.compile(r'<d p=".*?">(.*?)</d>')
    filename1 = filename +'.txt'
    File = open(filename1, "w", encoding="utf-8")
    data = re.findall(danmu,list)
    for i in data:
        File.writelines(i)
        File.writelines("\n")
    File.close()





#爬虫对象
data = pd.read_csv("爬虫对象2.csv",encoding='gbk')
filename_list=data.values[0:1,0]#文件名
url_list=data.values[0:1,1]#链接
cid_list=data.values[0:1,2]



#执行

if __name__ =="__main__":
    main()

