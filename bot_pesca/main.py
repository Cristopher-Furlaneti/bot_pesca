import pyautogui

from actions import check_poke_position, click_fish, get_loot, poke_atack, use_fishing_rod, use_pokeball, check_char_position


X_FISH = 647
Y_FISH = 552
RGB_FISH = (85, 230, 23)

MAX_ATTEMPT = 800
attempt = 0

while True:
    fish = pyautogui.pixelMatchesColor(X_FISH, Y_FISH, RGB_FISH)
    attempt = attempt + 1
    print(attempt)
    if fish:
        click_fish(X_FISH, Y_FISH)
        pyautogui.sleep(1.5)
        poke_atack()
        pyautogui.sleep(2)
        get_loot()
        use_pokeball()
        check_poke_position()
        check_char_position()
        pyautogui.sleep(1)
        use_fishing_rod()
        attempt = 0
    if attempt == MAX_ATTEMPT:
        use_fishing_rod()
        attempt = 0
        