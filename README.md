# Discord Bot to get Minecraft Server Status
A discord bot, programmed in Python, that sends the status of a Minecraft server to a Discord channel.

* `bot.py` adds the #status command functionality, which gets the status of the minecraft server and sends as an embed to a discord channel.
* `alerts.py` adds alert functionality, so that when the server starts/stops or a user joins/leaves it sends a message to a discord channel.

## Requirements
* [Discord](https://discordapp.com/) account
* Python
* A Minecraft server (see [this guide](https://codakid.com/how-to-make-a-minecraft-server/) for how to set up a Minecraft server)

### Python Dependencies
* [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html#installing)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [watchdog](https://pypi.org/project/watchdog/)

## Installation Steps
1. Clone repo
2. Go to [Discord Developers](https://discord.com/developers/applications/) and create a new application
3. Navigate to the bot tab, add a bot, and copy the token
4. Navigate to the OAuth2 tab, click "bot" under scopes and then "Send Messages" and "Read Message History" under bot permissions
5. Go to this URL, select which server you'd like to add the bot too and authorise
6. Create a new file called `.env` and add the following:
```
TOKEN=token_you_copied
ADDRESS=the_address_of_the_server
WEBHOOK=the_webhook_url
LOGPATH=the_path_of_your_server_log_file
```
7. Run the `bot.py` and `alert.py` files!

### Running bot.py on a Raspberry Pi
To run the bot.py file that gets the status of the server, I decided to run mine on a Raspberry Pi so that I could leave it running. The alert.py file needs to be on the machine running the server, as it needs to track file modifications.

#### Steps:
1. Make sure you have nohup and Python installed on your Pi and that the Python dependencies above are installed.

2. Clone repo to Raspberry Pi using
```
git clone https://github.com/davidbeechey/minecraft-server-discord-bot.git
```

3. Run
```
nohup python3 <path to bot.py file>/bot.py >> <path to bot.py file>/log.txt &
```
4. (optional) To run on boot, add that line to the end of `/etc/profile` using `sudo nano /etc/profile`
