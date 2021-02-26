import discord
from discord.ext import commands
import requests
from requests.api import request
import random
import os

# Client (our bot)
client = commands.Bot(command_prefix='!openroom ')
client.remove_command('help')
ohcolor = discord.Color.from_rgb(239, 92, 52)
# gifs
gify = ["https://gph.is/g/aQQDGMV",
        "https://gph.is/g/E0WYq8o",
        "http://gph.is/2uu95WB",
        "http://gph.is/2aguawW",
        "https://gph.is/g/4bjzgmo",
        "http://gph.is/1CBEAKL"]
l = len(gify)
helptxt = " \"!openroom startjam <topic_without_spaces>\" "
support = "Reach out to admins/openhouse reps"


@client.command(name='startjam')
async def startjam(context, *, message):
    i = random.randint(0, 5)
    await context.message.channel.send(gify[i])
    print("test")
    print(context.message.content)
    str1 = context.message.content
    temp = str1.split()
    str2 = temp[2]
    author_id = context.message.author
    payload = {
        "type": "group_study"
    }
    url = "https://meets.api.openhouse.study/create/"
    request = requests.post(
        url, headers={"Content-Type": 'application/json'}, params={}, json=payload)
    linkopenroom = request.json()["room_url"]
    print(linkopenroom)
    myEmbed = discord.Embed(title="OpenRoom", color=ohcolor)
    myEmbed.add_field(name="Session by", value=author_id)
    myEmbed.add_field(name="Topic", value=str2, inline=False)
    myEmbed.add_field(name="Joining Link", value=linkopenroom, inline=False)
    myEmbed.set_footer(text='powered by openhouse')
    await context.message.channel.send(embed=myEmbed)
    str2 = ""
# 0x00ff00


@client.command(pass_context=True)
async def help(context):
    myEmbed = discord.Embed(title="OpenRoom Faq", color=ohcolor)
    myEmbed.add_field(name="How to start a session?", value=helptxt)
    myEmbed.add_field(name="Any other questions?", value=support, inline=False)
    myEmbed.set_footer(text='powered by openhouse')
    await context.channel.send(embed=myEmbed)
# Checking if the bot is online


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('? nope. Studying at Openroom'))
    print('Pikachu!')

# Run the bot on server
client.run(os.environ['DISCORD_TOKEN'])
