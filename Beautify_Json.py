# coding=utf-8
import wx
from beautify_json_function import beautify_json_function
from search_field import find_all_field_paths_and_values
import json

class MaimFrame(wx.Frame) :
    def __init__(self, parent, id) :
        wx.Frame.__init__(self, parent, id, title = "Beautify_Json V1.0.1", pos = (100, 100), size = (860, 845))
        # 创建第一个面板
        panel = wx.Panel(self, pos = (0, 0), size = (160, 230))
        # 控件
        self.json_txt = wx.StaticText(panel, label = "JSON数据", pos = (5, 10))
        # 控件
        self.json_txts = wx.TextCtrl(panel, pos = (15, 30), size = (130, 150), style = wx.TE_MULTILINE)

        # 创建第二个面板（----------------测试结果显示框-----------------------------）
        panel1 = wx.Panel(self, pos = (162, 0), size = (698, 800))
        self.show_text = wx.TextCtrl(panel1, id = -1, value = '', pos = (0, 0), size = (680, 790),
                                     style = wx.TE_MULTILINE | wx.TE_READONLY)

        # 获取按钮
        self.get_lst = wx.Button(panel, label = '美化', pos = (20, 190), size = (100, 30))
        self.get_lst.Bind(wx.EVT_BUTTON, self.get_lsts)



        panel3 = wx.Panel(self, pos = (0, 231), size = (160, 250))
        # 控件
        self.json_txt3 = wx.StaticText(panel3, label = "JSON数据", pos = (5, 10))
        # 控件
        self.json_datas3 = wx.TextCtrl(panel3, pos = (15, 30), size = (130, 150), style = wx.TE_MULTILINE)


        self.field_txt = wx.StaticText(panel3, label = "字段名称", pos = (5, 190))
        self.field_name = wx.TextCtrl(panel3, pos = (60, 190), size = (80, 20), style = wx.TE_LEFT)
        # 获取按钮
        self.get_lst = wx.Button(panel3, label = '查找', pos = (20, 215), size = (100, 30))
        self.get_lst.Bind(wx.EVT_BUTTON, self.find_field)


    def find_field(self,event) :
        try:
            # 取形如字符串的数据 并转为JSON数据
            jsonstr = self.json_datas3.GetValue()
            json_data = json.loads(jsonstr)
            # 取要查找的字段名称
            field_name1 = self.field_name.GetValue()
            # 获取这个字段在json中的路径
            res = find_all_field_paths_and_values(json_data,field_name1)
            if res :
                # self.show_text.Clear()
                self.show_text.AppendText('解析成功\n')
                self.show_text.AppendText(str(json_data) + '\n\n\n')
                for i in res :
                    url, values = i
                    self.show_text.AppendText('路径为：{0} 值为：{1}\n'.format(url, values))

                    output_string = ''.join(f'["{item}"]' if item.isdigit() else f'["{item}"]' for item in url)
                    self.show_text.AppendText('取值路径为：{}\n\n'.format(output_string))
            else :
                self.show_text.AppendText("未找到 {} 这个字段\n\n\n".format(field_name1))
        except Exception as e:
            # 形如字符串的数据转JSON数据 失败
            self.show_text.Clear()
            self.show_text.AppendText('解析JSON数据失败 {}\n'.format(e))

    # 获取按钮的Demo函数
    def get_lsts(self,event) :
        res = beautify_json_function(self.json_txts.GetValue())
        if res:
            self.show_text.Clear()
            self.show_text.AppendText('美化成功\n')
            self.show_text.AppendText(res+'\n\n\n\n\n')
        else:
            self.show_text.AppendText("美化异常\n\n\n\n\n")


def main() :
    app = wx.App()
    win = MaimFrame(parent = None, id = -1)  # 创建窗体
    win.Show()  # 显示窗体
    app.MainLoop()  # 运行程序


if __name__ == "__main__" :
    main()