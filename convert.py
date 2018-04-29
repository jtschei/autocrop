from pathlib import Path
from PIL import Image
from PIL import ImageChops
import sys

def docrop(pngfile,jpgfile):
    orig = Image.open(pngfile)
    rgb = orig.convert('RGB')
    pix = rgb.getpixel((0,0))
    whiteBoundary = False

    if (pix[0] == 255 and pix[1] == 255 and pix[2] == 255):
        whiteBoundary = True

    if whiteBoundary:
        rgb = ImageChops.invert(rgb)

    box = rgb.getbbox()
    cropped = rgb.crop(box)

    if whiteBoundary:
        cropped = ImageChops.invert(cropped)

    cropped.save(jpgfile)

if __name__ == "__main__":
    srcdir = sys.argv[1]
    dstdir = sys.argv[2]
    newbase = sys.argv[3]

    idx=100
    srcfiles = Path(srcdir).glob('*.png')
    for srcfile in srcfiles:
        dstfile = dstdir + "/" + newbase + "-" + str(idx) + ".jpeg"
        print("{} => {}".format(srcfile,dstfile))
        docrop(srcfile,dstfile)
        idx = idx + 1
