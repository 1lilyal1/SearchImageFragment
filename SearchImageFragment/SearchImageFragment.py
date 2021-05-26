from PIL import ImageGrab
import os
import time
import cv2
import numpy as np
import time; 
from tqdm import tqdm

# Search for an image by fragment

# Поиск изображения 
# SoursePicture - большое изображение в котом введётся поиск по фрагменту
# template - фрагмент
def FindImage(SoursePicture, template):
    img_rgb = cv2.imread(SoursePicture)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.51 # Если  найденные фрагменты в картинке (SoursePicture), похожи на template больше чем на 51%, то возращает true
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        if pt != None:
            return True
    else:
        return False

Result = ""
template = cv2.imread("fragment.jpg",0) #Малая часть изображения, фрагмент по которому введётся поиск в большом
SoursePicture = "picture" # Каталог с папками в которых возможен фрагмент

start = time.time()
Chapters = os.listdir(SoursePicture);
for Chapter in tqdm(Chapters):
    for picture in  os.listdir(SoursePicture + "/" + Chapter):
        if FingImage(SoursePicture + "/"  + Chapter + "/" + picture, template):
            Result += SoursePicture + "/" + Chapter + "/" + picture + "\n"

timeEnd = "Ran in {} seconds".format(time.time() - start)
Result += timeEnd
my_file = open("Result.txt", "w+")
my_file.write(Result)
my_file.close()
