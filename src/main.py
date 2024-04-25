import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
from time.time_functions import get_time  # Import the get_time function

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
PREFIX = '?'  # Prefix for your bot commands, change as needed
CHANNEL_ID = YOUR_CHANNEL_ID
WELCOME_FOLDER = 'welcome_memes'
GOODBYE_FOLDER = 'goodbye_memes'
TIME_FOLDER = 'time'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Function to get list of filenames from the folder
def get_files(folder):
    files = os.listdir(folder)
    return [os.path.join(folder, file) for file in files]

@bot.event
async def on_ready():
    print(f'Got into {bot.user}'. He is mine now!)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(CHANNEL_ID)

    if channel is not None:
        welcome_memes = get_files(WELCOME_FOLDER)
        if welcome_memes:
            meme_path = random.choice(welcome_memes)
            welcome_message = (
                f'Hello {member.mention}! '
                f'Welcome to {member.guild.name}! '
                f'We hope you have an adventurous time here.\n'
            )
            # Send the welcome message with a random welcome meme
            await channel.send(welcome_message, file=discord.File(meme_path))

            # Get and send the current time for a city
            time_city = 'America/New_York'  # Change to the desired city or timezone
            current_time = get_time(time_city)
            time_message = f'Current Time in {time_city}: {current_time}'
            await channel.send(time_message)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(CHANNEL_ID)

    if channel is not None:
        goodbye_memes = get_files(GOODBYE_FOLDER)
        if goodbye_memes:
            meme_path = random.choice(goodbye_memes)
            goodbye_message = (
                f'Goodbye, {member.display_name}! We will miss you. '
                f'Here\'s a meme to remember our time together:\n'
            )
            await channel.send(goodbye_message, file=discord.File(meme_path))

            # Get and send the current time for a city
            time_city = 'America/New_York'  # Change to the desired city or timezone
            current_time = get_time(time_city)
            time_message = f'Current Time in {time_city}: {current_time}'
            await channel.send(time_message)

@bot.command(name='owo', help='Responds with owo')
async def owo(ctx):
    await ctx.send('owo')

# Run the bot
bot.run(TOKEN)
