import requests
import re
from bs4 import BeautifulSoup
def getIp(tel):
    url = "http://m.ip138.com/mobile.asp?mobile="
    try:
        r = requests.get(url+tel)
        r.raise_for_status()  #状态码为200，表示连接成功，否则失败
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ("爬取失败！")
if __name__ == "__main__":
    tel = input(u'请输入要查询的电话号码：')
    #print (getIp(tel))
    print ("查找结果如下：")
    soup = BeautifulSoup(getIp(tel), "html.parser")
    a = soup.find('table')
    for k in a.find_all('td'):
        print (k.string)
