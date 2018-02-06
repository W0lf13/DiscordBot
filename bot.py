#
# Filename: bot.py
# DateCreated: 2018/01/29
# Author: Wolf
# Description: Playing around with a discord bot, basic connection, and commands testing
#

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

Client = discord.Client
#bot_prefix = "?"
bot_prefix = ""
client = commands.Bot(command_prefix=bot_prefix)
player = None


# function fires when bot has connected to the server, and is ready to operate
@client.event
async def on_ready():
    print('Bot online!')
    print('Name: ' + str(client.user))
    print('ID: ' + str(client.user.id))


# basic text back command
@client.command(pass_context=True)
async def ping(ctx):
    await client.say('Ping!')


# connects to an audio channel, and starts stream playing a youtube song
@client.command(pass_context=True)
async def play():
    await client.say('Joining General audio channel')

    channel = client.get_channel('406445255991492613')
    voice = await client.join_voice_channel(channel)

    await client.say('Playing some random music')

    global player
    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=5lLclBfKj48')
    #player = voice.create_ffmpeg_player('cool.mp3')
    #stream_player()
    player.volume = 0.1
    player.start()
    print('done')
    volup()


# Increases the players volume in an increment of 0.1
@client.command(pass_context=True)
async def volup():
    global player
    if player != None:
        player.volume += 0.1


# Decreases the players volume in an increment of 0.1
@client.command(pass_context=True)
async def voldown():
    global player
    if player != None:
        player.volume -= 0.1



#client.run("BOT TOKEN")
client.run("NDA2NDUxMDkyMzc3OTYwNDUz.DVBvzg.y3hSwBVDTtGadenQo5fVH7pvxY8")
