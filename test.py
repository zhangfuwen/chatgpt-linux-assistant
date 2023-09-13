import tkinter as tk
import tkinter.font as tkfont

# 创建应用程序窗口
window = tk.Tk()

import tkinter as tk
from tkinter import font

# 获取已安装的字体列表
font_names = font.families()

# 输出字体列表
for name in font_names:
    print(name)

#font_file = "/path/to/font.ttf"
#font_file="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"

# 创建自定义字体对象
#font = font.Font(family="CustomFont", file=font_file)

# 创建字体对象
font = tkfont.Font(family="PingFang", size=12)

# 创建 Entry 组件并设置字体
entry = tk.Entry(window, font=font)
entry.pack()

import tkinter as tk
from tkinter import font
import fontTools.ttLib as ttLib

root = tk.Tk()

# 获取所有可用字体的名称列表
available_fonts = font.families()
print(f"num fonts {len(available_fonts)}")

# 遍历每个字体名称获取字体文件路径
for font_name in available_fonts:
    try:
        font_properties = font.Font(font=font_name)
        font_file_path = font_properties.actual()['file']
        tt = ttLib.TTFont(font_file_path)
        print(f"Font Name: {font_name}")
        print(f"File Path: {font_file_path}")
        print(f"Full Name: {tt['name'].getNames()}")
        print("------------------")
    except:
        print(f"fail")
        pass

# 运行窗口的事件循环
window.mainloop()
