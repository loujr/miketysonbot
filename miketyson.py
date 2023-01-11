# Mike Tyson as a Service
import os

import discord  # discord.py
from discord.ext import commands
from dotenv import load_dotenv #python-dotenv
import re  # regex
import requests
import json


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
RAPIDAPI_TOKEN = os.getenv("RAPIDAPI_TOKEN")
# tokens and api keys are stored in .env file

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
    # prevents bot from responding to itself

    FC = re.compile("fight\s*club", re.IGNORECASE)
    if FC.search(message.content):
        await message.reply("Hey man don't talk about fightclub")
    # responds w/ first rule of fightclub if found in message

    LOU = re.compile(r"\blou\b", re.IGNORECASE)
    if LOU.search(message.content):
        await message.reply("That's my boy right there")
    # responds w/ thats my boy right there if lou is found in message


@bot.command(pass_context=True)
async def stonk(ctx, arg):
    symbol = arg
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
    querystring = {"region": "US", "symbols": symbol}
    headers = {
        "x-rapidapi-key": RAPIDAPI_TOKEN,
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    result = data["quoteResponse"]["result"][0]
    name = result["longName"]
    ticker = result["symbol"]
    market_open = result["regularMarketOpen"]
    current_market_price = result["regularMarketPrice"]
    percent_change = result["regularMarketChangePercent"]
    pretty_percent_change = "{:.2f}%".format(percent_change)
    # market_high = result["regularMarketDayHigh"]
    # market_low = result["regularMarketDayLow"]
    # market_cap = result["marketCap"]
    # volume = result["regularMarketVolume"]

    embed = discord.Embed(title=name, color=0x15DBC7)
    embed.add_field(name="Ticker:", value=ticker, inline=False)
    embed.add_field(name="Open:", value=market_open, inline=False)
    embed.add_field(name="Current:", value=current_market_price, inline=False)
    embed.add_field(name="Change:", value=pretty_percent_change, inline=False)
    await ctx.send(embed=embed)
    # .stonk <ticker>   returns stonk chart


@bot.command()
async def tableflip(ctx):
    await ctx.send("(╯°□°)╯︵ ┻━┻")
    # .tableflip


@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    # .pong


bot.run(TOKEN)
