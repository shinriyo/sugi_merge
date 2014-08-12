すぎマージ ver 0.1
===

使い方
--

1. ウィンドウに最初のファイルをドラッグする。
2. 結合ボタンを押下。
3. 同じフォルダにxxxAtlas.pngが生成される


必須
---
* PIL
* wx

_wxPython3.0-osx-3.0.0.0-cocoa-py2.7 をお奨めする_

_wxPython3.0-osx-3.0.0.0-carbon-py2.7 carbonは動かない。_

*py2app化の手順*

http://webconsole.blogspot.jp/2007/08/py2app.html

`py2applet --make-setup sugi_merge.py`

`rm -rf build dist`

`python setup.py py2app -A`

`open ./dist/sugi_merge.app`


