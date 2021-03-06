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
**基于上一篇发布的[使用BeautifulSoup的程序](https://github.com/Jeffrey-love/Crawler_BeautifulSoup)，这篇使用Xpath的功能更加完善，相比之下，增加了自动翻页、请求头随机更改（为了避免同一User-Agent频繁访问）、Referer的自动更新，还使用了一些python的实用语法，将在下面进行介绍**  :stuck_out_tongue_winking_eye:    

Xpath爬虫代码的基本逻辑没有什么变动，但是在处理网页源代码的部分做了一些改进。  
使用Xpath获取网页标签需要**使用科学的方法上网**，然后在扩展程序中安装Xpath Helper，这样一来可以方便自己查找标签，按住shift它还会自动帮你写出鼠标指针处的Xpath语法，非常的好用！  
:blush:  
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
`img_url = list('http:'+item for item in img_src)`  遍历列表img_src，在每个成员前面加上http:并重新赋值给img_url    

`for nurl,ntitle in zip(img_url,title):`  
`   save_img(nurl,ntitle,url)`  
同时遍历两个列表，一句话就可以结束，足以体现python语言的优势:heart_eyes:
      
我们再来看看运行后的效果：  
<img src="https://github.com/Jeffrey-love/Crawler_Xpath/blob/main/Pictures/1.jpg" width = "500" height = "400" alt="" align=center />  
以下是使用Xpath实现寻找翻页的函数：  
```python
def next_page(html):
    next_url = html.xpath('//a[@class="next"]/@href')
    if next_url:
        next_url = "http://www.4399dmw.com" + next_url[0]
        return next_url
    else:
        return False
```  
  
这样的好处就是不需要自己看有多少页，程序会自己爬取直到找不到下一页，但是这里又出现一个问题，如果一些网站使用了**懒加载**的技术，那么程序加载页面一开始是找不到class值为next的a标签的，这个时候就需要用到其它技术了，我会在下一篇中分享。    
Thanks for reading！:heartpulse:  
