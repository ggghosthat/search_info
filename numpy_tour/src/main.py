from turtle import right
from PIL import Image
import cv2
import numpy as np

w, h = 600,800


def gray_fun():
    img = np.zeros((w, h))
    loc = 0
    shade = 0
    n_shades = 255
    for i in range(n_shades):
        img[0:h, loc:loc+w//n_shades] = shade
        loc += w//n_shades
        shade += 255//n_shades

    cv2.imwrite("shady.png", img)

def rgb_fun():
    img = np.zeros((w, h, 3), dtype=np.uint8 )
    loc = 0
    shade = 0
    n_shades = 255
    for i in range(n_shades):
        img[0:h, loc:loc+w//n_shades, 1:6] = shade
        loc += w//n_shades
        shade += 255//n_shades

    cv2.imwrite("rgb_bgr.png", img)
    Image.fromarray(img).save('rgb_rgb.png')


def office_building():
    #landscape
    img = np.zeros((h,w,3), dtype=np.uint8)
    img[:] = (35, 29, 43)
    img[int(h*0.85): h, 0:w] = (35,55,43)

    #building
    img[int(h*0.1):int(h*0.9), int(w*0.2 ):int(w*0.8)] = (94, 101,123)

    #windows
    
    for row in range(6):
        for column in range(5):
            if np.random.randint(0,8) == 5:
                window_color = (240,230, 140)
            else:
                window_color = (28, 23, 35)

            img[int(h*0.1 + 100 * row + 20 ): int(h*0.1 + 60  + 100 * row + 20 ),
                int(w*0.2 + 75 * column + 15): int(w*0.2 + 30  + 75 * column + 15)
                ] = window_color

    Image.fromarray(img).save('office.png')
office_building()