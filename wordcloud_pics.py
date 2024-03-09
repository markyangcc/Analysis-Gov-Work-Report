import jieba
import wordcloud
from matplotlib.pyplot import imread
import os

# 创建文件夹存储报告
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'wordcloudpics')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)


for year in range(2014, 2023+1):

    mask = imread("China.jpg")
    f = open(f"./reports/{year}_gov_report.txt", "r", encoding="utf-8")

    # 忽略掉不符合的语气词，连接词
    excludes = {"和","的","要","是","在"}

    t = f.read()
    f.close()
    ls = jieba.lcut(t)  # 使用精确分词模式进行分词
    txt = " ".join(ls)  # 利用空格连接精确分词后的词语

    # 设置字体,否则汉字会变为全是方框框，显示不出来
    # 分别选择了 Ubuntu/Windows/MacOS 的一种字体
    fonts = [
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        'C:/Windows/Fonts/simhei.ttf',
        '/System/Library/fonts/PingFang.ttc'
    ]

    # 如果所有路径都不存在，`font` 将会是 `None`
    font = next((path for path in fonts if os.path.exists(path)), None)

    w = wordcloud.WordCloud(
        width=1000,  # 设置图片宽度
        height=700,  # 设置图片高度
        background_color="white",  # 设置图片背景颜色
        font_path=font,  # 指定字体文件的完整路径，如果不设置可能显示不了中文
        max_words=100,  # 词云中最大词数
        max_font_size=80,  # 词云中最大的字体号数
        mask=mask,  # 使用遮照
        stopwords=excludes  # 被排除的词列表
    )
    w.generate(txt)

    
    # 生成图片写入文件夹内
    w.to_file(f"{final_directory}/{year}政府工作报告词云.png")
