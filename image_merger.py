#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 参考URL
# http://librabuch.jp/2013/05/python_pillow_pil/

import sys
import Image
argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数
print (argc)

base_file_name = "spAttackDamage"

digit = 4

# 最初の数字
first_num = 1

#ファイル数
file_count = 16

digited_num = first_num.zfill(digit)
# 今後のサイズのため1つ開いてサイズ計算
fst_img = Image.open(base_file_name + digited_num + ".png")
width, height = fst_img.size
print (width)
print (height)

canvas_width = 4
canvas_height = 4

# 下地
canvas = Image.new('RGBA', (width*canvas_width, height*canvas_height),
		(255, 255, 255, 255))

for x in range(canvas_width):
    for y in range(canvas_height):
        digited_num = first_num.zfill(digit)
        img = Image.open(base_file_name + digited_num + ".png")
        canvas.paste(img, (width*y, height*x))
        first_num += 1

# 出力
canvas.save(base_file_name + "Atlas.png")

