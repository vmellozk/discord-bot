#
import os
import discord
import asyncio
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv
import ffmpeg

#Carregando o dotenv e aplicando o token a variável
load_dotenv()
token = os.getenv('DISCORD_TOKEN_KEY')

#
intents = discord.Intents.default()
intents.message_content = True

#
client = discord.Client(intents=intents)

#
bot = commands.Bot(command_prefix='!', intents=intents)

#Printa o bot ao iniciar
@client.event
async def on_ready():
    print(f'Logged is as {client.user}!')

#Configuração dos comandos Padrões
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!hello'):
        await message.channel.send(f"Olá, {message.author.mention}!")

    if message.content.lower().startswith('!ping'):
        await message.channel.send(f"Pong!")

    if message.content.lower().startswith("!echo"):
        response = message.content[6:]
        await message.channel.send(response)

#Configuração do YoutubeDL
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


client.run(token)
