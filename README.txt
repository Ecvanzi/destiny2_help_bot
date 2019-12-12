Destiny2_help_bot
=================

Destiny2_help_bot - это телеграм бот созданный для помощи игрокам в Destiny2. 

Установка
==========

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:
Install and update using `pip`_:

.. code-block:: text
    pip install -r requirements.txt

После этого положите картинки с котиками в папку image. У всех картинок в названии должно быть cat и расширение jpg или jpeg.

Настройка
==========

Создайте файл settings.py и добавьте в него следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
        'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = "API_key полученный у BotFather"


Запуск
=======
В виртуальном окружении выполните:

.. code-block:: text

    python destiny2_bot.py