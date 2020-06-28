# Coder  :- Naveen A. B.
# Reddit :- u/RNA3210d

# Telegram bot to monitor and control your RPi
# The teleport library enables the Raspberry Pi to communicate with the Telegram bot using the API.
# Use "sudo pip install telepot" to install telepot library
import datetime 
import telepot  
import subprocess
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO   
from time import sleep      
from gpiozero import CPUTemperature
led1 = 5  #Set the GPIO pin number of LED 1
led2 = 10 #Set the GPIO pin number of LED 2       

GPIO.setmode(GPIO.BCM)     # Use Board pin numbering
GPIO.setup(led1, GPIO.OUT) # Declaring the output pin
GPIO.setup(led2, GPIO.OUT) # Declaring the output pin

now = datetime.datetime.now() 

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message
    print ('Incoming...')
    print(command)
    cpu = CPUTemperature()
    temp = cpu.temperature
    # Comparing the incoming message to send a reply according to it
    if command == '/help':
        bot.sendMessage (chat_id, str("ledon1 - Switch on LED 1\nledoff1 - Switch off LED 1\nledon2 - Switch on LED 2\nledoff2 - Switch off LED 2\ncpu - Get CPU info\nusb - See connected USB devices\nhi - To check if online\ntime - Returns time\ndate - Returns date\ntemp - CPU Temperature\nrepoupdate - update repositories \nupgrade - upgrade packages\nshutdown - Shutdown RPi\nreboot - Reboot RPi"))
    elif command == '/hi':
        bot.sendMessage (chat_id, str("Hi. BLEEP..BLOP.., bot is online"))
    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/ledon1':
        bot.sendMessage(chat_id, str("LED 1 ON"))
        GPIO.output(led1, True)
    elif command == '/ledoff1':
        bot.sendMessage(chat_id, str("LED 1 is OFF"))
        GPIO.output(led1, False)
    elif command == '/ledon2':
        bot.sendMessage(chat_id, str("LED 2 ON"))
        GPIO.output(led2, True)
    elif command == '/ledoff2':
        bot.sendMessage(chat_id, str("LED 2 is OFF"))
        GPIO.output(led2, False)
    elif command == '/temp':
        bot.sendMessage(chat_id, str("CPU temp. : ") + str(temp))
    elif command == '/repoupdate':
        bot.sendMessage(chat_id, str("Updating repos..."))
        p = subprocess.Popen("apt-get update", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        bot.sendMessage(chat_id, str(p))
        bot.sendMessage(chat_id, str("Update complete"))
    elif command == '/upgrade':
        bot.sendMessage(chat_id, str("Upgrading all packages..."))
        p = subprocess.Popen("apt-get upgrade -y", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        bot.sendMessage(chat_id, str(p))
        bot.sendMessage(chat_id, str("Upgrade complete"))
    elif command == '/shutdown':
        bot.sendMessage(chat_id, str("Shutdown command sent.."))
        subprocess.call('sudo shutdown -h now', shell=True)
    elif command == '/reboot':
        bot.sendMessage(chat_id, str("Reboot command sent.."))
        subprocess.call('sudo reboot', shell=True)
    elif command == '/cpu':
        p = subprocess.Popen("lscpu", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        bot.sendMessage(chat_id, str(p))
    elif command == '/usb':
        p = subprocess.Popen("lsusb", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        bot.sendMessage(chat_id, str(p))
# Enter your telegram token below
bot = telepot.Bot('Enter your Telegram bot API token here')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('GPIOTEL 2.00 at your service...')

while 1:
    sleep(10)
