# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import telebot
from telebot import types
from utils.telegramcalendar import create_calendar
from telebot import apihelper
import datetime



driver = webdriver.Chrome('chromedriver')

current_shown_dates={}
from selenium.webdriver.common.by import By
from time import sleep
x = ''
telephone = ''
tomp = ''
d = ''
l = ''
rot2 = ''
name = ''

proxies = { 'http': 'socks5://127.0.0.1:9099', 'https': 'socks5://127.0.0.1:9099' }
TOKEN = '1112582970:AAHEpQdfzGh-BE9emDmGOtYHmeH-Fy3LPD8'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['stall'],func=lambda message: True)
def botik(message):
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton("Подтвердить", callback_data='s')
    item_2 = types.InlineKeyboardButton("Изменить", callback_data='g')
    markup2.add(item, item_2)
                
    bot.send_message(message.chat.id, 'Все верно?', reply_markup=markup2)
@bot.message_handler(commands=['start'], func=lambda message: True)
def handle_calendar_command(message): 
    global d,rot2, m
    bot.send_message(message.chat.id, 'Добрый день!  Вас приветствует стоматология "Дента+"')
    sleep(0.3)
    bot.send_message(message.chat.id, 'Здесь вы можете записаться на прием в любое удобное для вас время!')
    sleep(0.3)
    
    markup3 = types.InlineKeyboardMarkup(row_width= 1)
    item1 = types.InlineKeyboardButton("Запломбировать зуб", callback_data='one')
    item2 = types.InlineKeyboardButton("Вырвать зуб", callback_data='two')
    item3 = types.InlineKeyboardButton("Отбеливание зубов", callback_data='three')
    markup3.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выберите услугу:', reply_markup=markup3)
    '''
    
    '''

@bot.callback_query_handler(func=lambda call: 'DAY' in call.data[0:13])
def handle_day_query(call):
    global d,rot2, m
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    last_sep = call.data.rfind(';') + 1
    m = call.data[4:8]
    rot2 = call.data[9:11]
    newstr = call.data.replace(";", " ") 
    m = newstr.split()[1]
    rot2 = newstr.split()[2]
    d = newstr.split()[3]
    if d == '22':
        if int(month) == 6:
            print(month)
            ignore(call)
    else:


        if saved_date is not None:
            driver.get('https://calendar.google.com/calendar/r/day/' + m+'/'+ rot2 +'/' + str(d) +"?pli=1%252Fday%252F2021%252F5%252F11")
            bot.send_message(call.message.chat.id, 'Ожидайте...')
            try:
                l_keys = 'stomatologyReservation@gmail.com'
                p_keys = '10293873745'

                day = call.data[last_sep:]
                
                
                sleep(1)
                login = driver.find_element_by_class_name('whsOnd')
                login.send_keys(l_keys)
                cursor = driver.find_element_by_class_name('CwaK9')
                cursor.click()
                sleep(6)
                password = driver.find_element_by_class_name('whsOnd')
                password.send_keys(p_keys)
                cursor = driver.find_element_by_class_name('CwaK9')
                cursor.click()
                no_time = []
                sleep(4)
                
                
            except:
                no_time = []
                sleep(4)
                all_if = driver.find_elements_by_class_name('gVNoLb')
                for i in range(0,len(all_if)):
                    no_time.append(all_if[i].text)
            markup3 = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("11:00", callback_data='11')
            item2 = types.InlineKeyboardButton("12:00", callback_data='12')
            item3 = types.InlineKeyboardButton("13:00", callback_data='13')
            item4 = types.InlineKeyboardButton("14:00", callback_data='14')
            item5 = types.InlineKeyboardButton("15:00", callback_data='15')
            item6 = types.InlineKeyboardButton("16:00", callback_data='16')
            item7 = types.InlineKeyboardButton("17:00", callback_data='17')
            print(no_time)
            
            if '11AM–12PM' not in no_time:
                markup3.add(item1)
            if '12–1PM' not in no_time:
                markup3.add(item2)
            if '1–2PM' not in no_time:
                markup3.add(item3)
            if '2–3PM' not in no_time:
                markup3.add(item4)
            if '3–4PM' not in no_time:
                markup3.add(item5)
            if '4–5PM' not in no_time:
                markup3.add(item6)
            if '5–6PM' not in no_time:
                markup3.add(item7)
                
            bot.send_message(chat_id=chat_id, text="Время",reply_markup=markup3)

        else:
            # add your reaction for shown an error
            pass


