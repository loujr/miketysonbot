# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # displays when successful connection to discord

@client.command()
async def ping(ctx):
    await ctx.send('Pong')
    #responds pong: $ping

@client.command()
async def fightclub(ctx):
    await ctx.send('1st rule of FightClub is you do not talk about FightClub.')
    #responds w/ first rule of FC: $fightclub


client.run(TOKEN)
