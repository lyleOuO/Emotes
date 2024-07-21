# 适用于acfun,douyin

from bs4 import BeautifulSoup
import json

# 读取 HTML 文件
with open('emote.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取acfun所有的 li 标签
li_tags = soup.find_all('li')

# 提取douyin所有的 li 标签
#li_tags = soup.find_all('span')

# 构建存储图片和标题信息的列表
images = []
for li in li_tags:
    img_tag = li.find('img')
    if img_tag:
        images.append({
            'src': img_tag.get('src'),
            'alt': img_tag.get('alt'),
            'title': li.get('title', '')
        })

# 将列表转换为 JSON 格式
json_data = json.dumps(images, indent=4, ensure_ascii=False)

# 将 JSON 数据写入文件
with open('acfun.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print('JSON 文件生成成功：images_with_titles.json')