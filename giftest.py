from PIL import Image
import sys
import os
GIF  = input("Enter the GIF filename")
def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print ("Cant load", infile)
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()
    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            #Convert a gif to a set of black and white images
            #new_im = new_im.convert("L")
            new_im.paste(im)
            fname = infile[0:(len(infile)-4)]+'_'+str(i)+'.png'
            new_im.save('Screenshot_'+ fname, 'PNG')
            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence

processImage(GIF)