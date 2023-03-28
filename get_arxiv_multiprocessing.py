import urllib.request
import feedparser
from datetime import datetime
import json
from multiprocessing import Pool
import time
import re

def get_article_info(url):
    response = urllib.request.urlopen(url)
    rss = response.read()
    feed = feedparser.parse(rss)
    data = []
    # 遍历每个文章，输出标题、摘要和作者信息
    for entry in feed.entries:
        summary = entry.summary.replace('\n', '').replace('</p>', '').replace('<p>', '').replace('\\', '')
        summary = re.sub(r'http\S+', '', summary)
        title = entry.title.replace('(arXiv:'+ entry.title.split('(arXiv:')[1].split(')')[0] + ')', '').strip()
        info = {
               "instruction": "If you are an expert in writing papers, please generate a good paper title for this paper based on other authors' descriptions of their abstracts.",
               "input": str(summary),
               "output": str(title)
                    }
        data.append(info)
    return data

if __name__ == '__main__':
    # 获取Arxiv每日更新的人工智能和计算机视觉分类的文章
    url1 = "http://export.arxiv.org/rss/cs.AI"  # 人工智能分类RSS源
    url2 = "http://export.arxiv.org/rss/cs.CV"  # 计算机视觉分类RSS源
    urls = [url1, url2]

    # 数据源
    data = []
    
     # 开始计时
    start = time.time()

    # 使用多线程获取文章信息
    with Pool(4) as p:
        data = p.map(get_article_info, urls)
    # 将多个列表合并为一个列表
    data = [info for subdata in data for info in subdata]

    # 获取当前日期
    today = datetime.today().date()

    # 保存json
    with open('data/'+str(today)+'.json', 'w+') as f:
        json.dump(data, f)
    
    # 结束计时并输出用时
    end = time.time()
    print('共处理了%s篇文章，用时%.2f秒' % (len(data), end-start))
    
    # 共处理了371篇文章，用时4.51秒