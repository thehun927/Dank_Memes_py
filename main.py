import pyautogui
import time
from numpy import random


def main():
    pyautogui.write('p beg')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('p dig')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('p fish')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('p hunt')
    pyautogui.press('enter')


def postmeme():
    pyautogui.write('p postmeme')
    pyautogui.press('enter')
    time.sleep(1)
    with pyautogui.hold('shift'):
        pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
    pyautogui.press('enter')


def search():
    pyautogui.write('p search')
    pyautogui.press('enter')
    time.sleep(1)
    with pyautogui.hold('shift'):
        pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.press('enter')


def crime():
    pyautogui.write('p crime')
    pyautogui.press('enter')
    time.sleep(1)
    with pyautogui.hold('shift'):
        pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.press('enter')


def save():
    pyautogui.write('p deposit all')
    pyautogui.press('enter')


def rest():
    rand = random.randint(16, 58)
    time.sleep(rand)


x = 0
while x < 1:
    time.sleep(3)
    search()
    time.sleep(1)
    save()
    time.sleep(1)
    crime()
    time.sleep(1)
    postmeme()
    time.sleep(1)
    main()
    time.sleep(1)
    save()
    rest()
