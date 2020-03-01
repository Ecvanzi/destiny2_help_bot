from mongodb import db
from handlers import key_keyboard
from exotic_keyboard import e_weapon_menu, e_armor_menu


def get_exotic_weapon(update, context):
    query = update.callback_query
    cb = context.bot
    weapon_name = query.data
    weapon = db.exotic_weapons.find_one({"eng_name": weapon_name},
                                        {"eng_name": 1,
                                         "name": 1,
                                         "type": 1,
                                         "rate_of_fire": 1,
                                         "ammo": 1,
                                         "catalyst": 1,
                                         "drop": 1,
                                         "_id": 0})
    cb.send_photo(chat_id=query.message.chat.id,
                  photo=open(
                             'exotics/weapons/{}.jpg'
                             .format(weapon['eng_name']), 'rb'))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Название: {}'
                    .format(weapon['name']))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Тип оружия: {}'
                    .format(weapon['type']))
    weapon_perks(update, context, weapon_name)
    type_weapon(update, context, weapon_name)
    cb.send_message(chat_id=query.message.chat.id,
                    text='Катализатор: {}'
                    .format(weapon['catalyst']))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Где достать: {}'
                    .format(weapon['drop']))
    e_weapon_menu(update, context)


def get_exotic_armor(update, context):
    query = update.callback_query
    armor_name = query.data
    cb = context.bot
    armor = db.exotic_armor.find_one({"eng_name": armor_name},
                                     {"eng_name": 1,
                                      "name": 1,
                                      "type": 1,
                                      "perk": 1,
                                      "_id": 0})
    cb.send_photo(chat_id=query.message.chat.id,
                  photo=open('exotics/armor/{}.jpg'
                             .format(armor['eng_name']), 'rb'))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Название: {}'
                    .format(armor['name']))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Тип брони: {}'
                    .format(armor['type']))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Особенность: {}'
                    .format(armor['perk']))
    cb.send_message(chat_id=query.message.chat.id,
                    text='Где достать: Экзотические энграммы.')
    e_armor_menu(update, context)


def weapon_perks(update, context, weapon_name):
    query = update.callback_query
    cb = context.bot
    perks = db.exotic_weapons.find_one({'eng_name': weapon_name},
                                       {"num_of_perks": 1,
                                        "_id": 0})
    num_of_perks = perks['num_of_perks']
    if num_of_perks == 1:
        one_perk = db.exotic_weapons.find_one({'eng_name': weapon_name},
                                              {'perk1': 1,
                                               '_id': 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(one_perk['perk1']))
    elif num_of_perks == 2:
        two_perks = db.exotic_weapons.find_one({"eng_name": weapon_name},
                                               {"perk1": 1,
                                                "perk2": 1,
                                                "_id": 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(two_perks['perk1']))
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(two_perks['perk2']))
    else:
        cb.send_message(chat_id=query.message.chat.id,
                        text='Возникла ошибка')


def type_weapon(update, context, weapon_name):
    query = update.callback_query
    cb = context.bot
    bow = db.exotic_weapons.find_one({'eng_name': weapon_name},
                                     {'type': 1,
                                      "_id": 0})
    weapon_type = bow['type']
    if weapon_type == 'Лук':
        bow = db.exotic_weapons.find_one({'eng_name': weapon_name},
                                         {'rate_of_fire': 1,
                                          "_id": 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(bow['rate_of_fire']))
    elif weapon_type == 'Меч':
        cb.send_message(chat_id=query.message.chat.id,
                        text='Резерв: 62')
    else:
        bow = db.exotic_weapons.find_one({'eng_name': weapon_name},
                                         {'rate_of_fire': 1,
                                          'ammo': 1,
                                          "_id": 0})
        cb.send_message(chat_id=query.message.chat.id,
                        text='{}'.format(bow['rate_of_fire']))
        cb.send_message(chat_id=query.message.chat.id,
                        text='Обойма: {}'.format(bow['ammo']))
