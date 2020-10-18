import jieba
import wordcloud
from matplotlib.pyplot import imread


for year in range(2014, 2020+1):

    mask = imread("China.jpg")
    f = open(f"./reports/{year}_gov_report.txt", "r", encoding="utf-8")

    # 忽略掉不符合的词
    excludes = {"div", "h5", "class", "h4", "h3",
                "h2", "h1", "conlun2_box_text", "p", "id", "span"}

    t = f.read()
    f.close()
    ls = jieba.lcut(t)  # 使用精确分词模式进行分词
    txt = " ".join(ls)  # 利用空格连接精确分词后的词语

    # 设置字体,否则汉字会变为全是方框框，显示不出来
    font = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

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
    w.to_file(f"{year}政府工作报告词云.png")
