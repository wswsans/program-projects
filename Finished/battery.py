import subprocess
import time as t

# 'pmset -g ps'の結果を表示(list)
res = str(subprocess.check_output(['pmset', '-g', 'ps'])).split(" ")
desc = "とりあえず安全だね。"

# バッテリーの表示
battery = res[6][-4:-1]

#残りが、10%未満の時、最初に't'がつくため、削除
if battery[:1] == "t":
	battery = battery[1:]
	desc = "さっさと充電しろー!"
#バッテリー100%の時、00%になるため100%にする。
if battery == "00%":
	battery = "100%"
	desc = "安全だねー"

print("ただいまのバッテリーは", battery, "です")
print(desc)

#バッテリーかACアダプターのバッテリーどっち使ってるか表示
power = res[3][1:]

#充電中
if power == "AC":
	power = "充電中"
	if battery == "100%":
		desc = "さっさと充電機抜けー!"
	else:
		desc = "100%になったら抜くんだよ。"
#充電してない
if power == "Battery":
	power = "放置中"
	if len(battery) == 2:
		desc = "充電しろー!"
	else:
		desc = "10%未満になったら充電するんだよ"

print("今", power, "です")
print(desc)