### Imports
import pyautogui; pgui = pyautogui
from time import sleep
from selenium import webdriver

### Open Chrome, Full Screen, etc...
driver = webdriver.Chrome('/usr/local/obin/Share/chromedriver/77') # 75
driver.maximize_window()
pyautogui.click(x=1415, y=120)
pyautogui.hotkey('command', 'shift', 'b')

### Open URL
driver.get('https://userinyerface.com/')

### Main

## Index.html
sleep(5)
driver.find_element_by_class_name('start__link').click()

## Cookie
pgui.vscroll(-1)
# sleep(2)
# driver.find_element_by_class_name('button').click()

## PassWord
pgui.click(x=675, y=600)
pgui.hotkey('command', 'backspace')
# pgui.typewrite('KusaSugiWarota1010')
pgui.typewrite('A123456789')

## Mails
# write = ['kusaman.kusa', 'kusasugi']
for x in [630, 770]:
	pgui.click(x=x, y=650)
	pgui.hotkey('command', 'backspace')
	pgui.press('A')

## Select Com
pgui.click(x=870, y=650)
# pgui.moveTo(x=855, y=730)
# pgui.vscroll(-10)
pgui.click(x=855, y=720)

## Do not Accept, Next
pgui.click(x=585, y=710)
pgui.click(x=580, y=780)

## Select All
pgui.vscroll(1)
pgui.moveTo(x=215, y=380)
pgui.vscroll(-10)
for y in [295, 440, 585, 730]:
	for x in [430, 625, 820, 1010]:
		pgui.click(x=x, y=y)
pgui.click(x=715, y=885)

input('END\nEnter: ')
driver.quit()