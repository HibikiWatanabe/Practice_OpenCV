import os
import sys
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import numpy as np
import cv2
from numpy.lib.type_check import imag

#空ウィンドウ対策
root = tk.Tk()
root.withdraw()

#初期設定
dir = os.path.abspath(os.path.dirname('..//'+__file__)) #最初に開くディレクトリのパス
ratio = 0.1

#関数群
def f_open(file_name):
    img = cv2.imread(file_name) #画像読み込み
    cv2.imshow('window', img) #画像のウィンドウ表示
    #ROI = cv2.selectROI('window', img, fromCenter=False, showCrosshair=False)

def f_select():
    #対応拡張子
    typ = [("jpgファイル","*.jpg"), ("pngファイル","*.png"), ("gifファイル","*.gif")] 

    #ファイル選択を促すメッセージ
    tkinter.messagebox.showinfo('mosaic_app', '処理画像を選択してください') 

    #エクスプローラによるファイル選択とfileへのパスの格納 iDirに名が入ったディレクトリが最初に開かれる
    file = tkinter.filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

    # 処理ファイル名のメッセージ出力
    tkinter.messagebox.showinfo('mosaic_app', file+'を選択しました')

    return file

def start():
    #空ウィンドウ
    cv2.namedWindow('window',cv2.WINDOW_NORMAL) 

def get_area(path):
    ROI = cv2.selectROI('Select ROIs', path, fromCenter=False, showCrosshair=False)
    return ROI

def start():
    #空ウィンドウ
    cv2.namedWindow('window',cv2.WINDOW_NORMAL) 

def get_area(path):
    ROI = cv2.selectROI('Select ROIs', path, fromCenter=False, showCrosshair=False)
    return ROI

def mosaic(img, ratio):
    hoge = cv2.resize(img, None, fx = ratio, fy = ratio, interpolation=cv2.INTER_NEAREST)

    return cv2.resize(hoge, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(img, ROI, ratio):
    dst = img
    dst[ROI[1]:ROI[1]+ROI[3], ROI[0]:ROI[0]+ROI[2]] = mosaic(dst[ROI[1]:ROI[1]+ROI[3], ROI[0]:ROI[0]+ROI[2]], ratio)
    
    return dst

def end():
    cv2.destroyWindow('window') #ここまでに作られたすべてのウィンドウを閉じる

def mode_m(img):
    tkinter.messagebox.showinfo('mosaic_app','モザイクをかける範囲を選択してください')
    ROI = cv2.selectROI('window', img, fromCenter=False, showCrosshair=False) 
    print(ROI)
    dst = mosaic_area(img, ROI, ratio)
    return dst    

def change_ratio(prm):
    global ratio 
    ratio = prm / 100


#メイン処理
start() #初期画面
open_file = f_select() #開く画像ファイル選択
img = cv2.imread(open_file) #画像読み込み
cv2.imshow('window', img) #画像のウィンドウ表示
cv2.createTrackbar('Ratio','window',1,30,change_ratio)
while(1):
    key = cv2.waitKey(0) #キー入力待ち(この場合何かしらキーが入力されるまで無限に待つ)
    if key ==  27: #終了
        end()
        sys.exit()
    elif key == ord('s'): #モザイクかける
        dst = mode_m(img)
        cv2.imshow('window', dst) #画像のウィンドウ表示
    elif key == ord('o'): #別な画像を開く
        open_file = f_select()
        img = cv2.imread(open_file) 
        cv2.imshow('window', img)