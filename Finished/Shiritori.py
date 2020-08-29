print('Hello World!')
Check = True
words = []
head = input('最初の文字はなんですか\n>>> ')
print('それでは始めてください\n', head)
while Check:
	inp = input(head[-1] + ' > ')
	if inp == '':
		print('何も打たないとかまじ?')
	elif (inp[0] != head[-1]) or (inp in words):
		Check = False
		print('負けです')
	else:
		words.append(inp)
		head = inp

print('終わり')