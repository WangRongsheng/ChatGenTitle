import urllib.request
import feedparser
from datetime import datetime
import json
import time

# 获取Arxiv每日更新的人工智能和计算机视觉分类的文章
url1 = "http://export.arxiv.org/rss/cs.AI"  # 人工智能分类RSS源
url2 = "http://export.arxiv.org/rss/cs.CV"  # 计算机视觉分类RSS源
urls = [url1, url2]

# 数据源
data = []

# 开始计时
start_time = time.time()

# 遍历每个RSS源，获取文章信息
for url in urls:
    response = urllib.request.urlopen(url)
    rss = response.read()
    feed = feedparser.parse(rss)
    
    # 遍历每个文章，输出标题、摘要和作者信息
    for entry in feed.entries:
        #print('Title: %s' % entry.title)
        #print('Abstract: %s' % entry.summary)
        #print('\n')
        summary = entry.summary.replace('\n', '').replace('</p>', '').replace('<p>', '')
        title = entry.title.replace('(arXiv:'+ entry.title.split('(arXiv:')[1].split(')')[0] + ')', '').strip()
        info = {
               "instruction": "If you are an expert in writing papers, please generate a good paper title for this paper based on other authors' descriptions of their abstracts.",
               "input": str(summary),
               "output": str(title)
                    }
        data.append(info)

# 结束计时
end_time = time.time()

# 获取当前日期
today = datetime.today().date()

# 保存json
with open('data/'+str(today)+'.json', 'w+') as f:
    json.dump(data, f)

# 打印处理时间
print('处理完成，共获取%s篇文章，用时：%.2f秒。' % (len(data), end_time - start_time))

# 处理完成，共获取371篇文章，用时：6.89秒。