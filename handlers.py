
from telegram.ext import Updater


import os

from untils import keyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def greet_user(update, context):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе, "где Зур?", какая сейчас неделя проклятья и как пройти рейд.
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



