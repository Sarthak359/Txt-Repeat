import pyautogui
import time
time.sleep(4)
count = 0
while count <= 10:
    pyautogui.typewrite("i LOVE YOU❤️ "+str(count))
    pyautogui.press("enter")
    count = count+1
    time.sleep(1)

