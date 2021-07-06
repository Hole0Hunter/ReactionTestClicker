import pyautogui, time
# co-ordinates of test start 935, 368
# green colour RGB values = 75, 219, 106
time.sleep(5)

# move to the required co-ordinates
pyautogui.moveTo(935, 368)

# click to start test
pyautogui.click()

while True:
    if pyautogui.pixelMatchesColor(935, 368, (75, 219, 106)):
        pyautogui.click()

