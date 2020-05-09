import telebot
from time import sleep


bot = telebot.TeleBot('1173699882:AAGpJD6jHDo7Wtb_Q7waQh3G8rNftkbRVko')

@bot.message_handler(commands=['start'])
def start(message):
    while True:
        bot.send_message(message.chat.id, 'hello')
        sleep(1)
    
@bot.message_handler(commands=['hi'])
def hi(message):
    bot.send_message(message.chat.id, 'hi')




bot.polling()