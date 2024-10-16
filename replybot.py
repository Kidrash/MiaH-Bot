# https://my.telegram.org/apps
import os

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.Telebot(BOT_TOKEN)

@bot.message_handler(commands= ['start', 'hello']) 
def send_welcome(message):
    bot.reply_to(message, "Heyy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()  

# make a config.json file with the following parameters
# {
#     "api_id": #API-ID,
#     "api_hash": "#API-HASH"
#   }

# Also have a .env file with the following line;
# export BOT_TOKEN = (Bot token obtained from botfather)

# Note:!!
# the API-ID and API-HASH are obtained from the website above, commented out in line 1 

  