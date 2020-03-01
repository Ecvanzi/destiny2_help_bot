from mongodb import db
from handlers import main_keyboard
from armory_keyboard import *

type_l = ['автомат', 'дробовик', 'скаутская винтовка', 'импульсная винтовка',
          'револьвер', 'пистолет', 'лук', 'гранатомет',
          'плазменная винтовка', 'пистолет пулемет', 'снайперская винтовка',
          'меч', 'ракетная установка', 'линейно-плазменная винтовка',
          'пулемет', 'дробь', 'дробаш', 'автик', 'пульса',  'скаутка',
          'ревик', 'ппшка', 'греник', 'плазма', 'снипа', 'снайпа',
          'ракетница', 'линейка', 'пулик']

weapon_l = ['былые обиды']


def i_know_what_i_want(update, context):
    cb = context.bot
    query = update.callback_query
    cb.send_message(chat_id=query.message.chat.id,
                    text='Введи название или тип оружия.')


def i_know_weapon(update, context):
    cb = context.bot
    user_message = update.message.text
    if user_message in type_l:
        print('типы')
        #find_weapon_type(user_message, update, context)
    elif user_message in weapon_l:
        print('название')
        #find_weapon(user_message, update, context)
    else:
        cb.send_message(chat_id=update.message.chat.id,
                        text='Не понял что ты имеешь в виду.')
        main_keyboard(update)


#def find_weapon_type(user_message, update, context):