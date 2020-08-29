npm install --save discord.js

mkdir $HOME/DiscordBot/

cat <<EOF > $HOME/DiscordBot/Bot.js
//Discord.js(JavaScript)
const discord = require('discord.js'), bot = new discord.Client(), prefix = bot_data[3];

var bot_data = ["Token", Client_ID, "Bot#1234", "!", "|Run: JavaScript|Prefix: !|"]

bot.on('ready', () => {bot.user.setGame(bot_data[4])});

bot.on('message', ms => {
  if (ms.content == prefix + 'Ping') {
    ms.reply('pong!');
  }
});

bot.login(bot_data[0]);

EOF

echo "node ~/Desktop/DiscordBot/Bot.js をやってください"
