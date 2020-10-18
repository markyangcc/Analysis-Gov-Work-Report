# Analysis-Report-Gov-Work
利用Python爬取网站近年的政府工作报告，并进行简单的词频分析+词云

## 一、抓去gov.cn上政府工作报告网页内容
首先要做的就是把政府工作报告爬下来

参照 scrape.py 

## 二、利用jieba Lib 进行简单的词频分析

已经将政府工作报告的内容爬了下来，接下来利用中文分词库对报告进行词频分析，获得出现次数最高的词

参照 words_frequency_analysis.py


## 三、生成词云进行可视化

利用