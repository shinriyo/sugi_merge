#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from image_merger import convert
import os
import re
import glob
#http://d.hatena.ne.jp/Megumi221/20110308/1299571975


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        # ファイルをドロップする対象
        self.window = window
        self._file_list = []
        self._output_name = 'output.png'


    # ファイルをドロップするときの処理
    def OnDropFiles(self, x, y, filenames):
        for file in filenames:
            # 最初のファイルにする
            self._first_file = file
            #self.window.text.SetValue(file)
            # 最期の数字だけを取る
            nums = re.findall('\d+', file)
            last_num = nums[len(nums)-1]
            # ファイル名
            file_name = os.path.basename(file)
            # 数字をとった名前 xxxx.pngを取る
            base_name = file_name.replace(last_num+'.png', '')

            # パスだけの絶対パス
            dir_path = os.path.dirname(file)
            self._output_name = os.path.join(dir_path, base_name)+'Atlas.png'
            files = glob.glob(os.path.join(dir_path, base_name)+'*.png')
            self.window.text.SetLabel('\n'.join(files))
            self._file_list = files
	    break


    @property
    def file_list(self):
        return self._file_list

    @property
    def first_file(self):
        return self._first_file


    @property
    def output_name(self):
        return self._output_name


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Merge Images",
                          size=(500, 300))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        drag_lbl = wx.StaticText(panel, -1, "ここに1番目のpngを1つドラッグ")
        sizer.Add(drag_lbl, flag=wx.GROW)
        # 水平線
        sizer.Add(wx.StaticLine(panel),flag=wx.GROW)

        w_lbl = wx.StaticText(panel, wx.ID_ANY, "【対象ファイル一覧】")
        sizer.Add(w_lbl, flag=wx.GROW)

        self.text = wx.StaticText(panel, wx.ID_ANY, "")
        sizer.Add(self.text, flag=wx.GROW)
        panel.SetSizer(sizer)

        # ドロップする対象をこのフレーム全体にする
        self.dt = MyFileDropTarget(self) 
        self.SetDropTarget(self.dt)

        # ボタン
        button_name = "結合"
        run_button = wx.Button(panel, wx.ALL, button_name)
        # コールバック
        run_button.Bind(wx.EVT_BUTTON, lambda evt, temp=button_name: self.on_button(evt, temp))
        sizer.Add(run_button, wx.ALL, 5)


    # 結合ボタンのコール
    def on_button(self, Event, button_label):
        files = self.dt.file_list
        if len(files) == 0:
            return

        fst = self.dt.first_file
        out_file = self.dt.output_name
        convert(fst, out_file, files)

        count = len(files)
        #for file in files:
        #    print (file)


app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()
