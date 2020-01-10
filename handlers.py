
from telegram.ext import Updater
from datetime import *

import os


from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def greet_user(update, context):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе, "где Зур?", какая сейчас неделя проклятья и как пройти рейд.
    '''.format(update.message.chat.first_name)
    update.message.reply_text(text)
    main_keyboard(update)
    
    

def main_keyboard(update):
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
    update.message.reply_text("Выбирай категорию:", reply_markup=reply_markup)

def key_keyboard(update, context):
    query = update.callback_query
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
    context.bot.send_message(chat_id=query.message.chat.id,text = "Выбирай категорию:", reply_markup=reply_markup)
