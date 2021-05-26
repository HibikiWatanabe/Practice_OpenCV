import numpy as np
import cv2
import os
import tkinter.messagebox
import tkinter.filedialog

def start():
    #空ウィンドウ
    cv2.namedWindow('window',cv2.WINDOW_NORMAL) 

def get_area( path):
    ROI = cv2.selectROI('Select ROIs', path, fromCenter=False, showCrosshair=False)
    return ROI