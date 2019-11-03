import os
import discord
import asyncio
# import psycopg2

from funcoes.rolagem import criar_roll

# Variaveis com os valores das varieveis de ambiente informados
# Utilizado para manter as informações em um lugar mais seguro
TOKEN = os.environ.get('TOKEN')
HOST = os.environ.get('HOST')
DATABASE = os.environ.get('DATABASE')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

client = discord.Client()


# Mensagem quando o bot é iniciado
@client.event
async def on_ready():
    print('Bot Elpida Started')
    print('ID: %s - Name:%s' % (client.user.id, client.user.name))


# Monitora as mesagens e vê se alguma se encaixa em alguma condição
@client.event
async def on_message(message):
    if message.content.lower().startswith('/help'):
        await message.channel.send('Eu estou sendo desenvolvido, logo terei novas funções!')
    if message.content.lower().startswith('/roll'):
        try:
            await message.channel.send(criar_roll(message))
        except ValueError:
            await message.channel.send(
                ":robot: **BOT**\n\n"
                ":speech_balloon: Fui projetado para não ser burro igual você!"
            )


# Starta o bot com o Token informado
client.run(TOKEN)

# conn = psycopg2.connect(
#     host=HOST,
#     database=DATABASE,
#     user=USER,
#     password=PASSWORD
# )
