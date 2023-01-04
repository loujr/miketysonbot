# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot has connected to Discord!")

    # displays when successful connection to discord


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    if "fightclub" in message.content:
        await message.reply("Hey man don't talk about fightclub")


    # responds w/ first rule of fightclub if found in message


@bot.command()
async def tableflip(ctx):
    await ctx.send("(╯°□°)╯︵ ┻━┻")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


bot.run(TOKEN)
