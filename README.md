## Castle Defense 2 bot

Games nowadays usually require insane amount of time to farm resources for upgrading and purchase of items. For mobile games especially, it is harder to write a bot since the script will have to be ported over to the phone.

There are two ways to overcome this. One is to install the mobile OS in a virtual machine in a PC; second is to mirror the mobile OS into the PC. Then the script is  ran in a PC environment.

The python library pyautogui help to simulate mouse-clicks on the window so that a rule-based system based on clicking an x,y coordinate can be coded. This example uses stage **15-3** of the game **Castle TD2**. It will build and upgrade all towers to reach the last level in the stage but not completing it (completing a stage drastically reduces the amount of diamonds collected on subsequent tries).

To further automate the bot, I used periodic screenshots and various image recognition techniques on the images to decide on various actions.

#### Using OCR

I have added a level of intelligence to the bot using object character recognition (OCR). The script crop the screenshot to a specific popup message in order to detect if the game has ended so that it can auto restart.

#### Using RBG Histogram Quantities

The 2nd level of intelligence, while a rudimentary form of classification, is effective by using cropped screenshots to recognise the colours of a particular image. I used pillow and numpy to grab the first count of histogram bar to identify the back button. This button might be at two different positions because the phone will switch from landscape to mobile depending on the auto-advertisement being shown.

#### Template Matching

I also employed template matching so that I can obtain the coordinates to build the towers by having an image of a tower-construction image and match against an initial screenshot of the map. This was done using skimage normalized cross-correlation. Refer to [here](https://github.com/mapattacker/cheatsheets/blob/master/python/skimage-tutorial.ipynb) on how the code works (go to template matching section).

### Dependencies
__Python__: pyautogui, pytesseract, skimage, pillow, numpy

__Chrome Vysor__: mobile mirroring software

![screenshot](https://github.com/mapattacker/castletd2-bot/blob/master/img/Screenshot.png)

![template matching](https://github.com/mapattacker/castletd2-bot/blob/master/img/templatematch.png)