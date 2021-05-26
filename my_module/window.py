import numpy as np
import cv2
import os
import tkinter.messagebox
import tkinter.filedialog

def get_area(event, x, y, flg):
    ROI = cv2.selectROI('Select ROIs')