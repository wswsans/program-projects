# Imports
import pyautogui as pgui
from time import sleep
import selenium
from selenium import webdriver
Keys = webdriver.common.keys.Keys

# SiteSet
ID = {
	'サイバーサンダーサイダー': 23829,
	'初音ミクの消失': 17156,
	'初音ミクの激唱': 24409,
	'初音ミクの暴走': 27646,
	'残酷な天使のテーゼ': 24666,
	'シャルル': 21925,
	'ロストワンの号哭': 24061,
	'千本桜': 19319
}
ct = 0
for Name in list(ID.keys()):
	ct += 1
	print(str(ct) + '.', Name, end='\n')
Num = int(input('この中の番号を選んでください\n>>> '))
ID = str(ID[list(ID.keys())[Num - 1]])
# ID = str(input('https://typing-tube.net/ の曲のIDを入力してください\n>>> '))

# Open Window
driver = webdriver.Chrome('/usr/local/obin/Share/chromedriver/79') # 74
driver.maximize_window()
pgui.click(x=1415, y=120)
pgui.hotkey('command', 'shift', 'b')

# Open URL
driver.get('https://typing-tube.net/movie/show/' + ID)
sleep(5)
for X in range(14):
	driver.find_element_by_xpath('/html/body').send_keys(Keys.DOWN)
driver.find_element_by_xpath('//*[@id="playBotton2"]/a[1]').click()
while True:
	try:
		text = driver.find_element_by_xpath('//*[@id="kashi_roma"]').text
		if (' ' in text) or (text == ''):
			continue
		print(text)
		driver.find_element_by_xpath('/html/body').send_keys(text)
	except KeyboardInterrupt:
		print('\nQuit!')
		break
	except selenium.common.exceptions.NoSuchElementException:
		pass
	except Exception as e:
		print('Error\n', e)
		break
		raise e

# End
driver.quit()
