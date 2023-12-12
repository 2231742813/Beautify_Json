# coding=utf-8
import wx
from beautify_json_function import beautify_json_function

class MaimFrame(wx.Frame) :
    def __init__(self, parent, id) :
        wx.Frame.__init__(self, parent, id, title = "Demo_wxpython V1.0.0", pos = (100, 100), size = (860, 845))
        # 创建第一个面板
        panel = wx.Panel(self, pos = (0, 0), size = (160, 190))
        # 控件
        self.json_txt = wx.StaticText(panel, label = "JSON数据", pos = (5, 10))
        # 控件
        self.json_txts = wx.TextCtrl(panel, pos = (15, 30), size = (130, 150), style = wx.TE_MULTILINE)

        # 创建第二个面板（----------------测试结果显示框-----------------------------）
        panel1 = wx.Panel(self, pos = (162, 0), size = (698, 800))
        self.show_text = wx.TextCtrl(panel1, id = -1, value = '', pos = (0, 0), size = (680, 790),
                                     style = wx.TE_MULTILINE | wx.TE_READONLY)

        # 获取按钮
        panel5 = wx.Panel(self, pos = (0, 191), size = (160, 80))
        self.get_lst = wx.Button(panel5, label = '解析', pos = (20, 35), size = (100, 30))
        self.get_lst.Bind(wx.EVT_BUTTON, self.get_lsts)


    # 获取按钮的Demo函数
    def get_lsts(self,event) :
        res = beautify_json_function(self.json_txts.GetValue())
        if res:
            self.show_text.Clear()
            self.show_text.AppendText('解析成功\n')
            self.show_text.AppendText(res+'\n\n\n\n\n')
        else:
            self.show_text.AppendText("解析异常\n\n\n\n\n")


def main() :
    app = wx.App()
    win = MaimFrame(parent = None, id = -1)  # 创建窗体
    win.Show()  # 显示窗体
    app.MainLoop()  # 运行程序


if __name__ == "__main__" :
    main()