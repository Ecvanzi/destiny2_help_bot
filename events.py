from mongodb import db
from handlers import key_keyboard
from events_keyboards import *


def get_event(update, context):
    query = update.callback_query
    event_name = query.data
    event = db.open_events.find_one({"eng_name": event_name }, {"event_name": 1, "about":1, "heroic":1,"page":1, "_id":0})
    context.bot.send_message(chat_id=query.message.chat.id, text='{}'.format(event['event_name']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Обычное прохождение: {}'.format(event['about']))
    context.bot.send_message(chat_id=query.message.chat.id, text='Героический режим: {}'.format(event['heroic']))
    page = "{}".format(event['page'])
    key_menu(update, context, page)