@bot.callback_query_handler(func=lambda call: 'MONTH' in call.data)
def handle_month_query(call):
    global d,rot2, m, month
    
    info = call.data.split(';')
    month_opt = info[0].split('-')[0]
    year, month = int(info[1]), int(info[2])
    chat_id = call.message.chat.id
    

    if month_opt == 'PREV':
        month -= 1

    elif month_opt == 'NEXT':
        month += 1

    if month < 1:
        month = 12
        year -= 1 

    if month > 12:
        month = 1
        year += 1

    date = (year, month)
    current_shown_dates[chat_id] = date
    markup = create_calendar(year, month)
    bot.edit_message_text("Выберите дату: ", call.from_user.id, call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: "IGNORE" in call.data)
def ignore(call):
    global d,rot2, m
    bot.answer_callback_query(call.id, text="Это не дата!")

@bot.message_handler(commands=['asfsa'])
def variant(message):
    bot.send_message(message.chat.id, 'Мы работаем 5/7 с 11.00 до 17.00 Сб. Вс. - Выходной')
    now = datetime.datetime.now()
    chat_id = message.chat.id

    date = (now.year, now.month)
    current_shown_dates[chat_id] = date
    
    markup = create_calendar(now.year, now.month)

    bot.send_message(message.chat.id, "Выберите подходящий для вас день: ", reply_markup=markup)


    
@bot.message_handler(commands=['write'], func=lambda message: True)
def parser(message):
    global d,x,name, rot2, m, telephone, tomp
    bot.send_message(message.chat.id,'Ожидайте, обычно это занимает около минуты')
    l_keys = 'stomatologyReservation@gmail.com'
    p_keys = '10293873745'

    driver.get('https://calendar.google.com/calendar/r/day/' + m+'/'+ rot2 +'/' + str(d) +"?pli=1%252Fday%252F2021%252F5%252F11")
    sleep(4)

    try:
        login = driver.find_element_by_class_name('whsOnd')
        login.send_keys(l_keys)
        cursor = driver.find_element_by_class_name('CwaK9')
        cursor.click()
        sleep(6)
        password = driver.find_element_by_class_name('whsOnd')
        password.send_keys(p_keys)
        cursor = driver.find_element_by_class_name('CwaK9')
        cursor.click()
        
        sleep(4)
        
        a = ActionChains(driver).move_by_offset(100, 100).click().perform()
        sleep(1)

        timer = driver.find_elements_by_class_name('WpDZC')

        for i in range(0, len(timer)):
            if i == 1:
                timer[i].click()
                break 
        tm = driver.find_elements_by_class_name('VKy0Ic')
        print(x)
        print(x + ':00')
        for i in range(0,len(tm)):
            if str(x) == tm[i].text:
                tm[i].click()
                break
        sleep(2)
        title = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
        title.click()
        title.send_keys(name + ' ' + telephone)
        sleep(2)
        desk = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[5]/div[1]/div/div[2]/div/div/span/span')
        desk.click()
        sleep(1)
        disc = driver.find_element_by_xpath('//*[@id="T2Ybvb0"]')
        disc.send_keys(tomp)
        sleep(2)
        butt = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[3]/span')
        butt.click()
        bot.send_message(message.chat.id, 'Вы успешно забронированы!')
    except:
        sleep(4)
        
        a = ActionChains(driver).move_by_offset(100, 100).click().perform()
        sleep(1)

        timer = driver.find_elements_by_class_name('WpDZC')

        for i in range(0, len(timer)):
            if i == 1:
                timer[i].click()
                break 
        tm = driver.find_elements_by_class_name('VKy0Ic')
        print(x)
        print(x + ':00')
        for i in range(0,len(tm)):
            if str(x) == tm[i].text:
                tm[i].click()
                break
        sleep(2)
        title = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
        title.click()
        title.send_keys(name + ' ' + telephone)
        sleep(2)
        desk = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[5]/div[1]/div/div[2]/div/div/span/span')
        desk.click()
        sleep(1)
        disc = driver.find_element_by_xpath('//*[@id="T2Ybvb0"]')
        disc.send_keys(tomp)
        sleep(2)
        butt = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[3]/span')
        butt.click()
        bot.send_message(message.chat.id, 'Вы успешно забронированы!')

                
