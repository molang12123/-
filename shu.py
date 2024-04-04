#怎么发送
import requests
#pip install lxml
from lxml import etree

# 发送给谁
url = 'https://www.51shucheng.net/wangluo/douluodalu/21750.html'

#发送请求
while True:

    # 伪装自己

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    resp = requests.get(url , headers= headers)
    #设置编码
    resp.encoding = 'utf-8'
    #响应信息
    # print(resp.text)

    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="neirong"]/p/text()'))
    title = '\n\n'.join(e.xpath('//h1/text()'))
    url = f"""https://www.51shucheng.net/wangluo/douluodalu{e.xpath("//div[@class='next']/a/@href")[0]}"""

    #保存

    with open('斗罗大陆.txt','w',encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')