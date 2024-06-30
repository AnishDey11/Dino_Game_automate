import pyautogui
import time
from PIL import Image, ImageGrab

def type(line):
    pyautogui.typewrite(line)

def hit(key):
    pyautogui.keyDown(key)
    return

def press(key):
    pyautogui.press(key)

def is_colliding(data):
    for i in range(460, 550):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                hit("up")
                return
    for i in range(430, 530):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return

def ti(sec):
    time.sleep(sec)

if __name__ == "__main__":
    pyautogui.hotkey("winleft", "d")
    ti(5)
    press("winleft")
    ti(1)
    type("chrome")
    ti(2)
    press("enter")
    ti(2)
    type("chrome://dino")
    ti(2)
    press("enter")
    ti(1)
    press("space")
    ti(2)
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        is_colliding(data)
        # for i in range(350, 400):
        #     for j in range(410, 563):
        #         data[i, j] = 171
        # for i in range(300, 350):
        #     for j in range(563, 650):
        #         data[i, j] = 0
        # image.show()
        # break