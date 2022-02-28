---
categories:
  - 知识积累
author: JeffreyLove
copyright: true
date: '2022/2/27 11:00:00'
description: 一个简单的爬虫程序
tags:
  - python
  - 爬虫
  - Xpath
---
# Crawler_Xpath  
### 使用Xpath模块编写的爬虫代码  
**基于上一篇发布的[使用BeautifulSoup的程序](https://github.com/Jeffrey-love/Crawler_BeautifulSoup)，这篇使用Xpath的功能更加完善，相比之下，增加了<u>自动翻页、请求头随机更改（为了避免同一User-Agent频繁访问）、Referer的自动更新</u>，还使用了一些python的实用语法，将在下面进行介绍**  :stuck_out_tongue_winking_eye:    

Xpath爬虫代码的基本逻辑没有什么变动，但是在处理网页源代码的部分做了一些改进。  
使用Xpath获取网页标签需要**使用科学的方法上网**，然后在扩展程序中安装Xpath Helper，这样一来可以方便自己查找标签，按住shift它还会自动帮你写出鼠标指针处的Xpath语法，非常的好用！  

用法就像下面这样  
我这里举了三个例子，但其实这些语法不是单一的，只要能够筛选到你想要的标签，都可以使用  
```python
    # Xpath关键在于下面一步，使用etree分析源代码
    html = etree.HTML(html_doc)
    # 将页码提取出来作为文件夹名
    page = html.xpath('//span[@class="cur"]/text()')
    mk_dir("第" + page[0] + "页")
    # 会将标题下的文字提取出来并且保存为列表
    title = html.xpath('//a[@class="u-card"]/div[@class="u-ct"]/p[@class="u-tt"]/text()')
    # 将图片链接保存为列表：img_src
    img_src = html.xpath('//div[@class="lst"]/a[@class="u-card"]/img/@data-src')
```

### 编写过程中遇到的比较实用的python语言  




under constructing~~~
