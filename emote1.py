# 适用于 bilibili,weibo,roundface

from bs4 import BeautifulSoup
import json

# 读取 HTML 文件
with open('emote.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取所有的 img 标签
img_tags = soup.find_all('img')

# 构建存储图片信息的列表
images = []
for img in img_tags:
    images.append({
        'src': img.get('src'),
        'alt': img.get('alt', '')
    })

# 将列表转换为 JSON 格式
json_data = json.dumps(images, indent=4, ensure_ascii=False)

# 将 JSON 数据写入文件
with open('images.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print('JSON 文件生成成功：images.json')
