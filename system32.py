import disocord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
client = commands.Bot(command_prefix = "/")
@client.event
async def on_ready():
    print("Im Hack Bot please like me")
    await client.change_Presence(game=discord.Game(name="Playing With NabzGT#9028"))

@client
async def trainer(ctx, user: discord.Member):
    await bot.send_message(message.channel, "Oh Want Trainer Go Fuck Ur ass")
