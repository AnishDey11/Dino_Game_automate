import pyautogui
import time
from PIL import Image, ImageGrab

def hit(key):
    pyautogui.keyDown(key)
    return

def is_colliding(data):
    for i in range(460, 550):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
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
    ti(3)
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