import os
from PIL import Image
from sys import argv

def textExtract(im):
    xdim,ydim = im.size
    out = Image.new("RGBA",im.size)
    yt=ydim
    yb=0
    xl=xdim
    xr=0
    for i in range(xdim):
        for j in range(ydim):
            pixel = im.getpixel((i,j))
            if(type(pixel)!=type(1) and len(pixel)>=3):
                if(not(pixel[0]>60 and pixel[1]>60 and pixel[2]>60)):
                    out.putpixel((i,j),(pixel[0],pixel[1],pixel[2],235))
                    yt=min(yt,j)
                    yb=max(yb,j)
                    xl=min(xl,i)
                    xr=max(xr,i)
                else:
                    out.putpixel((i,j),(0,0,0,0))
            else:
                if(pixel<80):
                    out.putpixel((i,j),(pixel,pixel,pixel,235))
                    yt=min(yt,j)
                    yb=max(yb,j)
                    xl=min(xl,i)
                    xr=max(xr,i)
                else:
                    out.putpixel((i,j),(0,0,0,0))
    out=out.crop((xl,yt,xr,yb))
    xdim,ydim = out.size
    try:
        out=out.resize((int((xdim/ydim)*150),150))
    except:
        print(xdim,ydim)
    return out

src_folder = argv[1];
tar_folder = argv[2];
if(not(src_folder.endswith("/"))):
    src_folder+='/'
dic={}
lst = os.listdir(src_folder)
for item in lst:
    if(item!="Blank.jpg"):
        im = Image.open(src_folder+item,"r")
        xdim,ydim = im.size
        try:
            im=im.resize((int((xdim/ydim)*150),150))
            item = item.replace(".jpg","")
            dic[item]=textExtract(im)
        except:
            pass

try:
    os.chdir("profiles")
except:
    os.mkdir("profiles")
    os.chdir("profiles")
    
try:
    os.chdir(tar_folder)
except:
    os.mkdir(tar_folder)
    os.chdir(tar_folder)

for key in dic:
    dic[key].save(key+".png");
