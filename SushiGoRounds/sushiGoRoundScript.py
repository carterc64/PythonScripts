import win32api, win32con
import time
import os


class cords():
    xPad = 364
    yPad = 174

    startMenu1 = (250, 168)
    startMenu2 = (260, 366)
    startMenu3 = (517, 417)
    startMenu4 = (260, 366)

    f_shrimp = (-36, 300)
    f_rice = (20, 299)
    f_nori = (-38, 356)
    f_roe = (27, 355)
    f_salman = (-36, 411)
    f_unagi = (18, 409)

    plate1 = (20,175)
    plate2 = (122, 172)
    plate3 = (228, 174)
    plate4 = (327, 175)
    plate5 = (432, 176)
    plate6 = (531, 176)

    phone = (518, 329)

    m_toppings = (479, 240)
    m_rice = (477, 261)
    m_sake = (481, 283)

    t_shrimp = (427, 190)
    t_unagi = (510, 184)
    t_nori = (426, 244)
    t_fishEgg = (514, 242)
    t_salmon = (428, 300)

    t_rice = (478, 245)

    t_sake = (478, 237)

    deliverN = (425, 256)
    deliverE = (511, 262)


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
    x = x - cords.xPad
    y = y - cords.yPad
    print (x,y)

def startGame():
    mousePos((250, 168))
    leftClick()
    time.sleep(.1)

    mousePos((260, 366))
    leftClick()
    time.sleep(.1)

    mousePos((517, 417))
    leftClick()
    time.sleep(.1)

    mousePos((266, 366))
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


def main():
   startGame()
   makeFood("caliroll")

if __name__ == '__main__':
    main()



