from PIL import Image

#
# 通过色彩通道分离，不过效果看起来不理想
#

def fix(fname):
    im = Image.open(fname)
    newim = im.convert("RGBA")
    
    
    source = im.split()
    R, G, B = 0, 1, 2
    #rmask = source[R].point(lambda i:i != 255 and 255)
    #gmask = source[G].point(lambda i:i != 255 and 255)
    #bmask = source[B].point(lambda i:i != 255 and 255)       
    rmask = source[R].point(lambda i:i >= 255 and 255)
    gmask = source[G].point(lambda i:i >= 255 and 255)
    bmask = source[B].point(lambda i:i >= 255 and 255)
    out = Image.new("RGBA", im.size, None)
    #out.save("out.png")

    #out = source[G].point(lambda i: i * 0.7)
    
    newim.paste(out, None, rmask)
    newim.paste(out, None, gmask)
    newim.paste(out, None, bmask)      
    
    newim.save("test.png")
    rmask.save("rmask.png")
    gmask.save("gmask.png")
    bmask.save("bmask.png")
    
    
fix('AI05newworld.png')