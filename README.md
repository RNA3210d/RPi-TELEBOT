# RPi-TELEBOT

Python based Telegram bot to monitor and control the raspberry pi.

## Setting up the bot
- Install telepot library for enabling the Raspberry Pi to communicate with the Telegram bot using the API.
  ```
  sudo apt-get install python-pip
  sudo pip install telepot
  ```
- Request the BotFather to create a new Bot.
- Paste the HTTP access token here :
  ```
  bot = telepot.Bot('  Enter your Telegram bot API token here  ')
  ```
## Commands:


- help - List of commands
- ledon1 - Switch on LED 1
- ledoff1 - Switch off LED 1
- ledon2 - Switch on LED 2
- ledoff2 - Switch off LED 2
- cpu - Get CPU info
- usb - See connected USB devices
- hi - To check if online
- time - Returns time
- date - Returns date
- temp - CPU Temperature
- repoupdate - update repositories 
- upgrade - upgrade packages
- shutdown - Shutdown RPi
- reboot - Reboot RPi

## Usage :
 Type the command followed by a / .
 For example : To check the CPU Temperature;
 ```
 /temp
 ```
# Readme is still under construction.
