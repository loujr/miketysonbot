# Mike Tyson as a Service


import os
import discord  # discord.py
from discord.ext import commands
from dotenv import load_dotenv #python-dotenv
import re  # regex
import requests


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
    # .stonk <ticker> returns stonk chart

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
    
    w_forcast = result_condition["text"]
    pretty_w_forcast = w_forcast.lower()

    current_tempf = result_current["temp_f"]
    pretty_tempf = "{:.0f} °F".format(current_tempf)  
    # rounds to nearest whole number
    current_tempc = result_current["temp_c"]
    pretty_tempc = "{:.0f} °C".format(current_tempc)  
    # rounds to nearest whole number

    forcast = (f"> The current temperature in {pretty_location} is " 
        f"{pretty_tempf} / {pretty_tempc}. The current forcast "
        f"is _{pretty_w_forcast}_, {result_current['humidity'] }% humidity.")

    await ctx.send(forcast)

    # .weather <location> returns current weather

@bot.command(pass_context=True)
async def http(ctx, arg):
    number = arg
    url = (f"http://http.cat/{number}.jpg")

    if (number == "100" or number == "101" or number == "102" or number == "103" or
        number == "200" or number == "201" or number == "202" or number == "203" or
        number == "204" or number == "206" or number == "207" or number == "300" or
        number == "301" or number == "302" or number == "303" or number == "304" or
        number == "305" or number == "307" or number == "308" or number == "400" or
        number == "401" or number == "402" or number == "403" or number == "404" or
        number == "405" or number == "406" or number == "407" or number == "408" or
        number == "409" or number == "410" or number == "411" or number == "412" or
        number == "413" or number == "414" or number == "415" or number == "416" or
        number == "417" or number == "418" or number == "420" or number == "421" or
        number == "422" or number == "423" or number == "424" or number == "425" or
        number == "426" or number == "428" or number == "429" or number == "431" or
        number == "444" or number == "450" or number == "451" or number == "497" or
        number == "498" or number == "499" or number == "500" or number == "501" or
        number == "502" or number == "503" or number == "504" or number == "505" or
        number == "506" or number == "507" or number == "508" or number == "509" or
        number == "510" or number == "511" or number == "521" or number == "522" or
        number == "523" or number == "525" or number == "530" or number == "598"):
        # checks if number is valid http status code
        await ctx.send(url)
    else:
        await ctx.send("Invalid HTTP status code")
    # .http <status code> returns http.cat image
    
    await ctx.send("(╯°□°)╯︵ ┻━┻")
    # .tableflip

@bot.command()
async def fingerguns(ctx):
    await ctx.send("(☞ﾟヮﾟ)☞")
    # .fingerguns

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    # .pong


bot.run(TOKEN)
