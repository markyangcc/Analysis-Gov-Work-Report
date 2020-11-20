# Analysis-Report-Gov-Work
利用Python爬取网站近年的政府工作报告，并进行**简单的词频分析+词云**
<br></br>


文中**使用的路径均为相对路径，字体采用的是绝对路径**。所以可以直接运行 .py 文件而不需要考虑路径问题。

如果是Windows平台，字体路径需要手动更改，指定宋体或者黑体等能够显示完整中文的即可。

## 一、抓去gov.cn上政府工作报告网页内容
首先要做的就是把政府工作报告爬下来

参照 scrape.py 

运行后，会在相同目录下生成一个 reports 文件夹，里面存放着爬去的政府工作报告

![](https://gitee.com/gsyang/Image-Hosting/raw/master/img/scrape_gov_report_example.png)


### 如果没有安装 bs4 库，使用下列命令安装
```
pip install beautifulsoup4
```

## 二、利用jieba Lib 进行简单的词频分析

已经将政府工作报告的内容爬了下来，接下来利用中文分词库对报告进行词频分析，获得出现次数最高的词
参照 words_frequency_analysis.py

运行后，会在相同目录下生成一个 2014-2020_reports_analysis.txt 文件，里面写入了历年政府工作报告的词频分析结果

![](https://gitee.com/gsyang/Image-Hosting/raw/master/img/gov_report_wordcount_example.png)

### 如果没有安装 jieba 库，使用下列命令安装

```
pip install jieba
```
如果从国外拉取资源失败，那么就从国内镜像源拉，比如从阿里云镜像拉,

```
pip install jieba -i https://mirrors.aliyun.com/pypi/simple
```

## 三、生成词云进行可视化

利用 wordcloud 生成词云进行可视化展示，让结果更加生动。

参照 wordcloud_display_mask.py

文件夹里面的图片 China.jpg 是使用遮照时候使用的,去除遮照效果也是一样的

运行后，会在相同目录下生成一个 wordcloudpics 文件夹，里面存放着历年的词云图片

![](https://gitee.com/gsyang/Image-Hosting/raw/master/img/wordcloudpics_gov_report_example.png)

### 如果没有安装 wordcloud库，使用下列命令安装
```
pip install wordcloud
```

如果从国外拉速度太慢，就从国内镜像拉,例如

```
pip install wordcloud -i https://mirrors.aliyun.com/pypi/simple
```
