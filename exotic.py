from mongodb import db
from handlers import key_keyboard
from exotic_keyboard import *

def get_exotic_weapon(update, context):
    query = update.callback_query
    weapon_name = query.data
    weapon = db.exotic_weapons.find_one({"eng_name": weapon_name}, {"eng_name":1, "name":1, "type":1, "perk":1, "rate_of_fire":1, "ammo":1, "catalyst":1, "drop":1, "_id":0 })
    context.bot.send_photo(chat_id=query.message.chat.id, photo = open('exotics/weapons/{}.jpg'.format(weapon['eng_name']), 'rb'))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Название: {}'.format(weapon['name']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Тип оружия: {}'.format(weapon['type']))
    context.bot.send_message(chat_id=query.message.chat.id, text = '{}'.format(weapon['rate_of_fire']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Обойма: {}'.format(weapon['ammo']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Особенность: {}'.format(weapon['perk']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Что дает катализатор: {}'.format(weapon['catalyst']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Где достать: {}'.format(weapon['drop']))
    e_weapon_menu(update, context)
    
def get_exotic_armor(update, context):
    query = update.callback_query
    armor_name = query.data
    armor = db.exotic_armor.find_one({"eng_name": armor_name}, {"eng_name":1, "name":1, "type":1, "perk":1, "_id":0 })
    context.bot.send_photo(chat_id=query.message.chat.id, photo = open('exotics/armor/{}.jpg'.format(armor['eng_name']), 'rb'))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Название: {}'.format(armor['name']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Тип брони: {}'.format(armor['type']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Особенность: {}'.format(armor['perk']))
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Где достать: Экзотические энграммы, редкие выпадения в открытом мире.')
    e_armor_menu(update, context)