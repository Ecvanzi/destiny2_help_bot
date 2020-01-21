import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,  CallbackQueryHandler, ConversationHandler
from handlers import *
from xur import *


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
    dp.add_handler(CallbackQueryHandler(xur_weapon, pass_user_data=True, pattern = 'challenge'))
    #dp.add_handler(CallbackQueryHandler(raids, pass_user_data=True, pattern = 'raids'))
    #dp.add_handler(CallbackQueryHandler(weapon_list, pass_user_data=True, pattern = 'weapon_list'))
    #dp.add_handler(CallbackQueryHandler(armory, pass_user_data=True, pattern = 'armory'))
    #dp.add_handler(CallbackQueryHandler(other, pass_user_data=True, pattern = 'other'))


    mybot.start_polling()
    mybot.idle()


if __name__=="__main__":
    main()