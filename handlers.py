


def greet_user(bot, update, user_data):
    text = '''
    Привет {}. Я бот-помощник по игре Destiny 2.
    У меня ты можешь узнать какие испытания актуальны на этой неделе, "где Ксур?", какая сейчас неделя проклятья и как пройти рейд.'''.format(update.message.chat.first_name)
    update.message.reply_text(text)