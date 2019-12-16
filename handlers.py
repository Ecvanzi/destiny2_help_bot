from untils import keyboard
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def greet_user(bot, update, user_data):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе, "где Ксур?", какая сейчас неделя проклятья и как пройти рейд.'''.format(update.message.chat.first_name)
    keyboard = [[InlineKeyboardButton("Где Зур?", callback_data='')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text,  reply_markup=reply_markup)

def where_Xur(bot, update, user_data):
    text = 'Зур сегодня ...'
    update.message.reply_text(text)

