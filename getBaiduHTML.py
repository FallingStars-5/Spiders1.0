import requests #引入requests库
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}#浏览器身份标识链接
        r = requests.get(url,headers=kv,timeout=30) #timeout为超时时间30秒
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding=r.apparent_encoding 
        return r.text
    except:
        return "产生异常"
if __name__ == "__main__":
    #url="http://www.baidu.com/robots.txt"
    #robots协议
    url = "https://www.baidu.com/"
    print (getHTMLText(url))  
