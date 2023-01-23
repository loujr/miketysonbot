# Mike Tyson as a Service
import os

import discord  # discord.py
from discord.ext import commands
from dotenv import load_dotenv #python-dotenv

#from PIL import Image # pillow
#import urllib.request # urllib
#import tempfile # tempfile
import io
import aiohttp 

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

@bot.command(pass_context=True)
async def weather(ctx, arg):
    place = arg
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": place.format(str)}
    headers = {
        "x-rapidapi-key": RAPIDAPI_TOKEN,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    result_location = data["location"]
    result_current = data["current"]
    pretty_location = result_location["name"]
    result_condition = data["current"]["condition"]
    

#    icon = result_condition["icon"]
#    format_icon = icon.replace("//", "https://")

#    async def get_image(url):
#        async with ClientSession() as session:
#            await async with session.get(url) as resp:
#                discord.File(resp, 'image.png')

#    async def get_image(url):
#        async with aiohttp.ClientSession() as session:
#            async with session.get(url) as resp:
#                if resp.status != 200:
#                    return await ctx.send('Could not download file...')
#                data = io.BytesIO(await resp.read())




#    discord.File(format_icon, filename="image.png")
#    file = discord.File("image.png")

#    img_data = requests.get(format_icon).content
#    with open('image.png', 'wb') as handler:
#        file = discord.File(img_data, filename="image.png")




#    async with aiohttp.ClientSession() as session:
#        async with session.get(format_icon) as resp:
#            if resp.status != 200:
#                return await ctx.send('Could not download file...')
#            data = io.BytesIO(await resp.read())
#            await ctx.send(file=discord.File(data, 'image.png'))


#    embeded = discord.Embed(title="Weather", color=0x15DBC7)
#    embeded = embeded.set_image(url=format_icon)



#    urllib.request.urlretrieve(format_icon, "image.png")
#    with Image.open("image.png") as img:
#        file = discord.File(format_icon, filename="image.png")
#        await ctx.send(file=file)


    current_tempf = result_current["temp_f"]  
    current_tempc = result_current["temp_c"]
    forcast = f"> The current temperature in {pretty_location} is {current_tempf} °F / {current_tempc} °C. The current forcast is {result_condition['text']}."
#   forcast = f"> The current temperature in {pretty_location} is {current_tempf} °F / {current_tempc} °C \n> The current forcast is {result_condition['text']} {get_image(format_icon)}"
    await ctx.send(forcast)
     #.weather <location>   returns current weather


@bot.command()
async def tableflip(ctx):
    await ctx.send("(╯°□°)╯︵ ┻━┻")
    # .tableflip


@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    # .pong


bot.run(TOKEN)