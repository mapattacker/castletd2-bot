import pyautogui
import time
from PIL import Image
import pytesseract
import os
import numpy as np


startall = time.time()
# define initial OCR text variable
text = '1'
# speed button
speed = (552, 98)
# screenshot directory
img_path = r'screen.png'
img_path_button = r'button.png'
screenshot = "screencapture {}".format(img_path)
screenshot_button = "screencapture {}".format(img_path_button)
# cropping of screenshots
wood = (70, 180, 150, 210)
end_msg = (450, 300, 780, 360)
horizontal_button = (0,800,100,870)
vertical_button = (0,1400,80,1450)
# tower positions
list = [(306, 293), (362, 269), (405, 244), (450, 218), \
        (383, 201), (312, 197), (233, 202), (165, 219), \
        (204, 245), (262, 272), (479, 298), (527, 269), \
        (122, 297), (80, 267)]
# upgrade to lasers
upgrade = [(27,32),(0,-54),(29,-37),(0,-61)]
hero = [(36, 183),(587, 136)]
hero2 = (36, 138)
start = (587, 331)
# back button of vysor
backbutton = (102, 418) # horizontal
backbuttonV = (51, 708) # vertical
cancelbutton = (253, 314)
restartbutton =(361, 296)


# select vysor screen
pyautogui.click(list[0])



def objectrecognition():
    # screenshot to check for ending
    os.system(screenshot)
    img = Image.open(img_path)
    cropped = img.crop(end_msg)
    # declare OCR output variable as global
    global text
    text = pytesseract.image_to_string(cropped) # OCR to text

def colorrecognition(button):
    # screenshot to check for blue button position
    os.system(screenshot_button)
    img = Image.open(img_path_button)
    cropped = img.crop(button)
    # change list into nparray so that can use np.histogram
    rbg = np.array(cropped.histogram())
    # get the first binned quantity
    return int(np.histogram(rbg, bins=200, range=(0,500))[0][0])

def upgrade1st():
    # 1st tower upgrade
    for i in list:
        a = i
        pyautogui.click(a)
        time.sleep(0.5)
        z = upgrade[1]
        pyautogui.click(a[0]+z[0],a[1]+z[1])
        time.sleep(0.5)
        pyautogui.click(a[0]+z[0],a[1]+z[1])
        time.sleep(6)
        pyautogui.click(start)

        # OCR
        objectrecognition()
        if text == 'Emergency':
            global end
            end = 1
            print(1, 'Game Ended')
            # click cancel button when game ends
            pyautogui.click(cancelbutton)
            break
        else:
            pass

def upgrade2nd():
    # 2nd tower upgrade
    global end
    if end != 1:
        for i in list:
            a = i
            pyautogui.click(a)
            time.sleep(0.5)
            z = upgrade[2]
            pyautogui.click(a[0]+z[0],a[1]+z[1])
            time.sleep(0.5)
            pyautogui.click(a[0]+z[0],a[1]+z[1])
            time.sleep(4)
            pyautogui.click(start)
            time.sleep(4)
            pyautogui.click(start)

            # OCR
            objectrecognition()
            if text == 'Emergency':
                end = 1
                print(2, 'Game Ended')
                # click cancel button when game ends
                pyautogui.click(cancelbutton)
                break
            else:
                pass

def finalupgrade():
    # Final tower upgrades
    global end
    if end != 1:
        for zz, i in enumerate(list):
            # remove 2 towers upgrade so it won't kill the boss
            if zz != 3 and zz != 4:
                a = i
                pyautogui.click(a)
                time.sleep(0.5)
                z = upgrade[3]
                pyautogui.click(a[0]+z[0],a[1]+z[1])
                time.sleep(0.5)
                pyautogui.click(a[0]+z[0],a[1]+z[1])
                time.sleep(6)
                pyautogui.click(start)
                time.sleep(6)
                pyautogui.click(start)

                # OCR
                objectrecognition()
                if text == 'Emergency':
                    end = 1
                    print(3, 'Game Ended')
                    # click cancel button when game ends
                    pyautogui.click(cancelbutton)
                    break
                else:
                    pass
        

def restart():
    # remove advert and restart game

    # begin restart if OCR finds game has ended
    if end != 1:
        for i in range(20):
            objectrecognition()
            if text == 'Emergency':
                print(4, 'Game Ended')
                # click cancel button when game ends
                pyautogui.click(cancelbutton)
                break
            else:
                time.sleep(5)
                pass

    for num in range(8):
        objectrecognition()
        time.sleep(3)
        if text == 'Defeat':
            # click restart button if it appears
            print('Restart Button Shown')
            pyautogui.click(restartbutton)
            break
        # account for vertical rotation when displaying ads
        # previous histogram testing shown the quantity of colors fall within 980-1050
        elif 980 > colorrecognition(vertical_button) < 1050:
            print ('Vertical Ad')
            time.sleep(1)
            pyautogui.click(backbuttonV)
            time.sleep(3)
        elif 980 > colorrecognition(horizontal_button) < 1050:
            print ('Horizontal Ad')
            time.sleep(1)
            pyautogui.click(backbutton)
            time.sleep(3)

    endt = time.time()
    if num == 1:
        print (num, 'round down,', 360*num, 'diamonds earned! after',round((endt-startt)/60,2), 'mins')
    else:
        print (num, 'rounds down,', 360*num, 'diamonds earned! after', round((endt-startt)/60,2), 'mins')


# define number of rounds to loop
for num in range(5):
    # flag for ending
    global end
    end = 0
    startt = time.time()
    # shift heros
    for i in hero:
        pyautogui.click(i)
        pyautogui.click(181, 272)

    pyautogui.click(hero2)
    pyautogui.click(435, 266)

    # speed up
    pyautogui.click(speed)
    # pyautogui.click(start) round
    pyautogui.click(start)
    time.sleep(2)

    # build towers
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

    # click for next round
    time.sleep(7.5)        
    pyautogui.click(start)

    upgrade1st()

    # click for next round
    time.sleep(7.5)        
    pyautogui.click(start)


    upgrade2nd()
    finalupgrade()
    restart()



endall = time.time()
print('Game Ended after {} mins'.format(round((endall-startall)/60,2)))
# print(pyautogui.position())