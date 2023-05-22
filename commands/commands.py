import discord
from discord.ext import commands
from config.config import prefix

# Defines 
bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all(), description = f"Use {prefix}help to show help list")

# Deletes messages
@bot.command()
async def clear(ctx, amount = 5):
	await ctx.channel.purge(limit = amount + 1)

# Close the bot
@bot.command()
async def close(ctx):
	print("Recursion finished")
	await ctx.send("I'm done")
	await bot.close()