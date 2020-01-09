from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

def keyboard():
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Зур','Испытания', 'Рейды'],
                                        ['Оружейная','Гардероб','Другое']],
                                        resize_keyboard= True, one_time_keyboard=True)


    return my_keyboard