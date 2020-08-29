gem install discordrb

git clone https://github.com/sstephenson/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc

git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

mkdir $HOME/DiscordBot/

cat <<EOF > $HOME/DiscordBot/Bot.rb
bot_data = "Token", Client_ID, "Bot#1234", "!", "|Run: Ruby|Prefix: !|"

p "https://discordapp.com/api/oauth2/authorize?client_id=#{bot_data[1]}&permissions=8&scope=bot"
$:.unshift(File.dirname(File.expand_path(__FILE__)))
$dir = File.dirname(File.expand_path(__FILE__))

require "discordrb"
require "csv" #CSV作るときめっちゃ楽!

$bot = Discordrb::Commands::CommandBot.new Name: bot_data[2], client_id: bot_data[1], token: bot_data[0], prefix: bot_data[3], command_doesnt_exist_message: ("このコマンドは存在しません")
$bot.ready do |e|
    $bot.game = bot_data[4]
end

# イベントから様々な値が取得できる
# http://www.rubydoc.info/gems/discordrb/Discordrb/Events/MessageEvent
$bot.command(:default) do |e|
    # コマンド実行時の処理
    e.respond "こんにちは"
end

$bot.command(:Test, description: '発言できるかテスト') do |e|
    e.respond "Test <@#{e.user.id}>"
    e.respond "```**Bold** _italic_ __UnderBar__ ~~Slice~~ `Code` CodeBlock```\n**Bold** _italic_ __UnderBar__ ~~Slice~~ `Code` ```CodeBlock```"
end

$bot.run
EOF

echo "ruby ~/Desktop/DiscordBot/Bot.rb をやってください"
