ls = list()
with open('jpunicode.txt', mode='r') as f:
	file = f.read()
	for i in range(len(file)):
		ls[i] = file[i]

print(ls)