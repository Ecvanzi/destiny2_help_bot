from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

def keyboard():
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Испытания','Город грез', 'Рейды'],
                                        ['Открытые мероприятия','Оружейная','Другое']],
                                        resize_keyboard= True)

    return my_keyboard