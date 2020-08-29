from PIL import Image, ImageDraw
import cv2
import numpy as np
import math

FileName = input('File: ')

# 画像を読み込み
im = cv2.imread(FileName)

# サイズを取得
size = im.shape

# 白黒判定
QRList = list()
for Y in range(30, size[0] - 10, 20):
	QRList.append(str())
	for X in range(30, size[1] - 10, 20):
		# 0.0: 黒, 300.0: 白
		color = round(im[Y-10:Y+10, X-10:X+10].T[0:2].flatten().mean(), -2)
		QRList[-1] += {0.0: '1', 300.0: '0'}[color]
		# デバッグ用
		# print("{}/{}, {}/{}: {}" .format(Y,size[0], X,size[1], color))

# 書き込み
with open(FileName.split('.')[0] + '.txt', mode='w') as f:
	f.write('\n'.join(QRList))