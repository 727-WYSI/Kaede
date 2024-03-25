import discord
from discord.ext import commands
import random

TOKEN = 'INSERT_YOUR_BOT_TOKEN'
PREFIX = '!' #replaced if needed
CHANNEL_ID = INSERT_YOUR_CHANNEL_ID

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

#Memes list

#For new members
welcome_memes = [
    'meme1.lịnk',
    'meme2.link',
]


#For members who left
goodbye_memes = [
    'meme1.link',
    'meme2.link',
]

@bot.event
async def on_ready():
    print(f'Login successfully as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(CHANNEL_ID)

    if channel is not None:
        welcome_message = (
            f'Hello {member.mention}! '
            f'Welcome to {member.guild.name}! '
            f'We hope you have an adventurous time here.\n'
            f'Here\'s a random meme for you:\n{random.choice(welcome_memes)}'
        )
#Funny music link section
        funny_music_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Rick Astley - Never Gonna Give You Up
        funny_music_message = (
            f'But first, let\'s get into the mood with a funny music: {funny_music_link}'
        )

        # Send the messages to the channel
        await channel.send(welcome_message)
        await channel.send(funny_music_message)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(CHANNEL_ID)

    if channel is not None:
        goodbye_message = (
            f'Goodbye, {member.display_name}! We will miss you. '
            f'Here\'s a sad meme to remember our time together:\n{random.choice(goodbye_memes)}'
        )

        sad_music_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Rick Astley - Never Gonna Give You Up
        sad_music_message = (
            f'And to make it even more sentimental, here\'s a sad music: {sad_music_link}'
        )

        # Send the messages to the channel
        await channel.send(goodbye_message)
        await channel.send(sad_music_message)

@bot.command(name='owo', help='Responds with owo')
async def owo(ctx):
    await ctx.send('owo')

# Run the bot
bot.run(TOKEN)
