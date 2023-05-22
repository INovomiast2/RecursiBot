import discord
from discord.ext import commands
from commands.commands import bot
from config.config import token
from utils.colors import *
from utils.date import formatted_date

# Activate bot
@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = "Recursion"))
	print(f"{bold}{light_gray}{formatted_date} {blue}INFO{reset}     {magenta}discord.botRunning {reset}{bot.user.name} is ready!")

# Invalid command
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("Invalid command. Type -help to see the available commands")
		print(f"{bold}{light_gray}{formatted_date} {red}ERROR    {reset}{magenta}discord.command {reset}Invalid command")


# Run bot
bot.run(token)
