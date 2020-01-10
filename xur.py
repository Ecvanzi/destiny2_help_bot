import requests

import cloudscraper
import os
from datetime import *

from settings import SQLALCHEMY_DATABASE_URI
from model import Xur_tab
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from handlers import key_keyboard


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def where_xur(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Где Зур')
    date_now = datetime.today().isoweekday()
    if date_now == 1 or date_now > 2:
        scraper = cloudscraper.create_scraper(delay=5)
        context.bot.send_message(chat_id=query.message.chat.id, text='Обрабатываю запрос')
        html = get_xur('https://whereisxur.com/')
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            Xur_place = soup.find('h4', class_="title").string
            xp = Xur_place.replace("!", "").split(' ')
            Xur = 1
            if 'Titan' in xp :
                Xur_place = 'Зур прибыл на Титан. Будет ждать тебя до 20:00 вторника.'
            elif 'EDZ' in xp :
                Xur_place = "Зур прибыл на Землю. Будет ждать тебя до 20:00 вторника."
            elif 'Nessus' in xp:
                Xur_place = 'Зур прибыл на Несс. Будет ждать тебя до 20:00 вторника.'
            elif 'IO' in xp:
                Xur_place = 'Зур брибыл на Ио. Будет ждать тебя до 20:00 вторника.'
            else :
                Xur_place = 'Зур прибудет в пятницу в 20:00.'
                Xur = 0
            save_xur(Xur_place)
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
    else:
        context.bot.send_message(chat_id=query.message.chat.id, text ="Зур уехал, приедет в пятницу в 20:00.")
    key_keyboard(update, context)
    
    
    
    
def get_xur(url):
    try:
        scraper = cloudscraper.create_scraper(delay=5)
        result = scraper.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')

def save_xur(Xur_place):
    new_xur_place = Xur_tab(Xur_place= Xur_place)
    update(Xur_tab).where(Xur_tab.c.id==1).\
        values(Xur_place= Xur_place)
    session.commit()