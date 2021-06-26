import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="/")
token = os.getenv("DISCORD_BOT_TOKEN")


async def on_ready():
    await client.change_presence(activity=discord.Game('Sea of Thieves'))
    print("I am online")

client.run(token)
