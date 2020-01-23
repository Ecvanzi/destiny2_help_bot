from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def events(update, context):
    query = update.callback_query
    text = '''
    Вот список открытых мероприятий с указанием страницы на которой его искать:
    1) Добыча блеска, Обмен оружием, Пополнение запасов эфира
    2) Раскопки кабал, Очаг одержимых, Впускной механизм
    3) Ведьминский ритуал, Интеграция шпиля, Перекрестье вексов
    4) Упавший спутник, Побег в криокапсуле, Эфирный ритуал
    5) Генератор разлома
    '''
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text =text)
    events_keyboard(update, context)

def events_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('1', callback_data='first_page'),
        InlineKeyboardButton('2', callback_data='second_page'),
        InlineKeyboardButton('3', callback_data='third_page'),
        InlineKeyboardButton('4', callback_data='fourth_page'),
        InlineKeyboardButton('5', callback_data='fifth_page')
        ],
        [
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай страницу:', reply_markup = reply_markup)

def first_page(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Добыча блеска', callback_data='glimmer_extraction'),
        InlineKeyboardButton('Обмен оружием', callback_data='weapon_trade'),
        InlineKeyboardButton('Пополение запасов эфира', callback_data='ether_resupply')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Первая страница: Добыча блеска, Обмен оружием, Пополнение запасов эфира.', reply_markup = reply_markup)

def second_page(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton("Раскопки кабал", callback_data='cabal_excavation'),
        InlineKeyboardButton('Очаг одержимых', callback_data='taken_blight'),
        InlineKeyboardButton('Впускной механизм', callback_data='injection_rig')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Вторая страница: Раскопки кабал, Очаг одержимых, Впускной механизм.', reply_markup = reply_markup)

def third_page(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton("Ведьминский ритуал", callback_data='witches_ritual'),
        InlineKeyboardButton('Интеграция шпиля', callback_data='spire_integration'),
        InlineKeyboardButton('Перекрестье вексов', callback_data='vex_gate_lord')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Третья страница: Ведьминский ритуал, Интеграция шпиля, Перекрестье вексов.', reply_markup = reply_markup)

def fourth_page(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton("Упавший спутник", callback_data='fallen_satellite'),
        InlineKeyboardButton('Побег в криокапсуле', callback_data='cryocapsule_escape'),
        InlineKeyboardButton('Эфирный ритуал', callback_data='ether_ritual')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Четвертая страница: Упавший спутник, Побег в криокапсуле, Эфирный ритуал.', reply_markup = reply_markup)


def fifth_page(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton("Генератор разлома", callback_data='rift_generator')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard'),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Пятая страница: Генератор разлома.', reply_markup = reply_markup)

def key_menu(update, context, page):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Назад на страницу', callback_data = page),
        InlineKeyboardButton('Назад к выбору страниц', callback_data='events_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text = 'Куда дальше?', reply_markup = reply_markup)