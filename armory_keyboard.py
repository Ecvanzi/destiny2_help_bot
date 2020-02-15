from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def armory_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Знаю что мне нужно', callback_data='i_know_weapon'),
        InlineKeyboardButton('Не знаю что мне нужно', callback_data='weapon_keyboard')
        ],
        [
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')    
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай раздел:', reply_markup = reply_markup)

def weapon_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Обычные патроны', callback_data = 'light_ammo'),
        InlineKeyboardButton('Особые патроны', callback_data = 'special_ammo'),
        InlineKeyboardButton('Силовые патроны', callback_data = 'heavy_ammo')
        ],
        [
        InlineKeyboardButton('Назад', callback_data = 'armory_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data = 'key_keyboard')   
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай раздел:', reply_markup = reply_markup)

def light_ammo(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Автоматы', callback_data = 'auto_rifles'),
        InlineKeyboardButton('Винтовки разведчика', callback_data = 'scout_rifles')
        ],
        [
        InlineKeyboardButton('Импульсные винтовки', callback_data = 'pulse_rifles'),
        InlineKeyboardButton('Револьверы', callback_data = 'hand_cannons')
        ],
        [
        InlineKeyboardButton('Пистолеты-пулеметы', callback_data = 'submachine_guns'),
        InlineKeyboardButton('Пистолеты', callback_data = 'sidearms')
        ],
        [
        InlineKeyboardButton('Луки', callback_data = 'combat_bows')
        ],
        [
        InlineKeyboardButton('Назад', callback_data = 'weapon_keyboard'),
        InlineKeyboardButton('В раздел', callback_data = 'armory_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data = 'key_keyboard')   
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай раздел:', reply_markup = reply_markup)

def special_ammo(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Дробовики', callback_data = 'shotguns'),
        InlineKeyboardButton('Гранатометы', callback_data = 'grenade_launchers')
        ],
        [
        InlineKeyboardButton('Плазменные винтовки', callback_data = 'fusion_rifles'),
        InlineKeyboardButton('Снайперские винтовки', callback_data = 'sniper_rifles')
        ],
        [
        InlineKeyboardButton('Назад', callback_data = 'weapon_keyboard'),
        InlineKeyboardButton('В раздел', callback_data = 'armory_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data = 'key_keyboard')   
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай раздел:', reply_markup = reply_markup)

def heavy_ammo(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Мечи', callback_data = 'swords'),
        InlineKeyboardButton('Гранатометы', callback_data = 'heavy_grenade_launchers')
        ],
        [
        InlineKeyboardButton('Ракетные установки', callback_data = 'rocket_launchers'),
        InlineKeyboardButton('ЛИнейно-плазменные винтовки', callback_data = 'linear_fusion_rifles')
        ],
        [
        InlineKeyboardButton('Пулеметы', callback_data = 'machine_guns')
        ],
        [
        InlineKeyboardButton('Назад', callback_data = 'weapon_keyboard'),
        InlineKeyboardButton('В раздел', callback_data = 'armory_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data = 'key_keyboard')   
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай раздел:', reply_markup = reply_markup)