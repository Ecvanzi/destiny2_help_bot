import requests
from telegram.ext import Updater

import cloudscraper
import os

from bs4 import BeautifulSoup
from untils import keyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def greet_user(update, context):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе, "где Ксур?", какая сейчас неделя проклятья и как пройти рейд.
    '''.format(update.message.chat.first_name)
    keyboard = [
        [
        InlineKeyboardButton("Где Зур?", callback_data='Xur'),
        InlineKeyboardButton('Испытания', callback_data='challenge'),
        InlineKeyboardButton('Рейды', callback_data='raids')
        ],
        [
        InlineKeyboardButton('Оружейная', callback_data='weapon_list'),
        InlineKeyboardButton('Гардероб', callback_data='armory'),
        InlineKeyboardButton('Другое', callback_data='other')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text + "Выбирай категорию:", reply_markup=reply_markup)



def where_Xur(update, context):
    query = update.callback_query
    scraper = cloudscraper.create_scraper(delay=5)
    context.bot.send_message(chat_id=query.message.chat.id, text='Обрабатываю запрос')
    html = get_Xur('https://whereisxur.com/')
    Xur = 1
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        Xur_place = soup.find('h4', class_="title").string
        xp = Xur_place.replace("!", "").split(' ')
        if 'Titan' in xp :
            Xur_place = 'Зур прибыл на Титан.'
        elif 'Earth' in xp :
            Xur_place = "Зур прибыл на Землю."
        elif 'Nessus' in xp:
            Xur_place = 'Зур прибыл на Несс.'
        elif 'Io' in xp:
            Xur_place = 'Зур брибыл на Ио.'
        else :
            Xur_place = 'Зур отправился за новой партией экзотиков.'
            Xur = 0
        context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(Xur_place))
        if Xur == 1:
            Xur_image_url = soup.find('div', class_="et_pb_module et_pb_image et_pb_image_0").find('noscript').find("img")["src"]
            
            Xur_map = scraper.get(Xur_image_url, stream = True)
            with open('xur_place.png', 'wb') as f:
                f.write(Xur_map.content)
            context.bot.send_photo(chat_id=query.message.chat.id, photo=open('xur_place.png', 'rb'))
        else: 
            context.bot.send_message(chat_id=query.message.chat.id , text ='Картинки тоже не будет')
            
        
        
    else:
        context.bot.send_message(chat_id=query.message.chat.id, text ="Возникла ошибка")
    
def get_Xur(url):
    try:
        scraper = cloudscraper.create_scraper(delay=5)
        result = scraper.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')


    
    
  