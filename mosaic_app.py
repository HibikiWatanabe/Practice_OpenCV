import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
from my_module import file_select, file_display

#とりあえずこのファイルと同じディレクトリをiDirに格納
dir = os.path.abspath(os.path.dirname('..//'+__file__)) 

file_name = file_select.f_select(dir)
print("Selected File Name:" + file_name) #パス取得テスト用

file_display.f_open(file_name)