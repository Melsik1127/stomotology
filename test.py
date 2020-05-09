# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import telebot
from telebot import types
from selenium.webdriver.common.by import By
from time import sleep


bot = telebot.TeleBot('1173699882:AAGpJD6jHDo7Wtb_Q7waQh3G8rNftkbRVko')



@bot.message_handler(commands=['help', 'start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=7)
    item1 = types.InlineKeyboardButton("1", callback_data='1')
    item2 = types.InlineKeyboardButton("2", callback_data='2')
    item3 = types.InlineKeyboardButton("3", callback_data='3')
    item4 = types.InlineKeyboardButton("4", callback_data='4')
    item5 = types.InlineKeyboardButton("5", callback_data='5')
    item6 = types.InlineKeyboardButton("6", callback_data='6')
    item7 = types.InlineKeyboardButton("7", callback_data='7')
    item8 = types.InlineKeyboardButton("8", callback_data='8')
    item9 = types.InlineKeyboardButton("9", callback_data='9')
    item10 = types.InlineKeyboardButton("10", callback_data='10')
    item11 = types.InlineKeyboardButton("11", callback_data='11')
    item12 = types.InlineKeyboardButton("12", callback_data='12')
    item13 = types.InlineKeyboardButton("13", callback_data='13')
    item14 = types.InlineKeyboardButton("14", callback_data='14')
    item15 = types.InlineKeyboardButton("15", callback_data='15')
    item16 = types.InlineKeyboardButton("16", callback_data='16')
    item17 = types.InlineKeyboardButton("17", callback_data='17')
    item18 = types.InlineKeyboardButton("18", callback_data='18')
    item19 = types.InlineKeyboardButton("19", callback_data='19')
    item20 = types.InlineKeyboardButton("20", callback_data='20')
    item21 = types.InlineKeyboardButton("21", callback_data='21')
    item22 = types.InlineKeyboardButton("22", callback_data='22')
    item23 = types.InlineKeyboardButton("23", callback_data='23')
    item24 = types.InlineKeyboardButton("24", callback_data='24')
    item25 = types.InlineKeyboardButton("25", callback_data='25')
    item26 = types.InlineKeyboardButton("26", callback_data='26')
    item27 = types.InlineKeyboardButton("27", callback_data='27')
    item28 = types.InlineKeyboardButton("28", callback_data='28')
    item29 = types.InlineKeyboardButton("29", callback_data='29')
    item30 = types.InlineKeyboardButton("30", callback_data='30')
    item31 = types.InlineKeyboardButton("31", callback_data='31')
    markup.add(item1, item2,item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27, item28, item29, item30, item31)
    bot.send_message(message.chat.id, 'Выберите дату:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 1
            elif call.data == '2':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 2
            elif call.data == '3':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 3
            elif call.data == '4':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 4
            elif call.data == '5':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 5
            elif call.data == '6':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 6
                print(d)
            elif call.data == '7':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 7
            elif call.data == '8':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 8
            elif call.data == '9':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 9
            elif call.data == '10':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 10
            elif call.data == '11':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 11
            elif call.data == '12':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 12
            elif call.data == '13':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 13
            elif call.data == '14':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 14
            elif call.data == '15':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 15
            elif call.data == '16':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 16
            elif call.data == '17':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 17
            elif call.data == '18':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 18
            elif call.data == '19':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 19
            elif call.data == '20':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 20
            elif call.data == '21':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 21
            elif call.data == '22':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 22
            elif call.data == '23':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 23
            elif call.data == '24':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 24
            elif call.data == '25':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 25
            elif call.data == '26':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 26
            elif call.data == '27':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 27
            elif call.data == '28':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 28
            elif call.data == '29':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 29
            elif call.data == '30':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 30
            elif call.data == '31':
                bot.send_message(call.message.chat.id ,'Теперь время в формате 24. Например: 14')
                d = 31
    
    except Exception as e:
        print(repr(e))
 
    
 

bot.polling()
    

