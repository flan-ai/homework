import cv2
import numpy as np


def medianBlur(img, kernel, padding_way):

    w=img.shape[0]
    h=img.shape[1]
    kernel
    if padding_way == "REPLICA":
        img_n=np.pad(img,((1,1),(1,1)),'edge')
    elif padding_way == "ZERO":
        img_n = np.pad(img, ((1, 1), (1, 1)), 'constant', constant_values=(0, 0))
    return cv2.filter2D(img_n,-1,kernel=kernel)



