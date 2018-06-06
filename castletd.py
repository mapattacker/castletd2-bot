import pyautogui
import time
from PIL import Image
import pytesseract
import os
import numpy as np
from skimage.color import rgb2gray
from skimage.feature import match_template
from skimage.io import imread
import pyautogui


startall = time.time()
# get screen resolution
screensize = pyautogui.size()
# define initial OCR text variable
text = '1'
# speed button
speed = (552, 98)
# screenshot directory
img_path = r'screen.png'
img_path_button = r'button.png'
img_path_template= r'template_match.png'
screenshot = "screencapture {}".format(img_path)
screenshot_button = "screencapture {}".format(img_path_button)
screenshot_template = "screencapture {}".format(img_path_template)
# cropping of screenshots
wood = (70, 180, 150, 210)
end_msg = (450, 300, 780, 360)
horizontal_button = (0,800,100,870)
vertical_button = (0,1400,80,1450)
map = (10,210,1240,690)
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


def take2nd(elem):
    return elem[1]

def templatematching():
    # extract coordinates of all tower positions
    os.system(screenshot_template)
    # get screenshot & crop to reduce search area
    img = imread(img_path_template)
    img = rgb2gray(img)


    # find ratio of screen resolution with screenshot resolution
    ratio = screensize[0] / img.shape[1]

    cropped = img[0:650, 0:1230]
    # read in template
    sign = imread('sign.png')


    # Template matching, results gives a correlation coefficient for all pixels in image
    result = match_template(cropped, sign)
    # Flatten, sort, and top 20 coefficient values'
    d = result.flatten()
    e = np.sort(d)[::-1][:20]

    # extract all coordinates
    list = []
    for i in e:
        # locate indexes from top 10 values
        top = np.argwhere(d==i)[0][0]
        # obtain coordinates from index
        ij = np.unravel_index(top, result.shape)
        # swap position as it is in (y, x)
        x, y = ij[::-1] 
        # centre the image based on template shape
        h, w = sign.shape
        x = int(x+h/2)
        y = int(y+w/2)
        list.append((x,y))

    # remove all duplicates
    list2 = list
    value = 5
    for i in list2:
        x = i[0]
        y = i[1]

        for i2 in list2:
            x2 = i2[0]
            y2 = i2[1]
            # if same coordinates do not remove as comparing same point
            if x-x2 == 0 and y-y2 == 0:
                continue
            # if coordinates are very similar, likely to be duplicates; remove
            elif -value <= x-x2 <= value and -value <= y-y2 <= value:
                list2.remove(i2)
    
    # change the coordinates of screenshot to actual computer screen coordinates
    list2 = [(one * ratio, two * ratio) for one, two in list2]
    # order it such that it builds from bottom to top
    return sorted(list2, reverse=True, key=take2nd)

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
    # change tpositions into nparray so that can use np.histogram
    rbg = np.array(cropped.histogram())
    # get the first binned quantity
    return int(np.histogram(rbg, bins=200, range=(0,500))[0][0])

def upgrade1st():
    # 1st tower upgrade
    for i in tpositions:
        a = i
        pyautogui.click(a)
        time.sleep(0.5)
        z = upgrade[1]
        pyautogui.click(a[0]+z[0],a[1]+z[1])
        time.sleep(0.5)
        pyautogui.click(a[0]+z[0],a[1]+z[1])
        for aa in range(5):
            pyautogui.click(start)
            time.sleep(1)

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
        for i in tpositions:
            a = i
            pyautogui.click(a)
            time.sleep(0.5)
            z = upgrade[2]
            pyautogui.click(a[0]+z[0],a[1]+z[1])
            time.sleep(0.5)
            pyautogui.click(a[0]+z[0],a[1]+z[1])
            for aa in range(7):
                pyautogui.click(start)
                time.sleep(1)

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
        for zz, i in enumerate(tpositions):
            # remove 2 towers upgrade so it won't kill the boss
            if zz != 2 and zz != 3 and zz != 4:
                a = i
                pyautogui.click(a)
                time.sleep(0.5)
                z = upgrade[3]
                pyautogui.click(a[0]+z[0],a[1]+z[1])
                time.sleep(0.5)
                pyautogui.click(a[0]+z[0],a[1]+z[1])
                for aa in range(5):
                    pyautogui.click(start)
                    time.sleep(1)

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
        

def restart(num):
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

    for i in range(8):
        objectrecognition()
        time.sleep(3)
        if text == 'Defeat':
            # click restart button if it appears
            print('Restart Button Detected')
            pyautogui.click(restartbutton)
            break
        # account for vertical rotation when displaying ads
        # previous histogram testing shown the quantity of colors fall within 980-1050
        elif 980 < colorrecognition(vertical_button) < 1050:
            print ('Vertical Ad Detected')
            time.sleep(1)
            pyautogui.click(backbuttonV)
            time.sleep(3)
        elif 980 < colorrecognition(horizontal_button) < 1050:
            print ('Horizontal Ad Detected')
            time.sleep(1)
            pyautogui.click(backbutton)
            time.sleep(3)

    endt = time.time()
    if num == 1:
        print (num, 'round down,', 360*num, 'diamonds earned! after',round((endt-startt)/60,2), 'mins')
    else:
        print (num, 'rounds down,', 360*num, 'diamonds earned! after', round((endt-startt)/60,2), 'mins')


# get all tower coordinates
tpositions = templatematching()

# select vysor screen
pyautogui.click(tpositions[0])


# define number of rounds to loop
for num in range(1,10):
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
    for i in tpositions:
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
    for aa in range(6):
        pyautogui.click(start)
        time.sleep(1)

    upgrade1st()

    # click for next round
    for aa in range(7):
        pyautogui.click(start)
        time.sleep(1)

    upgrade2nd()
    finalupgrade()
    restart(num)



endall = time.time()
print('Game Ended after {} mins'.format(round((endall-startall)/60,2)))
# print(pyautogui.position())