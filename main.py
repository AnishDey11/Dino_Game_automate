import pyautogui
import time
from PIL import Image, ImageGrab

def press(key):
    pyautogui.keyDown(key)

def iscollide(data):
    for i in range(275, 325):
        for j in range(563, 650):
            if data[i, j] < 100:
                press("up")
                return
    for i in range(250, 300):
        for j in range(410, 563):
            if data[i, j] < 100:
                press("down")
                return
    return

if __name__ == '__main__':
    time.sleep(2)
    press("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)
        # for i in range(275, 325):
        #     for j in range(563, 650):
        #         data[i, j] = 0
        # for i in range(250, 300):
        #     for j in range(410, 563):
        #         data[i, j] = 171
        # image.show()
        # break