from lxml import etree
import csv

"""
处理并解析 html 文件，将聊天消息、消息发送者 qq 号、发送时间这些信息
存入 csv 文件中。
"""

def parse_writeout(html_file):
    # 初始化
    tree = etree.parse(html_file, etree.HTMLParser())
    td_list = tree.xpath('//tr/td')

    # 消息计数
    num = 0
    # 记录当前日期
    curDate = ''
    # 盛装所有数据元组（元组包含 id，消息和时间）
    tuple_list = []

    # 初始化，写入表头
    fp = open(r'./works/messages.csv', 'w', encoding='utf-8_sig', newline='')
    writer = csv.writer(fp)
    writer.writerow(['id', 'message', 'time'])

    for item in td_list:
        # 解析日期是否有更新，有更新则替换最新日期拼接时间字符串
        date = item.xpath('./text()')
        if date and date[0][0] != '\r':
            curDate = date[0][-10:]
        
        # 解析时间、 id 和消息
        time = item.xpath('./div[1]/text()')
        id_info = item.xpath('./div[1]/div/text()')
        message = item.xpath('./div[2]/font/text()')

        # 筛选文字消息执行以下操作（非文字消息 message 列表为空）
        if id_info and message and id_info[0][:4] != '系统消息':
            # 时间由当前日期和具体时间拼接而成
            time = curDate + ' ' + time[0]
            
            # @类的消息的列表，最后一个元素才是有效值
            if (len(message) > 1):
                tuple_list.append((id_info[0], message[-1], time))
            else:
                tuple_list.append((id_info[0], message[0], time))
            num += 1

    writer.writerows(tuple_list)
    return num


def main():
    record_num = parse_writeout('./works/records.html')
    print('遍历记录%d条' %record_num)
    print('消息记录 csv 数据文件已生成')


if __name__ == "__main__":
    main()
