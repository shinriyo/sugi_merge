#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
#import image_merger
#http://d.hatena.ne.jp/Megumi221/20110308/1299571975

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        # ファイルをドロップする対象
        self.window = window


    # ファイルをドロップするときの処理
    def OnDropFiles(self, x, y, filenames):
        for file in filenames:
            #self.window.text.SetValue(file)
            self.window.text.SetLabel(file)


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Merge Images",
                          size=(500, 300))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        drag_lbl = wx.StaticText(panel, -1, "ここにpngをドラッグ")
        sizer.Add(drag_lbl, 0, wx.ALL, 5)

        #self.text = wx.TextCtrl(panel, -1, "", size=(200,-1))
        self.text = wx.StaticText(panel, -1, "")
        sizer.Add(self.text, 0, wx.ALL, 5)
        panel.SetSizer(sizer)

        # ドロップする対象をこのフレーム全体にする
        dt = MyFileDropTarget(self) 
        self.SetDropTarget(dt)

	run_button = wx.Button(panel, wx.ALL, "結合")
	sizer.Add(run_button, wx.ALL, 5)


app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()
