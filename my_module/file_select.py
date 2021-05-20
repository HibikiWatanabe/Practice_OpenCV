#ファイルを選択する機能
import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog

root = tkinter.Tk()
root.withdraw()

def f_select(path):
    #jpgファイルのみ表示
    typ = [("jpgファイル","*.jpg"), ("pngファイル","*.png"), ("gifファイル","*.gif")] 

    #ファイル選択を促すメッセージ
    tkinter.messagebox.showinfo('mosaic_app','処理ファイルを選択してください') 

    #エクスプローラによるファイル選択とfileへのパスの格納 iDirに名が入ったディレクトリが最初に開かれる
    file = tkinter.filedialog.askopenfilename(filetypes = typ,initialdir = dir) 

    # 処理ファイル名のメッセージ出力
    tkinter.messagebox.showinfo('mosaic_app',file+'を選択しました')

    return file

#テスト実行用
'''
f_name = f_select()
print(f_name)
'''