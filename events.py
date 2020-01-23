from mongodb import db
from handlers import key_keyboard
from events_keyboards import *


def glimmer_extraction(update, context):
    page = 'first_page'
    event_name = "Добыча блеска."
    send_event(update, context, event_name)
    key_menu(update, context, page)
    
def weapon_trade(update, context):
    page = 'first_page'
    event_name = "Обмен оружием."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def ether_resupply(update, context):
    page = 'first_page'
    event_name = "Пополнение запасов эфира."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def cabal_excavation(update, context):
    page = 'second_page'
    event_name = "Раскопки Кабал."
    send_event(update, context, event_name)
    key_menu(update, context, page)
    
def taken_blight(update, context):
    page = 'second_page'
    event_name = "Очаг одержимых."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def injection_rig(update, context):
    page = 'second_page'
    event_name = "Впускной механизм."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def witches_ritual(update, context):
    page = 'third_page'
    event_name = "Ведьминский ритуал."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def spire_integration(update, context):
    page = 'third_page'
    event_name = "Интеграция шпиля."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def fallen_satellite(update, context):
    page = 'third_page'
    event_name = "Упавший спутник."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def vex_gate_lord(update, context):
    page = 'fourth_page'
    event_name = "Перекрестье вексов."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def cryocapsule_escape(update, context):
    page = 'fourth_page'
    event_name = "Побег в крио-капсуле."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def ether_ritual(update, context):
    page = 'fourth_page'
    event_name = "Эфирный ритуал."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def rift_generator(update, context):
    page = 'fifth_page'
    event_name = "Генератор разлома."
    send_event(update, context, event_name)
    key_menu(update, context, page)

def send_event(update, context, event_name):
    query = update.callback_query
    event = db.open_events.find_one({"event_name": event_name }, {"event_name": 1, "about":1, "heroic":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))