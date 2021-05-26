import numpy as np
import cv2
import os
import tkinter.messagebox
import tkinter.filedialog

def f_open(file_name):
    img = cv2.imread(file_name, 1) #画像読み込み
    cv2.namedWindow('window',cv2.WINDOW_NORMAL)
    cv2.imshow('window', img) #画像のウィンドウ表示

    while(1):
        key = cv2.waitKey(0) #キー入力待ち(この場合何かしらキーが入力されるまで無限に待つ)
        if key ==  27: #esc
            cv2.destoryAllWindows() #ここまでに作られたすべてのウィンドウを閉じる
        elif key == ord('s'): #s
            tkinter.messagebox.showinfo('mosaic_app','sが押されました') 
            