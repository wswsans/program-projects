#-*- using:utf-8 -*-
import time, pyautogui, subprocess, sys
pgui = pyautogui; cmd = subprocess
grep = lambda List, Name: [Ls for Ls in List if Name in Ls]

ls = list()
for X in range(1000):
	ls.append(chr(X))

if __name__ == '__main__':
	start = time.time()
	### CODE ###
	###  END  ###
	elapsed_time = time.time() - start 
	print ("elapsed_time: {0} [sec]".format(elapsed_time))