# RPi-TELEBOT

Python based Telegram bot to monitor and control the raspberry pi.

## Setting up the bot
- Install telepot library for enabling the Raspberry Pi to communicate with the Telegram bot using the API.
  ```
  sudo apt-get install python-pip
  sudo pip install telepot
  ```
- Request the BotFather to create a new Bot.
- Paste the HTTP access token here:
  ```
  bot = telepot.Bot('  Enter your Telegram bot API token here  ')
  ```
 - Run *gpiotel20.py* as sudo 
 - Try out the commands given below in the Telegram bot chat (see Usage section below)
 - GPIO of led1 and led2 set as 5 and 10 respectively(BCM numbering).
## Commands:


- help - List of commands
- ledon1 - Switch on LED 1
- ledoff1 - Switch off LED 1
- ledon2 - Switch on LED 2
- ledoff2 - Switch off LED 2
- cpu - Get CPU info (lscpu)
- usb - See connected USB devices (lsusb)
- hi - To check if online
- time - Returns time
- date - Returns date
- temp - CPU Temperature
- repoupdate - update repositories (sudo apt-get update)
- upgrade - upgrade packages (sudo apt-get upgrade -y)
- shutdown - Shutdown RPi (sudo shutdown -h now)
- reboot - Reboot RPi (sudo reboot)

## Usage:
- Use ' / ' before each command
- Example: To check the CPU Temperature;
 ```
 /temp
 ```
 
 <br />
## Tips:
 - See more about telegram bots here: https://core.telegram.org/bots
 -As the /repoupdate and /upgrade takes time you can use /ledon1 or /ledon2 command to alert you when the process is complete.
