import csv
import collections
import numpy as np
import pandas as pd

"""
进行词频统计，并去除停用词，输出一个数据文件
"""

def main():
    # 停用词表
    stopwords = [ line.rstrip() for line in open(r'./res/stopwords.txt', 'r', encoding = "utf-8" ).readlines () ]

    csv.field_size_limit(2147483647)
    #生成词袋库
    wf2 = csv.writer(open(r"./works/statistics.csv", 'w', newline='', encoding='utf-8_sig'))
    wf2.writerow(['no.','word','count'])

    #使用pd读取源文件
    data = pd.read_csv(r"./works/words_seg.csv")  
    print('词汇读取完毕')
    #源文件为一维数据，需要对data进行倒置处理,data.T
    train_data = np.array(data.T)
    #利用tolist()函数进行列表转化
    train_x_list=train_data.tolist()

    print('词汇入库，开始计数')
    #利用Counter函数进行字频快速统计
    all_words = collections.Counter(train_x_list[0])  
    print('计数处理完毕')
    #将class格式转化为dict格式
    all_words_dict = dict(all_words)
    print('字典转换完毕')
    word_dict_sort = sorted(all_words_dict.items(), key=lambda item: item[1], reverse=True) #排序
    print('排序转换完毕')

    # 写出数据文件
    num = 0
    for key in word_dict_sort:
        if key[0] not in stopwords:
            wf2.writerow([num, key[0], key[1]])  #写入文件
            num += 1
    print('统计了%d个词汇' %num)

if __name__ == "__main__":
    main()