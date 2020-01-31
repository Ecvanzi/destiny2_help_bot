from telegram import InlineKeyboardButton, InlineKeyboardMarkup




def events_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Добыча блеска', callback_data='glimmer_extraction'),
        InlineKeyboardButton('Обмен оружием', callback_data='weapon_trade')
        ],
        [
        InlineKeyboardButton('Пополение запасов эфира', callback_data='ether_resupply'),
        InlineKeyboardButton("Раскопки кабал", callback_data='cabal_excavation')
        ],
        [
        InlineKeyboardButton('Очаг одержимых', callback_data='taken_blight'),
        InlineKeyboardButton('Впускной механизм', callback_data='injection_rig')
        ],
        [
        InlineKeyboardButton("Ведьминский ритуал", callback_data='witches_ritual'),
        InlineKeyboardButton('Интеграция шпиля', callback_data='spire_integration')
        ],
        [
        InlineKeyboardButton('Перекрестье вексов', callback_data='vex_gate_lord'),
        InlineKeyboardButton("Упавший спутник", callback_data='fallen_satellite')
        ],
        [
        InlineKeyboardButton('Побег в криокапсуле', callback_data='cryocapsule_escape'),
        InlineKeyboardButton('Эфирный ритуал', callback_data='ether_ritual')
        ],
        [
        InlineKeyboardButton("Генератор разлома", callback_data='rift_generator')
        ],
        [
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Выбирай мероприятие.', reply_markup = reply_markup)

def key_menu(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Назад к выбору мероприятий', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Куда дальше?', reply_markup = reply_markup)