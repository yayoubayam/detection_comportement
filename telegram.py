# import requests
# import os
# import telebot
# TOKEN = "https://t.me/BotFather"
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#
# # bot = telebot.TeleBot('TOKEN')
# #
# # @bot.message_handler(commands=['start'])
# # def send_welcome(message):
# #     bot.reply_to(message, "Howdy, how are you doing?")
# print(requests.get(url).json())


import telebot
TOKEN = '5714085699:AAHpUteqmdOjpEq7OU2M9EO4AMGjNWyuUIM'

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

    bot.polling()