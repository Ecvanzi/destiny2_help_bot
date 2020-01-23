from mongodb import db
from handlers import key_keyboard
from events_keyboards import *


def glimmer_extraction(update, context):
    query = update.callback_query
    page = 'first_page'
    event = db.open_events.find_one({"event_name":"Добыча блеска."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)
    
def weapon_trade(update, context):
    query = update.callback_query
    page = 'first_page'
    event = db.open_events.find_one({"event_name":"Обмен оружием."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def ether_resupply(update, context):
    query = update.callback_query
    page = 'first_page'
    event = db.open_events.find_one({"event_name":"Пополнение запасов эфира."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def cabal_excavation(update, context):
    query = update.callback_query
    page = 'second_page'
    event = db.open_events.find_one({"event_name":"Раскопки Кабал."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)
    
def taken_blight(update, context):
    query = update.callback_query
    page = 'second_page'
    event = db.open_events.find_one({"event_name":"Очаг одержимых."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def injection_rig(update, context):
    query = update.callback_query
    page = 'second_page'
    event = db.open_events.find_one({"event_name":"Впускной механизм."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def witches_ritual(update, context):
    query = update.callback_query
    page = 'third_page'
    event = db.open_events.find_one({"event_name":"Ведьминский ритуал."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def spire_integration(update, context):
    query = update.callback_query
    page = 'third_page'
    event = db.open_events.find_one({"event_name":"Интеграция шпиля."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def fallen_satellite(update, context):
    query = update.callback_query
    page = 'third_page'
    event = db.open_events.find_one({"event_name":"Упавший спутник."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def vex_gate_lord(update, context):
    query = update.callback_query
    page = 'fourth_page'
    event = db.open_events.find_one({"event_name":"Перекрестье вексов."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def cryocapsule_escape(update, context):
    query = update.callback_query
    page = 'fourth_page'
    event = db.open_events.find_one({"event_name":"Побег в крио-капсуле."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def ether_ritual(update, context):
    query = update.callback_query
    page = 'fourth_page'
    event = db.open_events.find_one({"event_name":"Эфирный ритуал."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

def rift_generator(update, context):
    query = update.callback_query
    page = 'fifth_page'
    event = db.open_events.find_one({"event_name":"Генератор разлома."}, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    key_menu(update, context, page)

