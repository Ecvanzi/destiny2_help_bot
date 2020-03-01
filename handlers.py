
from telegram.ext import Updater
from datetime import *

import os


from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def greet_user(update, context):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе,
     "где Зур?", какая сейчас неделя проклятья и как пройти рейд.
    '''.format(update.message.chat.first_name)
    update.message.reply_text(text)
    main_keyboard(update)


def main_keyboard(update):
    keyboard = [
        [
         InlineKeyboardButton("Где Зур?",
                              callback_data='xur'),
         InlineKeyboardButton('Экзотики',
                              callback_data='exotic'),
         InlineKeyboardButton('(Не работает)Рейды',
                              callback_data='raids')
        ],
        [
         InlineKeyboardButton('Оружейная',
                              callback_data='armory'),
         InlineKeyboardButton('Открытые мероприятия',
                              callback_data='events'),
         InlineKeyboardButton('(Не работает)Другое',
                              callback_data='other')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выбирай категорию:", reply_markup=reply_markup)


def key_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
         InlineKeyboardButton("Где Зур?",
                              callback_data='xur'),
         InlineKeyboardButton('Экзотики',
                              callback_data='exotic'),
         InlineKeyboardButton('(Не работает)Рейды',
                              callback_data='raids')
        ],
        [
         InlineKeyboardButton('Оружейная',
                              callback_data='armory'),
         InlineKeyboardButton('Открытые мероприятия',
                              callback_data='events'),
         InlineKeyboardButton('(Не работает)Другое',
                              callback_data='other')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id,
                             text="Выбирай категорию:",
                             reply_markup=reply_markup)


def xur_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
         InlineKeyboardButton('Где Зур и что он привез?',
                              callback_data='all_xur'),
         InlineKeyboardButton('Обновить Зура',
                              callback_data='xur_here')
        ],
        [
         InlineKeyboardButton('Главное меню',
                              callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id,
                             text='''
    "Выбирай. Если не уверен что данные Зура актуальны,
    то ты можешь обновить данные по Зуру и посмотреть еще раз."
                             ''',
                             reply_markup=reply_markup)
