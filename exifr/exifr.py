#!C:/Python37/python3

from PIL import Image
import piexif
import sys, os

script, imgname = sys.argv

try:
    im = Image.open(imgname)
    exif_dict = piexif.load(im.info["exif"])
    exif_str = exif_dict["Exif"][36867].decode('utf-8')
    im.close()
except:
    im.close()
    print('File %s does not contain exif information' % imgname)
    sys.exit(0)

# 36867: DateTimeOriginal 36868: DateTimeDigitized

newdir = '\\'.join([exif_str[0:4],exif_str[5:7]])
newname = ''.join([newdir,
                   '\\',
                   exif_str[0:4],    # year
                   exif_str[5:7],    # month
                   exif_str[8:10],   # day
                   exif_str[11:13],  # hour
                   exif_str[14:16],  # minutes
                   exif_str[17:19]   # seconds
                  ])                 # without .jpg

try:
    os.makedirs(newdir)
except:
    pass

i = 1
while True:
    if os.path.isfile(newname+'.jpg'):
        newname += '-' + str(i)
        i += 1
    else:
        break

os.rename(imgname, newname+'.jpg')
print("File %s renamed to %s", (imgname, newname+'.jpg'))
