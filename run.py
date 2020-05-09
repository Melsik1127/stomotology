# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import telebot
from telebot import types
from selenium.webdriver.common.by import By
from time import sleep
x = ''
d = ''
name = ''

TOKEN = '1173699882:AAGpJD6jHDo7Wtb_Q7waQh3G8rNftkbRVko'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Запишитесь к стоматологу')
    bot.send_message(message.chat.id, 'Какого числа вы хотите пойти?')
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



@bot.message_handler(commands=['write'])
def parser(message):
    global d,x,name
    bot.send_message(message.chat.id,'Ожидайте, обычно это занимает около минуты')
    l_keys = 'stomatologyReservation@gmail.com'
    p_keys = '10293873745'

    driver = webdriver.Chrome('chromedriver')
    driver.get('https://calendar.google.com/calendar/r?pli=1')

    login = driver.find_element_by_class_name('whsOnd')
    login.send_keys(l_keys)
    cursor = driver.find_element_by_class_name('CwaK9')
    cursor.click()
    sleep(6)
    password = driver.find_element_by_class_name('whsOnd')
    password.send_keys(p_keys)
    cursor = driver.find_element_by_class_name('CwaK9')
    cursor.click()

    sleep(8)

    date = driver.find_elements_by_class_name('r4nke ')
    for i in range(0, len(date)):
        if d in date[i].text:
            date[i].click()

    sleep(4)
    a = ActionChains(driver).move_by_offset(500, 100).click().perform()
    sleep(1)

    timer = driver.find_elements_by_class_name('WpDZC')

    for i in range(0, len(timer)):
        if i == 1:
            timer[i].click()
            break 
    tm = driver.find_elements_by_class_name('VKy0Ic')

    for i in range(0,len(tm)):
        if str(x) + ':00' in tm[i].text:
            tm[i].click()
            break
        else:
            if str(x) in tm[i].text:
                tm[i].click()
                break
    sleep(2)
    title = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
    title.click()
    title.send_keys(name)
    sleep(2)
    butt = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[3]/span')
    butt.click()
    bot.send_message(message.chat.id, 'Вы успешно забронированы!')
    global array, sous
    del(array)
    del(sous)
    array = []
    sous = []
    sleep(5)
    driver.get('https://calendar.google.com/calendar/r?pli=1')


    sleep(8)
    date = driver.find_elements_by_class_name('r4nke')
    for i in range(0,5):
        if i < 2:
            date[i].click()
    cur = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[3]/span/span')

    for i in range(0,35):

        cur.click()
        sleep(2)
        data = driver.find_element_by_class_name('folmac')
        states = driver.find_elements_by_class_name('gVNoLb')
        for a in range(0, len(states)):
            if 'Сегодня' in data.text:
                g = 9
            else:
                if 'PM' or 'AM' in states[a].text:
                    print(str(int(data.text)) + ' '  +str(states[a].text))
                    array.append(data.text)
                    sous.append(states[a].text)
        print(array)
        print(sous)
    driver.quit()

@bot.message_handler(content_types=['text'])
def text(message):
    global d,sous,array
     
    print(d)
    if d in array:
        m = [i for i,val in enumerate(array) if val==d]
        print(m)
        for i in range(0, len(m)):
            bot.send_message(message.chat.id, d + ' числа занято: ' + sous[m[i]])
    bot.send_message(message.chat.id ,'Теперь время в формате 24. Например: 14')
    bot.register_next_step_handler(message, text2)
def text2(message):
    global x
    if message.text == '13':
        x = '1:00PM'
    elif message.text == '12':
        x = '12:00PM'
    elif message.text == '14':
        x = '2:00PM'
    elif message.text == '15':
        x = '3:00PM'
    elif message.text == '16':
        x = '4:00PM'
    elif message.text == '17':
        x = '5:00PM'
    elif message.text == '18':
        x = '6:00PM'
    elif message.text == '19':
        x = '7:00PM'
    elif message.text == '20':
        x = '8:00PM'
    elif message.text == '21':
        x = '9:00PM'
    elif message.text == '22':
        x = '22:00PM'
    elif message.text == '23':
        x = '23:00PM'
    elif message.text == '0':
        x = '12:00AM'
    
    else:
        x = message.text
    print(x)
    bot.send_message(message.chat.id, 'Имя, Фамилия и Телефон через /, например: Иван/Иванов/+345345')
    bot.register_next_step_handler(message, text3)
def text3(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Проверьте, правильно ли вы все вписали, если все верно, то напишите /write')
    

l_keys = 'stomatologyReservation@gmail.com'
p_keys = '10293873745'
array = []
sous = []


driver = webdriver.Chrome('chromedriver')
driver.get('https://calendar.google.com/calendar/r?pli=1')

login = driver.find_element_by_class_name('whsOnd')
login.send_keys(l_keys)
cursor = driver.find_element_by_class_name('CwaK9')
cursor.click()
sleep(6)
password = driver.find_element_by_class_name('whsOnd')
password.send_keys(p_keys)
cursor = driver.find_element_by_class_name('CwaK9')
cursor.click()

sleep(8)
date = driver.find_elements_by_class_name('r4nke')
for i in range(0,5):
    if i < 2:
        date[i].click()
cur = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[3]/span/span')

for i in range(0,35):

    cur.click()
    sleep(2)
    data = driver.find_element_by_class_name('folmac')
    states = driver.find_elements_by_class_name('gVNoLb')
    for a in range(0, len(states)):
        if 'Сегодня' in data.text:
            g = 9
        else:
            if 'PM' or 'AM' in states[a].text:
                array.append(data.text)
                sous.append(states[a].text)

driver.quit()



    
bot.polling()