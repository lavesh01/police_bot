import discord
from discord.ext import commands

# My bot token
TOKEN = 'MTExNTcxMTkyNDM0OTQ0MDA5MQ.GihraM.5JRfgtmsWNR7zyijstyuqmlCYQ3iZscXbaeGks'

# Different name variations
YOUR_NAME_VARIATIONS = ['Harkirat', 'Harkirat Sir', 'Harkirat Bhaiya']

# Dicord bot intents are described below
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

# Created a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check whether a message contains the name variations
    if any(name in message.content for name in YOUR_NAME_VARIATIONS):
        # Send a scolding DM to the user
        await message.author.send("How dare you mention my name in vain!")

    await bot.process_commands(message)

# Run / Start the bot
bot.run(TOKEN)
