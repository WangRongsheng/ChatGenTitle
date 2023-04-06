import requests
import xml.etree.ElementTree as ET

base_url = "http://export.arxiv.org/api/query?"
search_query = "large+language+models"
start = 0
max_results = 30

query = f"search_query=all:{search_query}&start={start}&max_results={max_results}"

url = base_url + query

response = requests.get(url)

if response.status_code == 200:
    print("获取论文成功！")

    # 解析XML响应
    root = ET.fromstring(response.text)

    # 打开用于保存结果的Markdown文件
    with open("LLMs-papers.md", "w+", encoding="utf-8") as md_file:
        print("读取成功")
        # 提取每篇论文的链接和标题
        c = 1
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            title = entry.find('{http://www.w3.org/2005/Atom}title').text

            # 将标题和链接写入Markdown文件
            md_file.write(str(c)+f". [{title}]({link})\n")
            c = c+1

        print("论文信息已保存到papers.md文件！")

else:
    print("获取论文失败")
