import requests

import cloudscraper
import os
from datetime import *

from bs4 import BeautifulSoup
from handlers import key_keyboard
from mongodb import save_xur_place, save_xur_weapon, db

def all_xur(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Где Зур')
    date_now = datetime.today().isoweekday()
    Xur_place = "Зур уехал, приедет в пятницу в 20:00."    

    if date_now == 1 or date_now > 4:
        where_xur(update, context)

        xur_point = db.xur_tab.find_one({}, {"xur_place": 1, "_id":0})
        context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(xur_point['xur_place']))
        xur_weapon(update, context)
        
        
    else:
        save_xur_place(db, Xur_place)
        xur_point = db.xur_tab.find_one({}, {"xur_place": 1, "_id":0})
        context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(xur_point['xur_place']))

    key_keyboard(update, context)
    
def get_xur(url):
    try:
        scraper = cloudscraper.create_scraper(
            delay=5, 
            recaptcha={'provider': 'return_response'}
    )
        result = scraper.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')

def xur_weapon(update, context):
    query = update.callback_query
    scraper = cloudscraper.create_scraper(
            delay=5, 
            recaptcha={'provider': 'return_response'}
    )

    html = get_xur('https://whereisxur.com/')
    soup = BeautifulSoup(html, 'html.parser')
    xur_first_weapon = soup.find('div', class_="et_pb_blurb_0").find('h4', class_='et_pb_module_header').find('span').string
    url_first_weapon = soup.find('div', class_="et_pb_blurb_0").find('noscript').find("img")["src"]
    first_img = scraper.get(url_first_weapon, stream = True)
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(xur_first_weapon))
    first_img = scraper.get(url_first_weapon, stream = True)
    with open('img_first_weapon.png', 'wb') as f:
                f.write(first_img.content)
    context.bot.send_photo(chat_id=query.message.chat.id, photo=open('img_first_weapon.png', 'rb'))

    xur_second_weapon = soup.find('div', class_="et_pb_blurb_1").find('h4', class_='et_pb_module_header').find('span').string
    url_second_weapon = soup.find('div', class_="et_pb_blurb_1").find('noscript').find("img")["src"]
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(xur_second_weapon))
    second_img = scraper.get(url_second_weapon, stream = True)
    with open('img_second_weapon.png', 'wb') as f:
                f.write(second_img.content)
    context.bot.send_photo(chat_id=query.message.chat.id, photo=open('img_second_weapon.png', 'rb'))

    xur_third_weapon = soup.find('div', class_="et_pb_blurb_2").find('h4', class_='et_pb_module_header').find('span').string
    url_third_weapon = soup.find('div', class_="et_pb_blurb_2").find('noscript').find("img")["src"]
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(xur_third_weapon))
    third_img = scraper.get(url_third_weapon, stream = True)
    with open('img_third_weapon.png', 'wb') as f:
                f.write(third_img.content)
    context.bot.send_photo(chat_id=query.message.chat.id, photo=open('img_third_weapon.png', 'rb'))

    xur_fourth_weapon = soup.find('div', class_="et_pb_blurb_3").find('h4', class_='et_pb_module_header').find('span').string
    url_fourth_weapon = soup.find('div', class_="et_pb_blurb_3").find('noscript').find("img")["src"]
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(xur_fourth_weapon))
    fourth_img = scraper.get(url_fourth_weapon, stream = True)
    with open('img_fourth_weapon.png', 'wb') as f:
                f.write(fourth_img.content)
    context.bot.send_photo(chat_id=query.message.chat.id, photo=open('img_fourth_weapon.png', 'rb'))
    save_xur_weapon(db, xur_first_weapon, url_first_weapon, xur_second_weapon, url_second_weapon, xur_third_weapon, url_third_weapon, xur_fourth_weapon, url_fourth_weapon)



def where_xur(update, context):
    query = update.callback_query
    scraper = cloudscraper.create_scraper(
            delay=5, 
            recaptcha={'provider': 'return_response'}
    )
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
        save_xur_place(db, Xur_place)
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
