from Gengo import *

print('西暦-> 元号 変換')

try:
	Seireki = int(input('西暦を入力: '))
except ValueError:
	quit('数字入力しろ')

Result = [Seireki, '無し', '未来', 'みらい']

for m in list(GengoList.keys()):
	for n in GengoList[m]:
		if Seireki >= n:
			Result = [Seireki, m, GengoList[m][n][0], GengoList[m][n][1]]

print('西暦', Result[0], '年\n', '時代区分:', Result[1], ' 漢字:', Result[2], ' 平仮名:', Result[3])