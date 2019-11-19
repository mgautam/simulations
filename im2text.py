from PIL import Image
import pytesseract
import os

m=1;#margin

imname = "/home/gautam/Pictures/Invoice2.jpg"
#fo = open("box.txt","r")
rectstrs = os.popen('./swtdetect '+ imname).read().split('\n');
with Image.open(imname) as im:
    i=0;
    #for line in fo.readlines():
    for line in rectstrs:
        #print(line)
        #x=line[:-1].split(" ")
        x=line.split(" ")
        #print(x)
        if (x[0] != 'total') or (x[0] != ''):
            try:
                x = map(int,x);
                box = (x[0]-m,x[1]-m,x[0]+x[2]+m,x[1]+x[3]+m);#(35, 30, 206, 37)
                region = im.crop(box)
                i=i+1
                region.save("cropped/"+str(i)+".png","PNG")
                #im.save("cropped/1"+str(i)+".png","PNG")
                print(pytesseract.image_to_string(region))
            except:
                continue
#fo.close()
