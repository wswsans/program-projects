from subprocess import check_output

stop = input('閉じる単語: ')

# try:
# 	check_output(['chrome-cli'])
# except Exception as e:
# 	print('Chrome-Cli がインストールされてません')
# 	check_output(['exit', '1'])

while True:
	tabs = str(check_output(['chrome-cli', 'list', 'links']))[2:-1].split('\\n')
	i = 0
	for n in tabs:
		if stop in n:
			check_output(['chrome-cli', 'close', '-t', list(reversed(tabs[i].split(']')[0][1:].split(':')))[0]])
			print('Closed: ' + n)
		i += 1