import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "?"

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)






@bot.event
async def on_ready():
    activity = discord.Game(name="OwO", type=4)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(f'''{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     

{Fore.GREEN}

░█████╗░██╗░░░██╗████████╗░█████╗░██████╗░░█████╗░███╗░░██╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║██║░██╔╝██╔════╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██║███████║██╔██╗██║█████═╝░█████╗░░██████╔╝
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░██║██╔══██║██║╚████║██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝██║░░██║██║░╚███║██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

selfbot is ready!
''')


















@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="💰 Help AutoOwO 💰",
        color=104189,
        description=
        f"💵**{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owob 50 seconds.\n\n**💵{prefix}stopautoOwO**\nstops autoOwO.\n\n**💵{prefix}Owobanbypass**\nIts prevent you from banning Owo by taking appropriate time\n Example:-`the bot takes breaak 5 min of runnning 1st break= 5min,2nd break=10min 3rd break=15min` \n\n made by <@907169033764356097>"
    )
    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/924964210184695839/933558251327467540/FB_IMG_1640012142547.jpg"
    )
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO  is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.send('owo')
            print(f"{Fore.GREEN}succefully owo")
            await asyncio.sleep(15)
            await ctx.send('ff')
            print(f"{Fore.GREEN}succefully ff")
            await ctx.send('hahaha')
            print(f"{Fore.GREEN}succefully fish + chat")
            await asyncio.sleep(10)
            await ctx.send('owo')
            print(f"{Fore.GREEN}succefully owo")
            await asyncio.sleep(13)


@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO Magi is now **disabled**!')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def Owobanbypass(ctx):
    await ctx.message.delete()
    await ctx.send('owobanbypass is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(300) 

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(4)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(900)

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(4)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(900)

            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(15)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owob')
            print(f"{Fore.GREEN}succefully battle")
            await asyncio.sleep(1200)        
            
# @bot.command()
# async def stopautoOwO(ctx):
#     await ctx.message.delete()
#     await ctx.send('auto OwO Magi is now **disabled**!')
#     global dmcs
#     dmcs = False



















































keep_alive()
bot.run(token, bot=False)
