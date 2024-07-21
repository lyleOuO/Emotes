# 如果拓展名为空或者是 avif 格式，使用 .png
import json
import os
import re
import requests
from urllib.parse import urlparse

# JSON 文件路径
json_file = './bilibili_emotes/biliblili_test2.json'

# 创建存储图片的文件夹，以 JSON 文件名命名
folder_name = os.path.splitext(os.path.basename(json_file))[0]  # 获取 JSON 文件名（不带扩展名）
folder_path = f'./bilibili_emotes/{folder_name}/'

# 创建文件夹，如果不存在
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 打开并读取 JSON 文件
with open(json_file, 'r', encoding='utf-8') as file:
    images_data = json.load(file)

# 遍历每个图片条目
for index, image_info in enumerate(images_data):
    src = image_info['src']
    alt = image_info.get('alt', '')  # 获取 alt 字段，如果不存在则为空字符串
    title = image_info.get('title', '')  # 获取 title 字段，如果不存在则为空字符串
    
    # 确定文件名
    if alt or title:  # 如果 alt 或 title 字段不为空
        filename = alt or title
    else:  # 如果 alt 和 title 都为空，则使用 JSON 文件名加上序号
        filename = f"{folder_name}_{index}"
    
    # 下载图片
    response = requests.get(src)
    if response.status_code == 200:
        # 获取图片内容
        image_content = response.content
        
        # 解析 src 链接，尝试获取文件名和拓展名
        parsed_url = urlparse(src)
        path = parsed_url.path
        filename_from_src = os.path.basename(path)
        _, ext = os.path.splitext(filename_from_src)
        
        # 如果无法从 src 链接获取有效的拓展名，使用默认的 .png
        if not ext or ext == '.avif':  # 如果拓展名为空或者是 avif 格式，使用 .png
            ext = '.png'
        
        # 清理和规范化文件名
        cleaned_filename = re.sub(r'[\\/:"*?<>|]', '', filename)  # 移除不支持的特殊字符
        cleaned_filename = cleaned_filename[:100]  # 限制文件名长度
        
        # 写入到文件，以 cleaned_filename 和拓展名 .png 作为文件名
        filename_to_save = os.path.join(folder_path, f"{cleaned_filename}{ext}")
        with open(filename_to_save, 'wb') as img_file:
            img_file.write(image_content)
        
        print(f"图片 '{filename_to_save}' 下载完成")
    else:
        print(f"无法下载图片：{src}")

print("所有图片下载完成")
