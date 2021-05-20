import numpy as np
import cv2
import os

#テスト画像の出力をやってみる
def f_open(file_name):
    img = cv2.imread(file_name, 0) #画像読み込み
    cv2.imshow('window', img) #画像のウィンドウ表示
    cv2.waitKey(0) #キー入力待ち(この場合何かしらキーが入力されるまで無限に待つ)
    cv2.destoryAllWindows() #ここまでに作られたすべてのウィンドウを閉じる
