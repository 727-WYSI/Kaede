import discord
from discord.ext import commands
import random
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
PREFIX = '.k
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))  # Securely load your channel ID from an environment variable
WELCOME_FOLDER = 'welcome_memes'
GOODBYE_FOLDER = 'goodbye_memes'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Function to get list of filenames from the folder
def get_files(folder):
    files = os.listdir(folder)
    return [os.path.join(folder, file) for file in files]

@bot.event
async def on_ready():
    print(f'Got into {bot.user}. He is mine now!')

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

@bot.command(name='memes', help='Pull out a random meme from the folder')
async def memes(ctx):
    meme_files = get_files(WELCOME_FOLDER)
    if meme_files:
        meme_path = random.choice(meme_files)
        await ctx.send(file=discord.File(meme_path))
    else:
        await ctx.send('No memes found!')

@bot.command(name='chat', help='Start a conversation with the bot')
async def chat(ctx):
    questions = [
        "What's your favorite hobby?",
        "What's the last book you read?",
        "Do you have any pets?",
        "What's your favorite movie?"
    ]

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for question in questions:
        await ctx.send(question)
        try:
            response = await bot.wait_for('message', check=check, timeout=60.0)
            await ctx.send(f'You answered: {response.content}')
        except asyncio.TimeoutError:
            await ctx.send('You took too long to answer!')
            break

@bot.command(name='ping', help='Ping a website and show basic info')
async def ping(ctx, website: str):
    try:
        output = subprocess.check_output(["ping", "-c", "1", website], universal_newlines=True)
        lines = output.split('\n')
        for line in lines:
            if "bytes from" in line:
                await ctx.send(line)
                break
    except subprocess.CalledProcessError:
        await ctx.send("Failed to ping the website.")

@bot.command(name='owo', help='Responds with owo')
async def owo(ctx):
    await ctx.send('owo')

# Run the bot
bot.run(TOKEN)
