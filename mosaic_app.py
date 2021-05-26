import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
from my_module import file_mng

#とりあえずこのファイルと同じディレクトリをiDirに格納
dir = os.path.abspath(os.path.dirname('..//'+__file__)) 
#開くファイルパスをdirに格納
file_name = file_mng.f_select(dir)
#パス取得テスト用
print("Selected File Name:" + file_name) 

#ファイルオープン
file_mng.f_open(file_name)
