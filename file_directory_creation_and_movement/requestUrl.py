

"""
实现内容：
实现了将微信公众号当中的网页中的符合要求的网页链接爬取下来
并且存入到txt文件当中
"""
from bs4 import BeautifulSoup#用于解析网页
import requests


url='https://mp.weixin.qq.com/s/ZqLPc2ja72qyfV2n-0mYSA'
web_data = requests.get(url)
soup=BeautifulSoup(web_data.text,'lxml')
#links = soup.select('#js_content > section:nth-of-type(10) a')
links_file=open('G:/Desktop/link.txt','a')
print("begin!")
for i in range(1,11):
    links = soup.select('#js_content > section:nth-of-type('+str(i)+') a')
    for href in links:
        b = href.text
        c = href.attrs['href']
        #print(b)
        #print(c)
        result=c+"\n"
        links_file.write(result)

links_file.close()
print("Done!")

