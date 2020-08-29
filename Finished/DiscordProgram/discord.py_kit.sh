pip3 install virtualenv
pip3 install virtualenvwrapper

cat <<EOF > ~/.bash_profile
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
EOF
cat <<EOF > ~/.bashrc
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
EOF

mkvirtualenv --python=`which python3` main

pip install -U ipython

# /Applications/Python\ 3.6/Install\ Certificates.command
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 << "EOF"

# install_certifi.py
#
# sample script to install or update a set of default Root Certificates
# for the ssl module.  Uses the certificates provided by the certifi package:
#       https://pypi.python.org/pypi/certifi

import os
import os.path
import ssl
import stat
import subprocess
import sys

STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
             | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
             | stat.S_IROTH |                stat.S_IXOTH )

def main():
    openssl_dir, openssl_cafile = os.path.split(
        ssl.get_default_verify_paths().openssl_cafile)

    print(" -- pip install --upgrade certifi")
    subprocess.check_call([sys.executable,
        "-E", "-s", "-m", "pip", "install", "--upgrade", "certifi"])

    import certifi

    # change working directory to the default SSL directory
    os.chdir(openssl_dir)
    relpath_to_certifi_cafile = os.path.relpath(certifi.where())
    print(" -- removing any existing file or link")
    try:
        os.remove(openssl_cafile)
    except FileNotFoundError:
        pass
    print(" -- creating symlink to certifi certificate bundle")
    os.symlink(relpath_to_certifi_cafile, openssl_cafile)
    print(" -- setting permissions")
    os.chmod(openssl_cafile, STAT_0o775)
    print(" -- update complete")

if __name__ == '__main__':
    main()
EOF

pip install -U discord.py

mkdir $HOME/DiscordBot/

cat <<EOF > $HOME/DiscordBot/Bot.py
import discord
from discord.ext.commands import Bot
from discord.ext import commands

bot_data = ["Token", Client_ID, "Bot#1234", "!", "|Run: Python|Prefix: !|"]

Client = discord.Client()
client = commands.Bot(command_prefix=bot_data[3])

@client.event
async def on_ready():
	print("Login\nName: {0} ID: {1}".format(client.user.name, client.user.id))
	await client.change_presence(game=discord.Game(name=bot_data[4]))

async def on_message(message):
	if message.content == "Ping!":
		await client.say("Pong!")
	print("Message: {0}\nby.{1}\nServer/CH: {2}/{3}".format(message.content, message.user, message.server, message.channel))


@client.command(pass_context=True)
async def ping():
	await client.say("Pong!")

client.run(bot_data[0])
EOF

echo "python ~/Desktop/DiscordBot/Bot.py をやってください"
