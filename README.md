Destiny2_help_bot
================

Destiny2_help_bot - это телеграм бот созданный для помощи игрокам в Destiny2. 

Установка
==========

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:


    pip install -r requirements.txt



Настройка
==========

Создайте файл settings.py и добавьте в него следующие настройки:

    import os
   
    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
        'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = "API_key полученный у BotFather"


Запуск
=======
В виртуальном окружении выполните:



    python destiny2_bot.py
