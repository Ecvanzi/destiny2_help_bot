import requests

import cloudscraper
import os

from settings import SQLALCHEMY_DATABASE_URI
from model import Xur_tab, md
from bs4 import BeautifulSoup
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine(SQLALCHEMY_DATABASE_URI)

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
            Xur_place = 'Зур прибыл на Титан. Будет ждать тебя до 20:00 вторника.'
        elif 'EDZ' in xp :
            Xur_place = "Зур прибыл на Землю. Будет ждать тебя до 20:00 вторника."
        elif 'Nessus' in xp:
            Xur_place = 'Зур прибыл на Несс. Будет ждать тебя до 20:00 вторника.'
        elif 'IO' in xp:
            Xur_place = 'Зур брибыл на Ио. Будет ждать тебя до 20:00 вторника.'
        else :
            Xur_place = 'Зур отправился за новой партией экзотиков.'
            Xur = 0
        #save_xur(Xur_place)
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

def save_xur(Xur_place):
    Session = sessionmaker()
    Session.configure(bind=engine)
    new_Xur_place = Xur_tab(Xur_place= Xur_place)
    md.session.add(new_Xur_place)
    md.session.commit()