import requests
from telegram.ext import Updater

import cloudscraper
import os

from bs4 import BeautifulSoup
from untils import keyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


import cloudscraper

def greet_user(bot, update, user_data):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе, "где Ксур?", какая сейчас неделя проклятья и как пройти рейд.'''.format(update.message.chat.first_name)
    keyboard = [[InlineKeyboardButton("Где Зур?", callback_data='/Xur')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text,  reply_markup=reply_markup)

def where_Xur(bot, update, user_data):
    update.message.reply_text('Обрабатываю запрос')
    html = get_Xur('https://whereisxur.com/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        Xur_place = soup.find('h4', class_="title").string
        update.message.reply_text(Xur_place)
        image = soup.find('div', class_="et_pb_module et_pb_image et_pb_image_0").find("img")
        os.makedirs('downloads', exist_ok=True)
        print(image)
        #Xur_map = 
        print(image.attrs) #чтобы понять что внутри и какие есть тэги и атрибуты
    else:
        update.message.reply_text("Возникла ошибка")
    
def get_Xur(url):
    try:
        scraper = cloudscraper.create_scraper(delay=5)
        result = scraper.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')



        

