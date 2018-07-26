import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

client = discord.Client()
bot = commands.Bot(command_prefix = "$")
# offline Variables
# botchannel = '470686765485785090'
# botid = '235088799074484224'
# bottoken = "NDcwODU4Nzc1NDUzMTA2MTg2.Djc1fQ.ogW4NrDpTRS0sPWEoX37LBtUuks"
# gamename = 'Mauerbausimulator 1961'

# Heroku variables
botchannel = os.environ['BOTCHANNEL']
botid = os.environ['BOTID']
bottoken = os.environ['BOTTOKEN']
gamename = os.environ['GAMENAME']

@bot.event
async def on_ready():
	print("Bot is ready")
	print(discord.__version__)
	await bot.change_presence(game=discord.Game(name=gamename))
	
@bot.event
async def on_message(message):
	
	msg = message.content			# Text content of the message
	emb = message.embeds			# Embed content of the message
	
	
	if message.content.startswith("!"):
		if message.channel != bot.get_channel(botchannel):
			await bot.delete_message(message)
			await bot.send_message(bot.get_channel(botchannel),"%s requested by %s!"%(msg, message.author.name))
			
	if message.channel != bot.get_channel(botchannel):
		if message.author.id == (botid):
			#print("Rythm posted something")
			await bot.delete_message(message)
			if message.content != "":
				await bot.send_message(bot.get_channel(botchannel),msg)
			else:
				replyemb = discord.Embed(title = "Rythm", description=message.embeds[0]['description'], color=0x00ff00)
				await bot.send_message(bot.get_channel(botchannel),embed=replyemb)
				#print(emb)

		

bot.run(bottoken)
