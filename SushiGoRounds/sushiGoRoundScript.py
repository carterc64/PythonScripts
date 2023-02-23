import win32api, win32con
import time
import os
import PIL
from PIL import ImageOps, Image, ImageGrab
from numpy import *


foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}


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

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

    
class order():
    nori = [(33, 30, 11), cords.t_nori, "nori", foodOnHand["nori"]]
    roe = [(127, 61, 0), cords.t_fishEgg, "roe", foodOnHand["roe"]]
    salmon = [(127, 71, 47), cords.t_salmon, "salmon", foodOnHand["salmon"]]
    shrimp = [(127, 102, 90), cords.t_shrimp, "shrimp", foodOnHand["shrimp"]]
    unagi = [(94, 49, 8), cords.t_unagi, "unagi", foodOnHand["unagi"]]
    rice = [(127, 127, 127), cords.t_rice, "rice", foodOnHand["rice"]]
    #sake = ((RGB values im.getPixel()), cords.t_nori)
    orderList = [nori, roe, salmon, shrimp, unagi, rice]

class sushi():
    nori = [ cords.f_nori, "nori", foodOnHand["nori"]]
    roe = [ cords.f_roe, "roe", foodOnHand["roe"]]
    salmon = [ cords.f_salman, "salmon", foodOnHand["salmon"]]
    shrimp = [cords.f_shrimp, "shrimp", foodOnHand["shrimp"]]
    unagi = [cords.f_unagi, "unagi", foodOnHand["unagi"]]
    rice = [ cords.f_rice, "rice", foodOnHand["rice"]]
  

    r_onigiri = [rice, rice, nori]
    r_caliroll = [rice, nori, roe]
    r_gunkan = [rice, nori, roe, roe]

    onigiri = (r_onigiri, "onigiri")
    caliroll = (r_caliroll, "caliroll")
    gunkan = (r_gunkan, "gunkan")

    sushiList = [onigiri, caliroll, gunkan]



    

def orderFood(food):

    for item in sushi.orderList:
        if item[2] == food:
            mousePos(cords.phone)
            time.sleep(.1)
            leftClick()
            mousePos(item[1])
            leftClick()
            s = screenGrab()
            if s.getpixel(item[1]) != item[0]:
                print ("rice avaiable")
                time.sleep(.1)
                leftClick()
                mousePos(cords.deliverN)
                time.sleep(.1)
                leftClick()
                time.sleep(2)
                break
            else: 
                print ("rice not avaiable")
                mousePos(cords.t_exit)
                leftClick()
                time.sleep(1)
                buyFood(food)
    



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
            for item2 in item[0]:
                item2[2] -= 1
                mousePos(item2[0])
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

def screenGrab():
    box = (cords.xPad+1, cords.yPad+1, cords.xPad+811, cords.yPad+608)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png', 'PNG')
    return im

def main():
   startGame()
   makeFood("caliroll")
   makeFood("gunkan")
   makeFood("onigiri")

if __name__ == '__main__':
    main()



