import pyautogui
import random
import winsound
import os
from datetime import datetime

X_BELLOSOM = 805
Y_BELLOSOM = 518
RGB_BELLOSOM = (109, 194, 192)

X_CHAR = 959
Y_CHAR = 534
RGB_CHAR = (14,14,14)

USE_POKEBALL = True

POKE_DEAD_POSITION = [(883, 528),(870, 597)]
BP_LOOT_POSITION = [(1703, 675),(1705, 749)]

LIST_ATACK = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
LIST_OCEAN_POSITION = (645,443)


def click_fish(x_fish, y_fish):
    pyautogui.moveTo(x_fish, y_fish)
    pyautogui.click()

def poke_atack():
    pyautogui.press(LIST_ATACK)

def get_loot():
    pyautogui.moveTo(POKE_DEAD_POSITION[0])
    pyautogui.click(button='right')
    pyautogui.sleep(0.8)
    pyautogui.moveTo(BP_LOOT_POSITION[0])
    pyautogui.click(clicks=5)
    pyautogui.sleep(0.8)
    pyautogui.moveTo(POKE_DEAD_POSITION[1])
    pyautogui.sleep(0.8)
    pyautogui.moveTo(BP_LOOT_POSITION[1])

def use_pokeball():
    if USE_POKEBALL:
        pyautogui.moveTo(POKE_DEAD_POSITION[0])
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.click()
        pyautogui.sleep(1)
        pyautogui.moveTo(POKE_DEAD_POSITION[1])
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.click()




def check_poke_position():
    poke = pyautogui.pixelMatchesColor(X_BELLOSOM, Y_BELLOSOM, RGB_BELLOSOM)
    if not poke:
        pyautogui.press('f11')
        pyautogui.sleep(0.8)
        pyautogui.moveTo(X_BELLOSOM, Y_BELLOSOM)
        pyautogui.click()

def use_fishing_rod():
    pyautogui.press('delete')
    pyautogui.moveTo(LIST_OCEAN_POSITION)
    pyautogui.click()

def check_char_position():
    char = pyautogui.pixelMatchesColor(X_CHAR,Y_CHAR, RGB_CHAR)
    if not char:
        pyautogui.moveTo(X_CHAR, Y_CHAR)
        pyautogui.click()