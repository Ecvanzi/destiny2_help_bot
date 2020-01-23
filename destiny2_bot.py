import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,  CallbackQueryHandler, ConversationHandler
from handlers import *
from xur import *
from events import *
from events_keyboards import events

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY, use_context=True)
    logging.info ('Бот запустился')
    dp = mybot.dispatcher
    
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CallbackQueryHandler(all_xur, pass_user_data=True, pattern = 'Xur'))
    #dp.add_handler(CallbackQueryHandler(challenge, pass_user_data=True, pattern = 'challenge'))
    #dp.add_handler(CallbackQueryHandler(raids, pass_user_data=True, pattern = 'raids'))
    #dp.add_handler(CallbackQueryHandler(weapon_list, pass_user_data=True, pattern = 'weapon_list'))
    dp.add_handler(CallbackQueryHandler(events, pass_user_data=True, pattern = 'events'))
    #dp.add_handler(CallbackQueryHandler(other, pass_user_data=True, pattern = 'other'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'glimmer_extraction'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'weapon_trade'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'ether_resupply'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'cabal_excavation'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'taken_blight'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'injection_rig'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'witches_ritual'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'spire_integration'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'fallen_satellite'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'vex_gate_lord'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'cryocapsule_escape'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'ether_ritual'))
    dp.add_handler(CallbackQueryHandler(get_event, pass_user_data=True, pattern = 'rift_generator'))
    dp.add_handler(CallbackQueryHandler(first_page, pass_user_data=True, pattern = 'first_page'))
    dp.add_handler(CallbackQueryHandler(second_page, pass_user_data=True, pattern = 'second_page'))
    dp.add_handler(CallbackQueryHandler(third_page, pass_user_data=True, pattern = 'third_page'))
    dp.add_handler(CallbackQueryHandler(fourth_page, pass_user_data=True, pattern = 'fourth_page'))
    dp.add_handler(CallbackQueryHandler(fifth_page, pass_user_data=True, pattern = 'fifth_page'))
    dp.add_handler(CallbackQueryHandler(events_keyboard, pass_user_data=True, pattern = 'events_keyboard'))
    dp.add_handler(CallbackQueryHandler(key_keyboard, pass_user_data=True, pattern = 'key_keyboard'))
    mybot.start_polling()
    mybot.idle()


if __name__=="__main__":
    main()