import pyautogui
import time

def screenshot_pages():
    pyautogui.click()       # mouse click to change active window to the pdf
    for i in range(16):     # number of times loop happens = number of pages
        time.sleep(0.75)    # slight delay to let next page fully load before taking screenshot
        filename = 'images/screenshot' + str(i + 1) + '.png'
        im = pyautogui.screenshot(filename, region = (1185, 175, 1428, 1850))    # takes screenshot of the page
        # region is the area of the screen to screenshot, region = (top_left_x, top_left_y, width, height)
        pyautogui.press('right')    # moves on to the next page

if __name__ == "__main__":
    screenshot_pages()
