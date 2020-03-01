import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackQueryHandler
from handlers import greet_user, key_keyboard, xur_keyboard, main_keyboard
from xur import xur_here, all_xur
from events import get_event
from events_keyboards import events_keyboard, event_list
from armory import type_l, weapon_l, i_know_weapon
from armory import i_know_what_i_want
from armory_keyboard import armory_keyboard, weapon_keyboard
from armory_keyboard import light_ammo, special_ammo, heavy_ammo
from exotic import get_exotic_armor, get_exotic_weapon
from exotic_keyboard import warlock_exotic, exot_armor, exot_weapon
from exotic_keyboard import exotic_guns, kinetic_exotic, energo_exotic
from exotic_keyboard import heavy_exotic, titan_exotic, hunter_exotic
from exotic_keyboard import exotic_keyboard, exotic_armor
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY,
                    use_context=True)
    logging.info('Бот запустился')
    dp = mybot.dispatcher
    cqh = CallbackQueryHandler
    mh = MessageHandler
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(mh(Filters.regex('({})'.format(type_l).format(weapon_l)),
                      i_know_weapon, pass_user_data=True))
    dp.add_handler(cqh(i_know_what_i_want, pass_user_data=True,
                       pattern='i_know_what_i_want'))
    dp.add_handler(cqh(xur_keyboard, pass_user_data=True, pattern='xur'))
    dp.add_handler(cqh(all_xur, pass_user_data=True, pattern='all_xur'))
    dp.add_handler(cqh(xur_here, pass_user_data=True, pattern='xur_here'))
    dp.add_handler(cqh(exotic_keyboard, pass_user_data=True, pattern='exotic'))
    #dp.add_handler(cqh(, pass_user_data=True, pattern = 'raids'))
    dp.add_handler(cqh(armory_keyboard, pass_user_data=True, pattern='armory'))
    dp.add_handler(cqh(events_keyboard, pass_user_data=True, pattern='events'))
    #dp.add_handler(cqh(, pass_user_data=True, pattern = 'other'))
    for event in event_list:
        dp.add_handler(cqh(get_event, pass_user_data=True, pattern=event))
    dp.add_handler(cqh(events_keyboard, pass_user_data=True,
                       pattern='events_keyboard'))
    dp.add_handler(cqh(key_keyboard, pass_user_data=True,
                       pattern='key_keyboard'))

    dp.add_handler(cqh(exot_weapon, pass_user_data=True,
                       pattern='exot_weapon'))
    for weapon in exotic_guns:
        dp.add_handler(cqh(get_exotic_weapon,
                       pass_user_data=True, pattern=weapon))

    dp.add_handler(cqh(kinetic_exotic, pass_user_data=True,
                       pattern='kinetic_exotic'))
    dp.add_handler(cqh(energo_exotic, pass_user_data=True,
                       pattern='energo_exotic'))
    dp.add_handler(cqh(heavy_exotic, pass_user_data=True,
                       pattern='heavy_exotic'))

    dp.add_handler(cqh(exot_armor, pass_user_data=True,
                       pattern='exot_armor'))
    for armor in exotic_armor:
        dp.add_handler(cqh(get_exotic_armor,
                           pass_user_data=True, pattern=armor))

    dp.add_handler(CallbackQueryHandler(titan_exotic, pass_user_data=True, pattern = 'titan_exotic'))
    dp.add_handler(CallbackQueryHandler(warlock_exotic, pass_user_data=True, pattern = 'warlock_exotic'))
    dp.add_handler(CallbackQueryHandler(hunter_exotic, pass_user_data=True, pattern = 'hunter_exotic'))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()