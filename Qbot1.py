import datetime
from datetime import datetime

import telebot

import const
from const import bot_token as token

import botusers as users


#api = QApi(token=const.qw_token, phone=const.qw_login)
bot = telebot.TeleBot(token)


def listener(messages):  # only used for console output now

    for m in messages:
        if m.content_type == 'text':
            print(str(datetime.now()) + " - [" + str(m.chat.id) +
                  "]: " + str(m.chat.first_name) + ": - " + m.text)


@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = '''Приветствую тебя друг!!!
    Ты находишься в Административной панели бота автопродаж.
    Вот список доступных команд:
    /des - добавит описание твоего магазина. То, что пользователь
    увидит, нажав кнопку '/start'.
    /help - инструкции под кнопку 'помощь'
    /gorod - После ее ввода добавляется новый город и автоматически
    продолжается ввод данных по предлагаемым тобой товарам.
    /set - Настройка существующего бота'''

    new_user = message.from_user.id
    if new_user not in users:
        users.append(new_user)
        with open('botusers.py', 'w') as file:
            file.write('users = [' + str(users) + ']')



    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row("Добавить Qiwi кошелек")
    user_markup.row("Проверить свой iP адрес")

    bot.send_message(message.from_user.id, answer, reply_markup = user_markup)


@bot.message_handler(commands=['set'])
def handle_set(message):
    answer = 'Ушли твои деньги. Не всмысле ушлт, а всмыле отправил я. Ну ты меня понял!!!'
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    bot.send_message(message.from_user.id, answer, reply_markup = user_markup)


@bot.message_handler(func=lambda message: message.text == "Добавить Qiwi кошелек")
# bot.message_handler(content_types=['text'])
def handle_text_all(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    user_markup.row('Россия', 'Казахстан')
    user_markup.row('Украина', 'Узбекистан')
    user_markup.row("Заполнить анкету(девушкам)")
    answer = 'Для начала выберите страну'

    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)

'''import telebot
from telebot import types

import const
import json
import tobase
#import pymongo
#url = 'mongodb+srv://Svet:552026@devky-yc6iv.gcp.mongodb.net/Devky?retryWrites=true&w=majority'

from datetime import datetime
from const import bot_token as token, data, next_photo

country = 'Казахстан'
#girls = []




        
        if m.content_type == 'photo':
            print('\n'+str(m))
            

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("А можно всех посмотреть")
    user_markup.row("Заполнить анкету(девушкам)")

    answer = 
    Приветствую тебя друг!!!
    Ты находишься в Боте приватных знакомств.
        Мои контакты - @jogav

    tobase.usr_db(usr = message.from_user)#Запишем в users нового пользователя
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    #bot.send_chat_action(message.from_user.id, 'А-а-а-а блять...')
    bot.send_photo(message.from_user.id, "AgACAgIAAxkDAAIaE15zyv95Cm3yAns1z19kVWxuLW_aAAIGrjEbXgaZS8xRPeJAO4kKHJ51kS4AAwEAAwIAA20AA7AwAQABGAQ")
        
    




@bot.message_handler(func=lambda message: message.text in data.keys())
#bot.message_handler(content_types=['text'])
def handle_text_cities(message):

    country = message.text
    print('----------------------------> coutry = ' + country)
    
    
    btn = data[country]
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row(btn[0], btn[1], btn[2], btn[3])
    user_markup.row(btn[4], btn[5], btn[6], btn[7])
    user_markup.row(btn[8], btn[9], btn[10], btn[11])
    user_markup.row('Вернуться в начало')
    
    answer = 'Так держать'
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    return country
     
    
@bot.message_handler(func=lambda message: message.text in data[country])
#bot.message_handler(content_types=['text'])
def handle_text_girls(message, next_photo=1):
       
    city = message.text
    print('----------------------------> country+city = ' + city)
    
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    
    for i in tobase.go_girls(country, city, next_photo):
        file_id=i['photo_id']
        answer=city+' - '+i['name']
        bot.send_photo(message.from_user.id, file_id)
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

    user_markup.row('Другой город','Следующие 5')
    user_markup.row('Украина', 'Узбекистан')
    next_photo = + 5

    return next_photo  
         
     
    

@bot.message_handler(func=lambda message: message.text == 'Следующие')
#bot.message_handler(content_types=['text'])
def handle_text_five(message):
    n=+5
    go_five(n)
                   
    
    

@bot.message_handler(func=lambda message: message.text == 'Вернуться в начало')
#bot.message_handler(content_types=['text'])
def handle_text_start(message):
    commands = ['start']
    handle_start(message)

      


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    # this is the standard reply to a normal message
    bot.send_message(message.chat.id, "I don't understand \"" +
                     message.text + "\"\nMaybe try the help page at /help")

bot.set_update_listener(listener)  # register listener


try:
    if __name__ == '__main__':
        bot.polling(none_stop=True)
except:
    Exception('ConnectTimeoutError')



    if message.text == 'Вернуться в начало':
        handle_start(message=message)
        #message.text = '/start'
        answer = 'Возвращаемся'

    btn_anket = telebot.types.KeyboardButton(
        text='https://t.me/devky_bot?command=/start'

    user_markup=telebot.types.InlineKeyboardMarkup()
        btn_my_site=telebot.types.InlineKeyboardButton(
            text='Вернуться в начало', url='https://t.me/devky_bot?/start')
        user_markup.add(btn_my_site)


@bot.message_handler(commands=['switch'])
def switch(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    switch_button = telebot.types.InlineKeyboardButton(
        text='Try', switch_inline_query="Telegram")
    user_markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат",
                     reply_markup=user_markup)






for i in 'Марат Привет!':
    kz=str(api.balance[1])
    ru=str(api.balance[0])
    print ((kz)+"тенге")
    print('До перечисления - '+(kz)+ 'тенге, '+(ru)+'рублей')
    t=str(i)
    api.pay(account="+77764934066", amount=1, comment=(t))
    print(api.balance)
    kz=str(api.balance[1])
    ru=str(api.balance[0])
    print('После перечисления - '+(kz)+ 'тенге, '+(ru)+'рублей')
    '''
