import re
import csv
import jieba

"""
对消息记录 csv 文件分词并滤除非中文字符，输出结果也为 csv 数据文件
"""

# 正则匹配字符串中的中文
def find_chinese(text):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', text)
    if chinese:
        return chinese
    else:
        return None


def main(mode):
    seg_list = []

    # 读取 data2csv 生成的 csv ，并使用 jieba 进行切分
    with open(r'./works/messages.csv', 'r', encoding = 'utf-8_sig') as fp:
        reader = csv.reader(fp)
        new_list = [row[1] for row in reader]
        del new_list[0]
        
        for item in new_list:
            gene = jieba.cut(item, cut_all=False)
            for seg_item in gene:
                seg_list.append(seg_item)

    # 在切分之后，提取其中的中文字符串，并生成词表，也存为 csv 文件
    with open(r'./works/words_seg.csv', 'w', encoding = 'utf-8_sig', newline = '') as fp:
        writer = csv.writer(fp)

        if mode == 'char':
            for item in seg_list:
                string = find_chinese(item)
                if string:
                    writer.writerow([string])
                else:
                    continue
        else:
            for item in seg_list:
                string = find_chinese(item)
                if string and len(string) > 1:
                    writer.writerow([string])
                else:
                    continue
    print('分词已完成，并生成了对应的数据文件')

if __name__ == "__main__":
    main()