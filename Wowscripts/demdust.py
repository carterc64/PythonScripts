import win32api, win32con
import time
import os
import PIL
from PIL import ImageOps, Image, ImageGrab
from numpy import *


class cords():
    gemSelect = (440,370)
    crushSelect = (380, 350)
    crushButton = (760, 755)

    auctioneer = (1110, 490)
    bagDust = ()
    creatAuction = ()
    cleanUp = ()


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print ("Click")

def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))


def crush(crushes, timeSleep):
    mousePos(cords.crushSelect)
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    mousePos(cords.gemSelect)
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    mousePos(cords.crushButton)
    crushes += 1.35 * timeSleep
    
        


def auction():
    mousePos((1170, 250))
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    mousePos((1290, 270))
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    mousePos((930, 205))
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    mousePos((1785, 735))
    leftClick()
    time.sleep(.1)


def main():
    i = 0
    crushes = 0
    timeSleep = 10
    while (i < 1000):
        crush(crushes, timeSleep)
        time.sleep(2)
        leftClick()
        time.sleep(.1)
        

        time.sleep(timeSleep)
        i += 1


if __name__ == '__main__':
    main()