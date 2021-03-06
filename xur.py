import requests

import cloudscraper

import os

from datetime import datetime

from bs4 import BeautifulSoup
from handlers import key_keyboard, xur_keyboard
from mongodb import save_xur_place, save_xur_img, save_xur_weapon, db


def xur_here(update, context):
    cb = context.bot
    query = update.callback_query
    cb.send_message(chat_id=query.message.chat.id, text='Обновляю данные')
    where_xur()
    xur_weapon()
    cb.send_message(chat_id=query.message.chat.id, text='Данные обновлены')
    xur_keyboard(update, context)


def all_xur(update, context):
    cb = context.bot
    query = update.callback_query
    cb.edit_message_text(chat_id=query.message.chat.id,
                         message_id=query.message.message_id, text='Где Зур')
    date_now = datetime.today().isoweekday()
    Xur_place = "Зур уехал, приедет в пятницу в 20:00."

    if date_now == 1 or date_now > 4:

        xur_point = db.xur_tab.find_one({}, {"xur_place": 1, "_id": 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(xur_point['xur_place']))
        cb.send_photo(chat_id=query.message.chat.id,
                      photo=open('xur_img/xur_place.png', 'rb'))

        xur_weapon_db = db.xur_tab.find_one({}, {'xur_first_weapon': 1,
                                                 "xur_second_weapon": 1,
                                                 "xur_third_weapon": 1,
                                                 "xur_fourth_weapon": 1,
                                                 "_id": 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(xur_weapon_db['xur_first_weapon']))
        cb.send_photo(chat_id=query.message.chat.id,
                      photo=open('xur_img/img_first_weapon.png', 'rb'))
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(xur_weapon_db['xur_second_weapon']))
        cb.send_photo(chat_id=query.message.chat.id,
                      photo=open('xur_img/img_second_weapon.png', 'rb'))
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(xur_weapon_db['xur_third_weapon']))
        cb.send_photo(chat_id=query.message.chat.id,
                      photo=open('xur_img/img_third_weapon.png', 'rb'))
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(xur_weapon_db['xur_fourth_weapon']))
        cb.send_photo(chat_id=query.message.chat.id,
                      photo=open('xur_img/img_fourth_weapon.png', 'rb'))

    else:
        save_xur_place(db, Xur_place)
        xur_point = db.xur_tab.find_one({}, {"xur_place": 1,
                                             "_id": 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(xur_point['xur_place']))

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


def xur_weapon():
    scraper = cloudscraper.create_scraper(
            delay=5,
            recaptcha={'provider': 'return_response'}
    )

    html = get_xur('https://whereisxur.com/')
    soup = BeautifulSoup(html, 'html.parser')
    xur_first_weapon = soup.find('div', class_="et_pb_blurb_0").find('h4', class_='et_pb_module_header').find('span').string
    url_first_weapon = soup.find('div', class_="et_pb_blurb_0").find('noscript').find("img")["src"]
    first_img = scraper.get(url_first_weapon, stream=True)
    with open('xur_img/img_first_weapon.png', 'wb') as f:
                f.write(first_img.content)

    xur_second_weapon = soup.find('div', class_="et_pb_blurb_1").find('h4', class_='et_pb_module_header').find('span').string
    url_second_weapon = soup.find('div', class_="et_pb_blurb_1").find('noscript').find("img")["src"]
    second_img = scraper.get(url_second_weapon, stream=True)
    with open('xur_img/img_second_weapon.png', 'wb') as f:
        f.write(second_img.content)

    xur_third_weapon = soup.find('div', class_="et_pb_blurb_2").find('h4', class_='et_pb_module_header').find('span').string
    url_third_weapon = soup.find('div', class_="et_pb_blurb_2").find('noscript').find("img")["src"]
    third_img = scraper.get(url_third_weapon, stream=True)
    with open('xur_img/img_third_weapon.png', 'wb') as f:
        f.write(third_img.content)

    xur_fourth_weapon = soup.find('div', class_="et_pb_blurb_3").find('h4', class_='et_pb_module_header').find('span').string
    url_fourth_weapon = soup.find('div', class_="et_pb_blurb_3").find('noscript').find("img")["src"]
    fourth_img = scraper.get(url_fourth_weapon, stream=True)
    with open('xur_img/img_fourth_weapon.png', 'wb') as f:
        f.write(fourth_img.content)
    save_xur_weapon(db, xur_first_weapon, xur_second_weapon,
                    xur_third_weapon, xur_fourth_weapon)


def where_xur():
    scraper = cloudscraper.create_scraper(
            delay=5,
            recaptcha={'provider': 'return_response'}
    )
    html = get_xur('https://whereisxur.com/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        xur_place = soup.find('h4', class_="title").string
        xp = xur_place.replace("!", "").split(' ')

        if 'Titan' in xp:
            xur_place = 'Зур прибыл на Титан. Будет там до 20:00 вторника.'
        elif 'EDZ' in xp:
            xur_place = "Зур прибыл на Землю. Будет там до 20:00 вторника."
        elif 'Nessus' in xp:
            xur_place = 'Зур прибыл на Несс. Будет там до 20:00 вторника.'
        elif 'IO' in xp:
            xur_place = 'Зур прибыл на Ио. Будет там до 20:00 вторника.'
        else:
            xur_place = 'Зур прибудет в пятницу в 20:00.'

        save_xur_place(db, xur_place)
        xur_image_url = soup.find('div', class_="et_pb_module et_pb_image et_pb_image_0").find('noscript').find("img")["src"]
        save_xur_img(db, xur_image_url)
        xur_map = scraper.get(xur_image_url, stream=True)
        with open('xur_img/xur_place.png', 'wb') as f:
            f.write(xur_map.content)

    else:
        xur_place = "Возникла ошибка при работе бота."

