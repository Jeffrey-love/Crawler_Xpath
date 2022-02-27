#! /user/bin.python
# -*- coding:UTF-8 -*-
import os
import requests
import random
from lxml import etree

# 自动寻找下一页
def next_page(html):
    next_url = html.xpath('//a[@class="next"]/@href')
    if next_url:
        next_url = "http://www.4399dmw.com" + next_url[0]
        return next_url
    else:
        return False

# 创建保存路径
def mk_dir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExist = os.path.exists(os.path.join('C:\pythonProject\python\pachong\dongman',path))
    if not isExist:
        print("--mkdir "+path)
        # 创建文件夹
        os.mkdir(os.path.join('C:\pythonProject\python\pachong\dongman',path))
        # 将路径转移到新建文件夹中，这样保存的图片就在这里
        os.chdir(os.path.join('C:\pythonProject\python\pachong\dongman',path))
        return True
    else:
        print(path+" already exists")
        os.chdir(os.path.join('C:\pythonProject\python\pachong\dongman', path))
        return True

# 下载图片
def save_img(img_url,img_name,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.{}.102 Safari/537.36".format(random.randint(1000,5000)),
        "Referer": url
    }
    proxies = {"HTTP": "http://58.20.234.243:9091"}
    try:
        img = requests.get(url=img_url,headers=headers,proxies=proxies)
        imgname = img_name+".jpg"
        with open(imgname,'ab') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)

def pachong(last_url,url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.{}.102 Safari/537.36".format(random.randint(1000,5000)),
        "Referer":last_url
    }
    proxies = {"HTTP": "http://58.20.234.243:9091"}
    print("---------------正在爬取"+url)
    resp = requests.get(url=url,headers=headers,proxies=proxies)
    html_doc = resp.content.decode("utf-8")
    # Xpath关键在于下面一步，使用etree分析源代码
    html = etree.HTML(html_doc)
    # 将页码提取出来作为文件夹名
    page = html.xpath('//span[@class="cur"]/text()')
    mk_dir("第" + page[0] + "页")
    # 会将标题下的文字提取出来并且保存为列表
    title = html.xpath('//a[@class="u-card"]/div[@class="u-ct"]/p[@class="u-tt"]/text()')
    # 将图片链接保存为列表：img_src
    img_src = html.xpath('//div[@class="lst"]/a[@class="u-card"]/img/@data-src')
    # 将每个链接前面加上http:
    img_url = list('http:'+item for item in img_src)
    print("--开始保存图片：")
    # 同时遍历两个列表的操作
    for nurl,ntitle in zip(img_url,title):
        save_img(nurl,ntitle,url)
    if next_page(html):
        pachong(url,next_page(html))
    else:
        print("--FINISH--无法找到下一页！")
        return False

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.{}.102 Safari/537.36".format(random.randint(1000,5000)),
        "Referer": "http://www.4399dmw.com/donghua/"
    }
    proxies = {"HTTP": "http://58.20.234.243:9091"}
    url = "http://www.4399dmw.com/search/dh-9-0-0-0-0-0-0/"
    # 这里要先完成第一页的爬虫操作，因为第一页的referer和后面的不同
    # try:
    print("------------正在爬取" + url)
    resp = requests.get(url=url, headers=headers, proxies=proxies)
    # except exception as e:
    #     print(e)
    #     return False
    html_doc = resp.content.decode("utf-8")
    html = etree.HTML(html_doc)
    # 将页码提取出来作为文件夹名
    page = html.xpath('//span[@class="cur"]/text()')
    mk_dir("第" + page[0] + "页")
    # 会将标题下的文字提取出来并且保存为列表
    title = html.xpath('//a[@class="u-card"]/div[@class="u-ct"]/p[@class="u-tt"]/text()')
    # 将图片链接保存为列表：img_src
    img_src = html.xpath('//div[@class="lst"]/a[@class="u-card"]/img/@data-src')
    # 将每个链接前面加上http:
    img_url = list('http:' + item for item in img_src)
    print("开始保存图片：")
    # 同时遍历两个列表的操作
    for nurl, ntitle in zip(img_url, title):
        save_img(nurl, ntitle,url)
    if next_page(html):
        pachong(url,next_page(html))
    else:
        print("无法找到下一页")
        return False

if __name__ == '__main__':
    main()