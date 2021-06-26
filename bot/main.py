import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="/")
token = os.getenv("DISCORD_BOT_TOKEN")


async def on_ready():
    activity = discord.Game(name="Netflix", type=1)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("I am online")

client.run(token)