@bot.message_handler(content_types=['text'])
def text(message):
    global name
    name = message.text
    
    bot.send_message(message.chat.id ,'Теперь номер телефона')
    
    bot.register_next_step_handler(message, text2)


def text2(message):
    global telephone
    telephone = message.text
    global x, name
    global d,sous,array,m, rot2, tomp, l
    print(tomp+ '.'+l)
    
    bot.send_message(message.chat.id, 'Все ли вы указали верно?\n'
    + 'Прием на ' + str(tomp) + '\n' + d + '.' + rot2 + '.' + m +
    '/' + l + '\n' + name + '\n' + telephone)
    
    botik(message)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global x, telephone, l, tomp
    try:
        if call.message:
            if call.data == '11':
 
                
                l = str(call.data) + ':00'
                print(l)               
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '11:00AM'
                sleep(2)
                
            elif call.data == '12':
                
                l = str(call.data) + ':00'
                print(l) 
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '12:00PM'
                sleep(2)
            elif call.data == '13':
                
                l = str(call.data) + ':00'
                
                print(l)
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '1:00PM'
                sleep(2)
            elif call.data == '14':
                
                l = str(call.data) + ':00'
                print(l)
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '2:00PM'
                sleep(2)
            elif call.data == '15':
                
                l = str(call.data) + ':00'
                print(l)
                
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '3:00PM'
                sleep(2)
            elif call.data == '16':
                
                l = str(call.data) + ':00'
                print(l)
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '4:00PM'
                sleep(2)
             
            elif call.data == '17':
                
                l = str(call.data) + ':00'
                print(l)  
                bot.send_message(call.message.chat.id, 'Введите Имя и Фамилию')   
                x = '5:00PM'
                sleep(2)
            elif call.data == 'g':
                handle_calendar_command(call.message)
            elif call.data == 's':
                parser(call.message)
            elif call.data == 'one':
                tomp = 'Запломбировать зуб'
                variant(call.message)
            elif call.data == 'two':
                tomp = 'Вырвать зуб'
                variant(call.message)
            elif call.data == 'three':
                tomp = 'Отбеливание зубов'
                variant(call.message)


    except Exception as e:

        print(repr(e))


    
    
    

    
    
'''
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

for i in range(0,5):

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

sleep(3)
driver.get('https://calendar.google.com/calendar/r/day/')
rot = driver.find_element_by_class_name('rSoRzd')
m = rot.text.split()[1]
if 'Май' in rot.text:
    g = '05'
if 'Январь' in rot.text:
    g = '01'
if 'Февраль' in rot.text:
    g = '02'
if 'Март' in rot.text:
    g = '03'
if 'Апрель' in rot.text:
    g = '04'
if 'Июнь' in rot.text:
    g = '06'
if 'Июль' in rot.text:
    g = '07'
if 'Август' in rot.text:
    g = '08'
if 'Сентябрь' in rot.text:
    g = '09'
if 'Октябрь' in rot.text:
    g = '10'
if 'Ноябрь' in rot.text:
    g = '11'
if 'Декабрь' in rot.text:
    g = '12'
if g == '01':
    rot2 = '1'
elif g == '02':
    rot2 = '2'
elif g == '03':
    rot2 = '3'
elif g == '04':
    rot2 = '4'
elif g == '05':
    rot2 = '5'
elif g == '06':
    rot2 = '6'
elif g == '07':
    rot2 = '7'
elif g == '08':
    rot2 = '8'
elif g == '09':
    rot2 = '9'
else:
    rot2 = g





    '''
bot.polling()