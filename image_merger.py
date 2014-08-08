#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 参考URL
# http://librabuch.jp/2013/05/python_pillow_pil/

import sys
import math
import Image


def convert(fst_file, out_put, file_list):
    """
    fst_file は最初のファイルのパス
    out_put は出力ファイル名
    file_list は元の画像リスト
    """
    file_count = len(file_list)

    # 今後のサイズのため1つ開いてサイズ計算
    fst_img = Image.open(fst_file)
    width, height = fst_img.size

    # 縦横のサイズを平方根で切り上げで
    canvas_width = canvas_height = int(math.ceil(math.sqrt(file_count)))

    # 下地
    # R G B A・・・Aは0にしないと透明にならない
    canvas = Image.new('RGBA', (width*canvas_width, height*canvas_height),
            (255, 255, 255, 0))

    for x in range(canvas_width):
        for y in range(canvas_height):
            index = x * canvas_width + y

            # indexがlistを超えることはある
            if index == file_count:
                break
            img = Image.open(file_list[index])
            canvas.paste(img, (width*y, height*x))

    # 出力
    canvas.save(out_put)
