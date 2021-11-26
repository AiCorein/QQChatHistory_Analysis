import data2csv
import words_segment
import words_statistics
import toClound
from mht2html import convert
import argparse
from hiddenPrint import HiddenPrints
import sys

"""
主程序，通过命令行参数实现控制流
    - 转化 mht 为 html
    - 解析 html 消息记录
    - 分词，提取中文
    - 频率统计
    - 生成词云
"""

def main(src, dest, mode='word'):
    print('>>>现在开始转化 mht 为 html ')
    convert(src)
    print('>>>mht 转化完成\n')

    print('>>>现在开始解析 html 为消息记录数据文件 ')
    data2csv.main()
    print('>>>解析完成，存储完成\n')

    print('>>>现在开始进行分词统计，并储存数据文件 ')
    words_segment.main(mode)
    print('使用统计模式：%s' %mode)
    print('>>>分词完成，存储完成\n')

    print('>>>现在开始进行词频统计，并存储数据文件 ')
    words_statistics.main()
    print('>>>统计完成，存储完成\n')

    print('>>>现在开始生成词云 ')
    toClound.main(dest)
    print('>>>生成结束，并已存储在 %s\n' %dest)
    print('程序结束并已退出')


parser = argparse.ArgumentParser(
    description="description: 通过 QQ 聊天记录 (电脑端导出的 mht 文件) 生成词云",
    epilog='''
        version: 1.0.0, developed by AiCorein © 2021
        (更多功能开发中...)
    '''
)
parser.add_argument('src', help="mht 文件路径")
parser.add_argument('dest', help="输出词云图片的路径")
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-v", "--verbose", help="详细的回显(默认)", action="store_true")
group1.add_argument("-q", "--quiet", help="只显示必要的回显", action="store_true")
group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-c", "--char", help="词频统计包含单字", action="store_true")
group2.add_argument("-w", "--word", help="词频统计不包含单字，只统计词语(默认)", action="store_true")
args = parser.parse_args()

if args.quiet:
    print('>>>任务启动...')
    with HiddenPrints():
        if args.char:
            main(args.src, args.dest, 'char')
        else:
            main(args.src, args.dest)
    print('>>>任务完成，已保存至 %s' %args.dest)
else:
    if args.char:
        main(args.src, args.dest, 'char')
    else:
        main(args.src, args.dest)
sys.exit()