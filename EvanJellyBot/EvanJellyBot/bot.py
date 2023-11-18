import os
import discord

from dotenv import load_dotenv

# Load Env
load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
BOT_CLIENTID = os.getenv("CLIENTID")
BOT_SERVERID = os.getenv("SERVERID")

# set discord intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # When the bot has logged in, call back
    print(f'We have logged in as {client.user}')


# very basic message detection
@client.event
async def on_message(message):

    # print(str(message))
    # print(message.author)
    # print(message.content.lower())
    # print(message.content.lower().find('Cat'))

    if message.author == client.user:
        return

    if message.content.lower().find('evanjelly') != -1:
        if message.content.lower().find('language') != -1:
            await message.channel.send('Im powered by snakes! :snake:')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.lower().find('beans') != -1:
        await message.channel.send('Beans are neat!')

    if (str(message.author) == "evanski_") and (message.content.lower().find('cat') != -1):
        await message.channel.send('EvanJelly is ME!')


# Login
client.run(BOT_TOKEN)
