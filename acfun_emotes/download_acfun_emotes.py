import json
import re
import os
import requests

# JSON 文件路径
json_file = './acfun_emotes/AC娘.json'

# 创建存储图片的文件夹，以 JSON 文件名命名
folder_name = os.path.splitext(os.path.basename(json_file))[0]  # 获取 JSON 文件名（不带扩展名）
folder_path = f'./acfun_emotes/{folder_name}/'

# 创建文件夹，如果不存在
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 打开并读取 JSON 文件
with open(json_file, 'r', encoding='utf-8') as file:
    images_data = json.load(file)

# 遍历每个图片条目
for image_info in images_data:
    src = image_info['src']
    title = image_info['title']
    
    # 下载图片
    response = requests.get(src)
    if response.status_code == 200:
        # 获取图片内容
        image_content = response.content
        
        # 清理和规范化文件名
        cleaned_title = re.sub(r'[\\/:"*?<>|]', '', title)  # 移除不支持的特殊字符
        cleaned_title = cleaned_title[:100]  # 限制文件名长度
        
        # 写入到文件，以 cleaned_title 作为文件名
        filename = os.path.join(folder_path, f"{cleaned_title}.png")  # 假设图片格式为 png
        with open(filename, 'wb') as img_file:
            img_file.write(image_content)
        
        print(f"图片 '{filename}' 下载完成")
    else:
        print(f"无法下载图片：{src}")

print("所有图片下载完成")
