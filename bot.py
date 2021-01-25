import discord
import urllib.request
import json
from datetime import datetime

client = discord.Client()

def server_status():

    response = urllib.request.urlopen(f"https://api.mcsrvstat.us/2/86.136.87.58:25566")
    data = json.load(response)
    online: bool = data['debug']['ping']
    # If not online skip this
    if online:
        motd = data['motd']['clean'][0].strip()
        version = data['version']
        online_players = data['players']['online']
        max_players = data['players']['max']
        try:
            player_names = data['players']['list']
        except:
            player_names = "No players :("
        return motd, version, online_players, max_players, player_names

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    command: str = message.content
    if command.startswith("#status"):
        # Ok, we are going to start here
        print("Executing command: {0}".format(command))

        try:
            motd, version, online_players, max_players, player_names = server_status()
            print(motd, version, online_players, max_players)
        except Exception as e:
            await message.channel.send("Sorry, but I can't find minecraft server with this ip :c")
            print("Failed to find server: {0}".format(e))
            return

        if player_names == "No players :(":
            players = player_names
        else:
            players = ' '.join(str(e) for e in player_names)

        # And the best part - send response!
        #### Create the initial embed object ####
        embed=discord.Embed(title="Server Status", description=f"The server is up!\n{motd}", color=0x109319)

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name="Minecraft Server", icon_url="https://static.wikia.nocookie.net/minecraft/images/f/fe/GrassNew.png/revision/latest/scale-to-width-down/340")

        embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft/images/f/fe/GrassNew.png/revision/latest/scale-to-width-down/340")

        embed.add_field(name="Players", value=f"{online_players}/{max_players}", inline=True)
        embed.add_field(name="Version", value=version, inline=True)
        embed.add_field(name="Online Players", value=players, inline=False)
        embed.add_field(name="Address", value="86.136.87.58:25566", inline=True)

        now = datetime.now()
        current_time = now.strftime("%a %d %b %H:%M")

        embed.set_footer(text=f"{current_time}")
            
        await message.channel.send(embed=embed)

client.run("ODAyOTY4MTI0MjY4NzQwNjA4.YA28Vw.4-J6cegShmRjrDedrJCXPGbPtG8")
