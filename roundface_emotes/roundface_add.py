import json

# 读取 JSON 文件
with open('roundface_emotes/roundface_add.json', 'r', encoding='utf-8') as file:
    images = json.load(file)

# 更新每个图片对象的 src 属性
for image in images:
    image['src'] = 'https://bbs.north-plus.net/' + image['src']

# 将更新后的列表重新写入 JSON 文件
with open('小圆脸.json', 'w', encoding='utf-8') as file:
    json.dump(images, file, indent=4, ensure_ascii=False)

print('JSON 文件更新成功：小圆脸.json')
