from PIL import Image

#
# 直接替换像素
#
def cut(file_name):
    img = Image.open(file_name)
    img = img.convert("RGBA")

    pixdata = img.load()

    # Clean the background noise, if color != white, then set to black.
    # change with your color
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (0, 0, 0, 0)
                
    img.save("new_" + file_name)
    
cut('AI05newworld.png')