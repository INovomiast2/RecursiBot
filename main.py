import discord
from config.config import token
from commands.commands import bot

# Define bot
@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Game(name = "Visual Studio Code"))
	print("RecursiBot is ready!")

# Run bot
bot.run(token)