import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="/")
token = os.getenv("DISCORD_BOT_TOKEN")


async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("хорошую жену"))
    print("I am online")

client.run("ODU2MDQ4NjA2MzMwNDg2ODE0.YM7XZA.6bV0SogRCr-FV-WkHzoyOt5Ma8c")
