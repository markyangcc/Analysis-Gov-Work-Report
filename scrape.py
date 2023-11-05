import os
import requests
import lxml
from bs4 import BeautifulSoup

# 创建文件夹 reports 存储报告
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'reports')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)


# 2014-2020
for year in range(2014, 2020+1):

    res = requests.get(f'http://www.gov.cn/guowuyuan/{year}zfgzbg.htm')  # 请求网页
    res.encoding = 'utf-8'  # 必须指定编码否则乱码
    soup = BeautifulSoup(res.text, 'lxml')

    # 获取报告正文，位于 conlun2_box_text class里面
    p_tags = soup.select('#conlun2_box_text')
    for p in p_tags:
        text = p.text

    # 爬取内容保存到文件夹中
    with open(f'{final_directory}/{year}_gov_report.txt', 'w') as f:
        f.write(str(text))

# 2021-2023+
for year in range(2021, 2023+1):
    res = requests.get(f'https://www.gov.cn/zhuanti/{year}lhzfgzbg/index.htm')  # 请求网页
    res.encoding = 'utf-8'  # 必须指定编码否则乱码
    soup = BeautifulSoup(res.text, 'lxml')

    # 获取报告正文，位于 zfgzbg class里面
    p_tags = soup.select('#zfgzbg > div > div.zhj-report-right.fr.bd > ul.addScroll.zhj-bgqw')
    for p in p_tags:
        text = p.text

    # 爬取内容保存到文件夹中
    with open(f'{final_directory}/{year}_gov_report.txt', 'w') as f:
        f.write(str(text))
