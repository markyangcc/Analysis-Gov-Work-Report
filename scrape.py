import os
import requests
from bs4 import BeautifulSoup

for year in range(2014, 2020+1):

    res = requests.get(f'http://www.gov.cn/guowuyuan/{year}zfgzbg.htm')  # 请求网页
    res.encoding = 'utf-8'  # 必须指定编码否则乱码
    soup = BeautifulSoup(res.text, 'lxml')

    # 获取报告正文，位于conlun2_box_text class里面
    text = soup.select('.conlun2_box_text')

    # 创建文件夹存储报告
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'reports')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    # 爬去内容保存到文件夹中
    with open(f'{final_directory}/{year}_gov_report.txt', 'w') as f:
        f.write(str(text))
