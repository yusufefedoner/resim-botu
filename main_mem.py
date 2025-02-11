import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('C:/Users/MEHTAP DÖNER/OneDrive/Masaüstü/kodland/m2l1/images/'))
    with open(f'C:/Users/MEHTAP DÖNER/OneDrive/Masaüstü/kodland/m2l1/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        
 
    await ctx.send(file=picture)
bot.run("MTMzMTMxNjUzMjA2Mzc2ODYzNg.Gj9Xka.tcMVSlUVsva_3bqY70DII9c2YMU-ZRxtpSIJ00")
