import discord
from discord.ext import commands

discord_token = "MTE5MjY2MjgyMDc1MjQ1NzgyOA.GfT_AS.43aKe7z2z0bOGscnvFoXTTExB91wde4jN8-aKo"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="mention!", intents=intents)

looping = False

@bot.command()
async def start(ctx):
    global looping
    looping = False
    while not looping:
        await ctx.send("@everyone hi!")

@bot.command()
async def stop(ctx):
    global looping
    looping = True

@bot.command()
async def helpme(ctx):
    messages = """
```
mention!help - Show all available commands
```
"""
    await ctx.send(messages)

@bot.event
async def on_ready():
    print("I'm ready to annoying everyone")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name = "mention!help"))

bot.run(discord_token)
