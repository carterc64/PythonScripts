import PIL
from PIL import Image, ImageGrab
import os
import time

"""
All coordinates with 1920 x 1080 in Microsoft Edge
xPad = 364
yPad = 174
play area = xPad+1, yPad+1, 1175, 782
"""


xPad = 364
yPad = 174
def screenGrab():
    box = (xPad+1, yPad+1, xPad+811, yPad+608)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap_' + 
            str(int(time.time())) + '.png', 'PNG')
    print("screenGrab succesful")
    

def main():
    screenGrab()

if __name__ == '__main__':
    main()
