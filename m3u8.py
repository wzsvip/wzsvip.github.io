import requests
from bs4 import BeautifulSoup
import re

# 读取list.txt文件
with open('list.txt', 'r') as f:
    lines = f.readlines()

# 解析名称和URL链接
name_url_pairs = []
for line in lines:
    name, url = line.strip().split()
    name_url_pairs.append((name, url))

# 访问链接并获取带有.m3u8后缀的媒体资源链接
media_links = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.3029.110 Safari/537.3'}
for name, url in name_url_pairs:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    m3u8_links = [link['href'] for link in soup.find_all('a', href=re.compile(r'\.m3u8$'))]
    media_links.extend([(name, m3u8_link) for m3u8_link in m3u8_links])

# 按名称顺序保存结果到wz.txt文件中
with open('wz.txt', 'w') as f:
    for name, m3u8_link in sorted(media_links):
        f.write(f'{name},{m3u8_link}
')