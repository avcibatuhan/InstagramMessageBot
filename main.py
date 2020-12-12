import pyautogui
import time

text2=open('text2','r')
time.sleep(1)

for word in text2:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)
