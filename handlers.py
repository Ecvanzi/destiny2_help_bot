


def greet_user(bot, update, user_data):
    text = 'Привет {}'.format(update.message.chat.first_name)
    update.message.reply_text(text)