import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregando o dotenv e aplicando o token à variável
load_dotenv()
token = os.getenv('DISCORD_TOKEN_KEY')

# Configurando intents e bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Carregar cogs
@bot.event
async def on_ready():
    print(f'Logado como {bot.user}!')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Cog {filename[:-3]} carregada com sucesso.')
            except Exception as e:
                print(f'Falha ao carregar a cog {filename[:-3]}.', e)

# Comandos padrão
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower().startswith('!hello'):
        await message.channel.send(f"Olá, {message.author.mention}!")

    if message.content.lower().startswith('!ping'):
        await message.channel.send(f"Pong!")

    if message.content.lower().startswith("!echo"):
        response = message.content[6:]
        await message.channel.send(response)

    # Passar a mensagem para outros comandos processarem
    await bot.process_commands(message)

bot.run(token)
