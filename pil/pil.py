#coding=utf-8
from PIL import Image, ImageDraw, ImageFilter
import os
from os import listdir
from os.path import isfile, join
import datetime

def main(file_name):
    bg = Image.open('bg.png')
    bg = bg.convert("RGBA")
    img = Image.open('saurce/' + file_name)
    img = img.convert("RGBA")

    pixdata = img.load()

    # Clean the background noise, if color != white, then set to black.
    # change with your color
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (0, 0, 0, 0)
          
    img.save( 'trans/' + file_name )

    ##############################
    #開啟背景
    width_bg , height_bg = bg.size

    #開啟贴图
    width_img , height_img = img.size

    #重設簽名檔的高為与背景一致
    #new_height_img = int(height_bg)
    #重設簽名檔的寬依據新的寬度等比例縮放
    #new_width_img = int(width_img/height_img*new_height_img)
    #重設簽名檔圖片
    #img_resize = img.resize((new_width_img, new_height_img))

    #背景尺寸修正
    new_height_bg = int(height_img)
    new_width_bg = int(width_bg/height_bg*new_height_bg)
    bg_resize = bg.resize((new_width_bg, new_height_bg))

    #新建一個透明的底圖
    resultPicture = Image.new('RGBA', bg_resize.size, (0, 0, 0, 0))
    #把照片貼到底圖
    resultPicture.paste(bg_resize,(0,0))

    #設定簽名檔的位置參數
    right_top = (new_width_bg - width_img, 0)

    #為了背景保留透明度，將im參數與mask參數皆帶入重設過後的簽名檔圖片
    resultPicture.paste(img, right_top, img)
    #resultPicture.paste(img)

    #儲存新的照片
    resultPicture.save( 'bg/' + file_name )

mypath = 'saurce'

# Get a list of all file names
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(str(onlyfiles))

id = 1

for f in onlyfiles:
    main(f)
    print(str(id) + '/' + str(len(onlyfiles)))
    id += 1
	
print('Done.')