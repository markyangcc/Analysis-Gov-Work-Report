# Analysis-Gov-Work-Report
利用Python爬取网站近年的政府工作报告，并进行**简单的词频分析+词云**

文中**使用的路径均为相对路径，字体采用的是绝对路径**。所以可以直接运行 .py 文件而不需要考虑路径问题。

## 一、抓取 gov.cn上政府工作报告网页内容
首先要做的就是把政府工作报告爬下来,

```shell
python3 scrape.py
```

运行后，会在当前目录下生成一个 reports 文件夹，里面存放着爬取的政府工作报告

注: 如果没有安装 bs4 库，使用下列命令安装,
```shell
pip install lxml
pip install beautifulsoup4

# 如果从国外拉取资源失败，那么就从国内镜像源拉，比如从阿里云镜像拉,
pip install lxml -i https://mirrors.aliyun.com/pypi/simple
pip install beautifulsoup4 -i https://mirrors.aliyun.com/pypi/simple
```

## 二、利用 jieba Lib 进行简单的词频分析

已经将政府工作报告的内容爬了下来，接下来利用中文分词库对报告进行词频分析，获得出现次数最高的词
```shell
python3  words_frequency.py
```

运行后，会在相同目录下生成一个 gov_work_reports_analysis.txt 文件，里面写入了历年政府工作报告的词频分析结果

注：如果没有安装 jieba 库，使用下列命令安装

```shell
pip install jieba

# 如果从国外拉取资源失败，那么就从国内镜像源拉，比如从阿里云镜像拉,
pip install jieba -i https://mirrors.aliyun.com/pypi/simple
```

## 三、生成词云进行可视化

利用 wordcloud 将词频转化为词云进行可视化展示，图片会比文字更有说服力。
```shell
python3  wordcloud_pics.py
```

运行后，会在相同目录下生成一个 wordcloudpics 文件夹，里面存放着历年的词云图片

注：文件夹里面的图片 China.jpg 是生成词云图片的地底图，换任何一张图片均可

注：如果没有安装 wordcloud库，使用下列命令安装
```shell
pip install wordcloud

# 如果从国外拉取资源失败，那么就从国内镜像源拉，比如从阿里云镜像拉,
pip install wordcloud -i https://mirrors.aliyun.com/pypi/simple
```
