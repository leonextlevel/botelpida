import os
import discord
import asyncio

TOKEN = os.environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print('Bot Elpida Started')
	print('ID: %s - Name:%s' % (client.user.id, client.user.name))


@client.event
async def on_message(message):
	if message.content.lower().startswith('/help'):
		await message.channel.send('Eu estou sendo desenvolvido, logo terei novas funções!')


client.run(TOKEN)
