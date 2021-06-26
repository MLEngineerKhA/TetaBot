import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="/")
token = os.getenv("DISCORD_BOT_TOKEN")


async def on_ready():
    await bot.change_presence(activity=discord.Game(name="a game"))
    print("I am online")

client.run(token)
