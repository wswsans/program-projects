from PIL import Image, ImageDraw

FName = input('File: ')
with open(FName, mode='r') as f:
	FILE = f.read().split('\n')

# ますの数 * 20px
COL = (len(FILE) + 2) * 20

# 真っ白な画像を作成
im = Image.new('RGB', (COL, COL), (255, 255, 255))
draw = ImageDraw.Draw(im)

x = y = 20
for Y in FILE:
	for X in Y:
		# COL = 1: 黒, 0: 白
		COL = [(255, 255, 255), (0, 0, 0)][int(X)]
		# 横に並べてく
		draw.rectangle((x, y, x + 20, y + 20), fill=COL, outline=COL)
		x += 20
	# 一行下へ
	y += 20
	x = 20

# 完成品を書き出し
im.save('{}.jpg'.format(FName.split('.')[0]), quality=95)