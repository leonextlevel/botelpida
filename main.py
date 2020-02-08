import os
import discord
# import psycopg2

from funcoes.rolagem import Roll
from funcoes.utils import comandos, ajuda

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
        await message.channel.send(ajuda(message.author.name))
    if message.content.lower().startswith('/roll'):
        try:
            num_dados = int(message.content.lower().split()[1])
            rolagem = Roll(num_dados)
            await message.channel.send(rolagem.get_resultados())
        except ValueError:
            await message.channel.send(
                "**ERROR** :robot:\n"
                "USUÁRIO SEM CAPACIDADE COGNITIVA DE UTILIZAR UM BOT!"
            )
    if message.content.lower().startswith('/comandos'):
        await message.channel.send(comandos())

# Starta o bot com o Token informado
client.run(TOKEN)

# conn = psycopg2.connect(
#     host=HOST,
#     database=DATABASE,
#     user=USER,
#     password=PASSWORD
# )
