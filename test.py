# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import telebot
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui as root

TOKEN = '1173699882:AAGpJD6jHDo7Wtb_Q7waQh3G8rNftkbRVko'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(bot.chat.id, 'Запишитесь к стоматологу')
    sleep(1.5)
    bot.send_message(bot.chat.id, 'Введите число, когда вам нужно к стоматологу например: 6 ')

d = input('Введите в какую дату вам нужно к зубному: ')
x = input('Введите во сколько вам нужно к зубному: ')
print('Ваше имя')   
name = str(input())
lastname = input('Ваша фамилия: ')
number = input('Ваш телефон: ')

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
sleep(2)
title = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
title.click()
title.send_keys(name + ' ' + lastname + ' ' + number)
sleep(2)
butt = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[3]/span')
butt.click()

bot.polling()