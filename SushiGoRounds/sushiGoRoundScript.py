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


def main():
   getCords()

if __name__ == '__main__':
    main()


