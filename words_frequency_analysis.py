import os
import jieba
import jieba.analyse
import codecs
import re
from collections import Counter


class WordCounter(object):

    def count_from_file(self, file, top_limit=0):
        with codecs.open(file, 'r', 'utf-8') as f:
            content = f.read()
            content = re.sub(r'\s+', r' ', content)
            content = re.sub(r'\.+', r' ', content)
            return self.count_from_str(content, top_limit=top_limit)

    def count_from_str(self, content, top_limit=0):
        if top_limit <= 0:
            top_limit = 100
        tags = jieba.analyse.extract_tags(content, topK=100)

        words = jieba.cut(content)
        counter = Counter()
        for word in words:
            if word in tags:
                counter[word] += 1

        return counter.most_common(top_limit)


# Drive Program
if __name__ == '__main__':

    counter = WordCounter()

    # 遍历文件夹为爬去下来的每个文件生成一份词频统计报告
    g = os.walk(r'./reports')

    for path, dicrt, files in g:
        for file_name in files:

            full_path = os.path.join(path, file_name)

            result = counter.count_from_file(full_path, top_limit=10)

            # 将分析报告写入 .txt 文件中
            output_file = '2014-2020_reports_analysis.txt'
            with open(output_file, "a") as f:
                f.write(str(file_name) + '统计：'+'\n\n')
            for i, j in result:
                with open(output_file, "a") as f:
                    f.write(str(i)+'\t'+str(j)+'\n')

            with open(output_file, "a") as f:
                f.write('\n')
