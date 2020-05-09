# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import telebot
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
    bot.send_message(message.chat.id, 'Введите число, когда вам нужно к стоматологу например: 6 ')
    



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
    sleep(5)
    driver.quit()

@bot.message_handler(content_types=['text'])
def text(message):
    global d
    d = message.text    
    print(d)
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
    





    
bot.polling()