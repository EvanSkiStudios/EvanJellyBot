import os
import discord

from dotenv import load_dotenv
from Utility import Responses

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
    # print(message.content)

    message_lower = message.content.lower()

    if message.author == client.user:
        return

    if message.mention_everyone:
        return

    # replying to EvanJelly directly
    if message.reference:
        referenced_message = await message.channel.fetch_message(message.reference.message_id)
        if referenced_message.author == client.user:
            # We have confirmed the replayed to message is from EvanJelly
            await message.channel.send('You called')
            return

    # Pinging @Evanjelly
    if message_lower.find("@" + str(BOT_CLIENTID)) != -1:
        await message.channel.send('Ping Pong!')
        return

    if message_lower in Responses.Greetings:
        await message.channel.send('Heyo')
        return

    if message_lower.find('evanjelly') != -1:
        if message.content.lower().find('language') != -1:
            await message.channel.send('Im powered by snakes! :snake:')
            return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        return

    if message_lower.find('beans') != -1:
        await message.channel.send('Beans are neat!')
        return

    if (str(message.author) == "evanski_") and (message.content.lower().find('evanjelly') != -1):
        await message.channel.send('EvanJelly is ME!')
        return


# Login
client.run(BOT_TOKEN)
