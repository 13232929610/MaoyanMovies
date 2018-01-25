#! C:\Python36\python.exe
# coding:utf-8
import json
import re
from multiprocessing.pool import Pool

import requests
from requests import RequestException

# 打开一个网页
def getOnePage(url):
    try:
        response=requests.get(url)
        if response.status_code==200: # 判断是否访问成功
            return response.text
        return None
    except RequestException:
        return None

def parseOnePage(html):
    # 正则匹配重要信息
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    # print(items)
    # 以字典形式返回
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6],
        }

# 写入到文件中
def writeToFile(content):
    with open('../doc/movies.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")


# 主程序
def main(offset):
    url="http://maoyan.com/board/4?offset="+str(offset)
    html=getOnePage(url)
    # print(html)
    for item in parseOnePage(html):
        print(item)
        writeToFile(item)

if __name__ == "__main__":
    # for i in range(10):
    #     main(i*10)
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])