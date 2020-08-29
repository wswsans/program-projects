def operating(Num_op, Num):
	if not 0<=Num<=95:
		return "error"
	nn = list("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()-^¥@[;:],./_=~|`{+*}<>? ") #Max94進数
	mod_rs = list("1")
	res = str()

	while not (mod_rs[len(mod_rs)-1]==0 and Num_op==0):
		mod_rs.append(Num_op%Num)
		Num_op = (Num_op-(Num_op%Num))//Num
	del mod_rs[:1]
	if len(mod_rs) != 1:
		del mod_rs[-1:]

	for i in range(len(mod_rs)):
		if mod_rs[len(mod_rs)-1-i] == 0:
			res = str(res)+"0"
		else:
			res += nn[int(mod_rs[len(mod_rs)-1-i])-1]

	return res

if __name__ == '__main__':
	print(operating(94, 95))