import discord

discord_token = "MTE5MjY2MjgyMDc1MjQ1NzgyOA.GZWuLN.kOFbWk9Gf4E6PuvzQKoSNORVNIFQeY2nL2m86I"

intents = discord.Intents.all()
bot = discord.Bot(command_prefix="mention!")

@bot.command()
async def test(ctx):
    await ctx.send("@everyone hi!")
@bot.command()
async def help(ctx):
    messages = """
```
mention!help - Show all available commands
```
"""
    await ctx.send(messages)

@bot.event
async def on_ready():
    print("I'm ready to annoying everyone")
    await bot.change_presence(activity=discord.activity(type=discord.ActivityType.playing, name = "mention!help"))

bot.run(discord_token)
