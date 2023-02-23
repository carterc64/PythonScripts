import win32api, win32con
import time
import os
import PIL
from PIL import ImageOps 
from numpy import *




class cords():
    xPad = 316
    yPad = 139

    startMenu1 = (457, 294)
    startMenu2 = (454, 586)
    startMenu3 = (846, 656)
    startMenu4 = (460, 547)

    f_shrimp = (50, 486)
    f_rice = (135, 488)
    f_nori = (56, 568)
    f_roe = (134, 570)
    f_salman = (52, 648)
    f_unagi = (131, 644)

    plate1 = (136, 304)
    plate2 = (281, 304)
    plate3 = (433, 301)
    plate4 = (579, 304)
    plate5 = (728, 306)
    plate6 = (883, 298)

    phone = (853, 520)

    m_toppings = (794, 396)
    m_rice = (794, 423)
    m_sake = (794, 461)

    t_shrimp = (725, 324)
    t_unagi = (847, 323)
    t_nori = (722, 399)
    t_fishEgg = (841, 400)
    t_salmon = (723, 485)

    t_rice = (798, 414)

    t_sake = (798, 414)

    deliverN = (721, 427)
    deliverE = (843, 427)


class sushi():

    r_onigiri = [cords.f_rice, cords.f_rice, cords.f_nori]
    r_caliroll = [cords.f_rice, cords.f_nori, cords.f_roe ]
    r_gunkan = [cords.f_rice, cords.f_nori, cords.f_roe, cords.f_roe]

    onigiri = (r_onigiri, "onigiri")
    caliroll = (r_caliroll, "caliroll")
    gunkan = (r_gunkan, "gunkan")

    sushiList = [onigiri, caliroll, gunkan]




def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print ("Click")


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print ("Left down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print ("Left up")

def mousePos(cord):
    win32api.SetCursorPos((cords.xPad + cord[0], cords.yPad + cord[1]))

def getCords():
    x,y = win32api.GetCursorPos()
    x = x-cords.xPad
    y = y-cords.yPad
    print (x,y)

def startGame():
    mousePos((cords.startMenu1))
    leftClick()
    time.sleep(.1)

    mousePos((cords.startMenu2))
    leftClick()
    time.sleep(.1)

    mousePos((cords.startMenu3))
    leftClick()
    time.sleep(.1)

    mousePos((cords.startMenu4))
    leftClick()
    time.sleep(.1)

def clearTables():
    mousePos(cords.plate1)
    leftClick()
    mousePos(cords.plate2)
    leftClick()
    mousePos(cords.plate3)
    leftClick()
    mousePos(cords.plate4)
    leftClick()
    mousePos(cords.plate5)
    leftClick()
    mousePos(cords.plate6)
    leftClick()
    time.sleep(1)

def foldMat():
    mousePos((cords.f_rice[0] + 100, cords.f_rice[1]))
    leftClick()


def makeFood(food):
    
    for item in sushi.sushiList:
        if (item[1] == food):
            for item in item[0]:
                mousePos(item)
                leftClick()
                time.sleep(.1)
    
    foldMat()
    time.sleep(.5)
    print ("sushi created")
    time.sleep(1.5)


def buyFood(food):

    mousePos(cords.phone)
    mousePos(cords.m_toppings)
	
	
    mousePos(cords.t_shrimp)
    mousePos(cords.t_nori)
    mousePos(cords.t_fishEgg)
    mousePos(cords.t_salmon)
    mousePos(cords.t_unagi)
    mousePos(cords.t_exit)
    mousePos(cords.m_rice)
    mousePos(cords.t_rice)
	
    mousePos(cords.deliverN)


def main():
   startGame()
   #makeFood("caliroll")

if __name__ == '__main__':
    main()



