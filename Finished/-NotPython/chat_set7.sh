#!/bin/bash

carent=$PWD
dummy=${DOCOMO_API_KEY:="NO"}
if [ -z $DCOMO_API_KEY=="NO" ]; then
	echo -e "DOCOMO_API_KEYがセットされてません! \nDOCOMO_API_KEY をセットします\nAPI Keyを入力してください"
	echo -n "API_KEY: "; read api_key
	echo "export DOCOMO_API_KEY=${$api_key}" >> ~/.bashrc; source ~/.bashrc
fi
echo "DOCOMO_API_KEY が読み込めました"

dummy=${DOCOMO_APP_ID:="NO"}
if [ -z $DCOMO_APP_ID=="NO" ]; then
	echo -e " DOCOMO_APP_IDがセットされてません!(Enterでスタート)"; read dummy
	cd dora-engine/; appid_res=$(./setup-docomo-appid.sh)
	if [ $appid_res = "" ]; then ###未完成
		echo "エラー! 終了します"
		exit 0
	fi
	echo $appid_res >> app_id.txt; app_id=${appid_res:7:36}
	echo "export DOCOMO_APP_ID=${$app_id}" >> ~/.bashrc; source ~/.bashrc
fi
echo "DOCOMO_APP_ID が読み込めました"


cd /etc/default/; sudo touch robot-server; sudo chmod 777 robot-server 
cat <<_EOF_ > /etc/default/robot-server
DOCOMO_API_KEY=$DOCOMO_API_KEY
DOCOMO_APP_ID=$DOCOMO_APP_ID
_EOF_
echo "RobotServer 書き込み完了"


sudo cat /lib/systemd/system/robot-server.service | tr -d '#'
echo "service 書き込み完了"

cd $carent

echo "ダンボールロボットの中で使う名前を教えてください"
echo -n "Name: "; read danball_name
cat <<EOF > $HOME/Documents/$danball_name/
/*チャットプログラム*/
ゆっくりしていってね

:loop
/speech-to-text/:例外発生
/goto/:成功

:例外発生
ききとれませんでした
/goto/:end

:成功
/chat
/text-to-speech
/goto/:loop

:end
/goto/:loop
EOF

echo "sudo reboot をしてください"