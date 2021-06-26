import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="/")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("хорошую жену"))
    print("I am online")

client.run(token)
