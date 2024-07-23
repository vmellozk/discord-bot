import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged is as {client.user}!')

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

token = os.getenv('DISCORD_TOKEN_KEY')
client.run(token)
