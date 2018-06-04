## Castle Defense 2 bot

Games nowadays usually require insane amount of time to farm resources for upgrading and purchase of items. For mobile games especially, it is harder to write a bot since the script will have to be ported over to the phone.

There are two ways to overcome this. One is to install the mobile OS in a virtual machine in a PC; second is to mirror the mobile OS into the PC. Then the script is  ran in a PC environment.

The python library pyautogui help to simulate mouse-clicks on the window so that an entirely rule-based system based on clicking an x,y coordinate can be coded. This example uses stage **15-3** of the game **Castle TD2**. It will build and upgrade all towers to reach the last level in the stage but not completing it (completing a stage drastically reduces the amount of diamonds collected on subsequent tries). 

I have added a level of intelligence to the bot using object character recognition (OCR). The script takes screenshots of the game periodically and crop the image to a specific popup to detect if the game has ended so that it can auto restart.

The next level of the bot is to employ image recognition so that I can command the bot to a next level of automation. Stay tune!

### Dependencies
__Python__: pyautogui, pytesseract, pillow

__Chrome Vysor__: mobile mirroring software

![screenshot](https://github.com/mapattacker/castletd2-bot/blob/master/Screenshot.png)