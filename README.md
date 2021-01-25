# Discord Bot to get Minecraft Server Status
A discord bot programmed in Python that checks the status of a minecraft server and sends as an embed to a Discord channel with a command.

## Requirements
* [Discord](https://discordapp.com/) account
* Python

### Dependencies
* [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html#installing)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation Steps
1. Clone repo
2. Go to [Discord Developers] (https://discord.com/developers/applications/) and create a new application
3. Navigate to the bot tab, add a bot, and copy the token
4. Navigate to the OAuth2 tab, click "bot" under scopes and then "Send Messages" and "Read Message History" under bot permissions
5. Go to this URL, select which server you'd like to add the bot too and authorise
6. Create a new file called `.env` and add the following:
```
TOKEN=token_you_copied
ADDRESS=the_address_of_the_server
```
7. Run!

