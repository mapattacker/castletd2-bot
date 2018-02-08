import pyautogui
import time

speed = (546,99)
list = [(304, 318), (360, 295), (401, 267), (447, 238), \
        (381, 216), (310, 213), (231, 214), (160, 234), \
        (202, 265), (260, 295), (473, 326), (523, 295), \
        (121, 325), (80, 291)]
upgrade = [(35,35),(0,-61),(33,-41),(0,-61)]
hero = [(38, 146),(37, 197),(583, 142)]
start = (582, 359)

# select screen
pyautogui.click(list[0])

# shift heros
for i in hero:
    pyautogui.click(i)
    pyautogui.click(206, 309)

# speed up
pyautogui.click(speed)
# pyautogui.click(start) round
pyautogui.click(start)
time.sleep(2)

# 1st tower
for i in list:
    a = i
    pyautogui.click(a)
    time.sleep(0.5)
    z = upgrade[0]
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(0.5)
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(0.15)
    pyautogui.click(start)

time.sleep(15)
pyautogui.click(start)

for i in list:
    a = i
    pyautogui.click(a)
    time.sleep(0.5)
    z = upgrade[1]
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(0.5)
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(5)
    pyautogui.click(start)

time.sleep(15)        
pyautogui.click(start)

for i in list:
    a = i
    pyautogui.click(a)
    time.sleep(0.5)
    z = upgrade[2]
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(0.5)
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(8)
    pyautogui.click(start)

for i in list:
    a = i
    pyautogui.click(a)
    time.sleep(0.5)
    z = upgrade[3]
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(0.5)
    pyautogui.click(a[0]+z[0],a[1]+z[1])
    time.sleep(12)
    pyautogui.click(start)

# print(pyautogui.position())

# cancel, remove ad, remove ad2, restart
time.sleep(30)
restart = [(237, 343),(327, 100),(24, 101),(366, 323)]
for i in restart:
    pyautogui.click(i)
    time.sleep(7)