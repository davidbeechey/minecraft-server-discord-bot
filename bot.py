import discord
import urllib.request
import json
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

address = os.getenv('ADDRESS')
token = os.getenv('TOKEN')

client = discord.Client()

def server_status():

    # Get details of the mc server
    response = urllib.request.urlopen(f"https://api.mcsrvstat.us/2/{address}")
    data = json.load(response)
    online = data['debug']['ping']

    # If not online skip this
    if online:
        motd = data['motd']['clean'][0].strip()
        version = data['version']
        online_players = data['players']['online']
        max_players = data['players']['max']

        # Try to get the players online, if there aren't any say "No players :("
        try:
            player_names = data['players']['list']
        except:
            player_names = "No players :("

        # Return the details of the server
        return motd, version, online_players, max_players, player_names

@client.event
async def on_ready():
    print("Bot is ready!")
    discord.Game(name="the server :)")

@client.event
async def on_message(message):

    # Get message content
    command = message.content

    # '#status' command
    if command.startswith("#status"):
        print("Executing command: {0}".format(command))

        # Try to get the details of the server
        try:
            motd, version, online_players, max_players, player_names = server_status()
        # Can't find server
        except Exception as e:
            await message.channel.send("Sorry, the server isn't up :(")
            print("Failed to find server: {0}".format(e))
            return

        # If there are players then format them into a string
        if player_names == "No players :(":
            players = player_names
        else:
            players = ' '.join(str(e) for e in player_names)

        # Create the initial embed object
        embed=discord.Embed(title="Server Status", description=f"Hi {message.author}, the server is up!", color=0x109319)

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name="Minecraft Server", icon_url="https://static.wikia.nocookie.net/minecraft/images/f/fe/GrassNew.png/revision/latest/scale-to-width-down/340")

        embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft/images/f/fe/GrassNew.png/revision/latest/scale-to-width-down/340")
        
        # Add the fields
        embed.add_field(name="MOTD", value=motd, inline=False)
        embed.add_field(name="Players", value=f"{online_players}/{max_players}", inline=True)
        embed.add_field(name="Online Players", value=players, inline=True)
        embed.add_field(name="Version", value=version, inline=False)
        embed.add_field(name="Address", value="86.136.87.58:25566", inline=True)

        # Get the time and add as footer
        now = datetime.now()
        current_time = now.strftime("%a %d %b %H:%M")
        embed.set_footer(text=f"{current_time}")
        
        # Send the embed to the discord channel
        await message.channel.send(embed=embed)

client.run(token)
