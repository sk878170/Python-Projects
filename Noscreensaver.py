"""When you want to prevent your laptop from going into sleep mode, WE disble screensaver mode"""

import pyautogui

# A infinite loop
print("Screensaver Mode on!")
while 1>0:
    # makes the mouse sleep or wait for 40 seconds
    pyautogui.sleep(10)
    # clicks about in the corner of the screen like
    # on the co-ordinates of (50,400)
    pyautogui.click(50,400)
    