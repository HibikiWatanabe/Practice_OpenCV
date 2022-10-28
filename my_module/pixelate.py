import numpy as np
import cv2
import os
import tkinter as tk

def mosaic(img, ratio):
    hoge = cv2.resize(img, None, fx = ratio, fy = ratio, interpolation=cv2.INTER_NEAREST)

    return cv2.resize(hoge, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(img, ROI, ratio):
    dst = img
    dst[ROI[1]:ROI[3], ROI[0]:ROI[2]] = mosaic(dst[ROI[1]:ROI[3], ROI[0]:ROI[2]], ratio)
    
    return dst
