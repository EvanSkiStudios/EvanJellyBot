import os
import discord

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
BOT_CLIENTID = os.getenv("CLIENTID")
BOT_SERVERID = os.getenv("SERVERID")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('This is a test of a message'):
        await message.channel.send('Test completed!')

client.run(BOT_TOKEN)