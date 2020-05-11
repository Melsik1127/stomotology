import telebot
import datetime
from utils.telegramcalendar import create_calendar
from telebot import apihelper

apihelper.proxies = {'https': 'socks5://telegram.vpn99.net:55655'}
bot = telebot.TeleBot("1173699882:AAGpJD6jHDo7Wtb_Q7waQh3G8rNftkbRVko")
current_shown_dates={}


@bot.message_handler(commands=['calendar'])
def handle_calendar_command(message):

    now = datetime.datetime.now()
    chat_id = message.chat.id

    date = (now.year, now.month)
    current_shown_dates[chat_id] = date
    
    markup = create_calendar(now.year, now.month)

    bot.send_message(message.chat.id, "Выберите дату:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'DAY' in call.data[0:13])
def handle_day_query(call):
    chat_id = call.message.chat.id
    saved_date = current_shown_dates.get(chat_id)
    last_sep = call.data.rfind(';') + 1
    m = call.data[4:8]
    rot2 = call.data[9:11]
    newstr = call.data.replace(";", " ") 
    m = newstr.split()[1]
    rot2 = newstr.split()[2]
    d = newstr.split()[3]
    print(m + '/' + rot2 + '/' + d)


    if saved_date is not None:

        day = call.data[last_sep:]
        date = datetime.datetime(int(saved_date[0]), int(saved_date[1]), int(day), 0, 0, 0)
        bot.send_message(chat_id=chat_id, text='Вы успешно выбрали дату')
        bot.answer_callback_query(call.id, text="")

    else:
        # add your reaction for shown an error
        pass


@bot.callback_query_handler(func=lambda call: 'MONTH' in call.data)
def handle_month_query(call):

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
    bot.answer_callback_query(call.id, text="Это не дата!")


if __name__ == "__main__":
    bot.polling()