# import numpy as np
import wordcloud
# from PIL import Image
# import matplotlib.pyplot as plt
import csv
import random

"""
配置并生成词云图片
"""

def random_color(word, font_size, position, orientation, font_path, random_state):
	s = 'hsl(%d, %d%%, %d%%)' % (random.randint(0, 360), random.randint(65, 80), random.randint(65, 80))
	return s

def main(dest):
    with open(r'./works/statistics.csv', 'r', encoding = 'utf-8_sig') as fp:
        reader = csv.reader(fp)
        all_words_dict = {row[1]:row[2] for row in reader}
        del all_words_dict['word']
        for k, v in all_words_dict.items():
            all_words_dict[k] = int(v)

    # 定义词频背景
    # mask = np.array(Image.open('./bd.png'))
    # color = np.array(Image.open('./color.png'))
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/STSONG.ttf', # 设置字体格式
        background_color="white",
        # mask=mask, # 设置背景图
        max_words=200, # 最多显示词数
        min_font_size=10,
        max_font_size=80, # 字体最大值
        # color_func=random_color, # 从颜色函数创建字体颜色
        random_state=50,
        scale=32
    )

    print('词云转换工作中')
    wc.generate_from_frequencies(all_words_dict)            # 从字典生成词云
    # image_colors = wordcloud.ImageColorGenerator(color)   # 从背景图建立颜色方案
    # wc.recolor(color_func=image_colors)                   # 将词云颜色设置为背景图方案
    # plt.imshow(wc) # 显示词云
    wc.to_file(dest)
    # plt.show() # 显示图像

if __name__ == "__main__":
    main()