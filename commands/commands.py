import discord
import datetime
from discord.ext import commands
from config.config import prefix
from utils.colors import *

# Get the current day
date = datetime.datetime.now()

# Format the current day
formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")

# Define the bot
bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all(), description = f"Use {prefix}help to show help list")

# Delete messages
@bot.command()
async def clear(ctx, amount = 5):
	await ctx.channel.purge(limit = amount + 1)
	await ctx.send(f"{ctx.author.mention} deleted {amount} messages")
	print(f"{bold}{light_gray}{formatted_date} {green}LOG      {reset}{magenta}discord.command {bold}{white}[{ctx.author.top_role}] {blue}{ctx.author.name}: {red}deleted {reset}{amount} messages from {ctx.channel.name}")

# Close the bot
@bot.command()
async def close(ctx):
	print("Recursion finished")
	await ctx.send("I'm done")
	await bot.close()