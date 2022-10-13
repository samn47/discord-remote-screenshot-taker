# Discord Remote Screenshot Taker
Instantly takes an image of your screen and sends it to your private discord bot. All remotely and super fast!
## Disclaimer

This program was made for educational purposes.  
The way you use it is your responsibility.  
I am not responsible for any malicious use of this program.

## Requirements

- A computer
- [Python 3.10](https://www.python.org) with pip
- A discord bot
- A discord server with the bot

Open CMD and type these commands:

```bash
pip install discord
```
```bash
pip install pyautogui
```

## Setup
When you open the file with an IDE or text editor, you will see this:

![imagem_2022-10-13_014815584](https://user-images.githubusercontent.com/114893759/195504107-69aa2922-cb2a-49f6-bb8e-5dabd94bf9af.png)

Here is how to configure the variables:

### token
>Change the value to your Discord bot's token.
### directoryname
>The name of the directory that the screenshots will be temporarily saved. The directory  
will be created in roaming, inside appdata. You can use an existing folder.
### prefix
>The command's prefix. Change it to any symbol ("." "," "!" "?" etc)
### command
>The command's name. You will use it to screenshot the screen.


## Features
- Remote screenshotting.
- Deletes the file after sending it to your server.
- Logs the file path and date the screenshot was taken.

## Troubleshooting

- Python window closing quickly when the file is ran.
>make sure you installed the modules correctly. repeat the process in [requirements](#Requirements).

- "Pip is not recognized as a internal or external command" error in CMD while installing modules.
>did you install pip? by default pip is also installed with python.

- "Improper token has been passed." when running the program.
>make sure the "token" variable is set to your discord bot's token. you probably didn't see the [setup](#Setup) step, huh?

If you have any other problem, use the issues box.
## Notes

- It does not have a native builder for .EXE files.
