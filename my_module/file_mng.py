import numpy as np
import cv2
import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog


#空ウィンドウ対策
root = tk.Tk()
root.withdraw()

def f_open(file_name):
    img = cv2.imread(file_name) #画像読み込み
    cv2.imshow('window', img) #画像のウィンドウ表示
    #ROI = cv2.selectROI('window', img, fromCenter=False, showCrosshair=False)

    while(1):
        key = cv2.waitKey(0) #キー入力待ち(この場合何かしらキーが入力されるまで無限に待つ)
        if key ==  27: #esc
            cv2.destoryAllWindows() #ここまでに作られたすべてのウィンドウを閉じる
        elif key == ord('s'): #s
            tkinter.messagebox.showinfo('mosaic_app','モザイクをかける範囲を選択してください')
            ROI = cv2.selectROI('mosaic', img, fromCenter=False, showCrosshair=False) 
            print(ROI)
            dst = pixelate.mosaic_area(img, ROI, 0.1)
            cv2.imshow('new', dst) #画像のウィンドウ表示


def f_select(path):
    #jpgファイルのみ表示
    typ = [("jpgファイル","*.jpg"), ("pngファイル","*.png"), ("gifファイル","*.gif")] 

    #ファイル選択を促すメッセージ
    tkinter.messagebox.showinfo('mosaic_app', '処理画像を選択してください') 

    #エクスプローラによるファイル選択とfileへのパスの格納 iDirに名が入ったディレクトリが最初に開かれる
    file = tkinter.filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

    # 処理ファイル名のメッセージ出力
    tkinter.messagebox.showinfo('mosaic_app', file+'を選択しました')

    return file
    #テスト実行用
    '''
    f_name = f_select()
    print(f_name)
    '''