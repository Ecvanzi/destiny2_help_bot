from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def exotic_keyboard(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Оружие', callback_data='exot_weapon_keyboard'),
        InlineKeyboardButton('Броня', callback_data='exot_armor_keyboard')
        ],
        [InlineKeyboardButton('Главное меню', callback_data='key_keyboard')]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, message_id= query.message.message_id, text ='Выбирай раздел:', reply_markup = reply_markup)
 

def exot_weapon(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Кинетическое оружие', callback_data='kinetic_exotic'),
        InlineKeyboardButton('Энергитическое оружие', callback_data='energo_exotic'),
        InlineKeyboardButton('Силовое оружие', callback_data='heavy_exotic')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай тип оружия или иди обратно:', reply_markup = reply_markup)

def exot_armor(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Экзоты титанов', callback_data='titan_exotic'),
        InlineKeyboardButton('Экзоты варлоков', callback_data='warlock_exotic'),
        InlineKeyboardButton('Экзоты охотников', callback_data='hunter_exotic')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай класс или иди обратно:', reply_markup = reply_markup)

def e_weapon_menu(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Назад', callback_data='exot_weapon'),
        InlineKeyboardButton('К выбору раздела', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Куда дальше?', reply_markup = reply_markup)

def e_armor_menu(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Назад', callback_data='exot_armor'),
        InlineKeyboardButton('К выбору раздела', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Куда дальше?', reply_markup = reply_markup)


def kinetic_exotic(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Милое дело', callback_data='sweet_business'),
        InlineKeyboardButton('Буря', callback_data='sturm')
        ],
        [
        InlineKeyboardButton('Крыло бдительности', callback_data='vigilance_wing'),
        InlineKeyboardButton('Крысиный король', callback_data='rat_king')
        ],
        [
        InlineKeyboardButton('Универсальный инструмент MIDA', callback_data='mida_multi_tool'),
        InlineKeyboardButton('Багрец', callback_data='crimson')
        ],
        [
        InlineKeyboardButton('Нефритовый кролик', callback_data='jade_rabbit'),
        InlineKeyboardButton('Гекельбери', callback_data='huckleberry')
        ],
        [
        InlineKeyboardButton('Режим SUROS', callback_data='suros'),
        InlineKeyboardButton('Цербер+1', callback_data='cerberus')
        ],
        [
        InlineKeyboardButton('Губитель желаний', callback_data='wish_ender'),
        InlineKeyboardButton('Злоумышленник', callback_data='malfeasance')
        ],
        [
        InlineKeyboardButton('Пиковый туз', callback_data='ace_of_spades'),
        InlineKeyboardButton('Компаньон', callback_data='chaperone')
        ],
        [
        InlineKeyboardButton('Бремя Идзанаги', callback_data='izanagis_burden'),
        InlineKeyboardButton('Последнее слово', callback_data='last_word')
        ],
        [
        InlineKeyboardButton('Арбалет', callback_data='arbalest'),
        InlineKeyboardButton('Шип', callback_data='thorn')
        ],
        [
        InlineKeyboardButton('Идеальная эпидемия', callback_data='outbreak_perfected'),
        InlineKeyboardButton('Злые силы', callback_data='bad_juju')
        ],
        [
        InlineKeyboardButton('Люмина', callback_data='lumina'),
        InlineKeyboardButton('Монте-Карло', callback_data='monte_carlo')
        ],
        [
        InlineKeyboardButton('Бастион', callback_data='bastion')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай:', reply_markup = reply_markup)

def energo_exotic(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Холодное сердце', callback_data='coldheart'),
        InlineKeyboardButton('Бойцовский лев', callback_data='fighting_lion')
        ],
        [
        InlineKeyboardButton('Солнечный выстрел', callback_data='sunshot'),
        InlineKeyboardButton('Гравитонове копье', callback_data='graviton_lance')
        ],
        [
        InlineKeyboardButton('Жесткий свет', callback_data='hard_light'),
        InlineKeyboardButton('Клятва небожога', callback_data='skyburners_oath')
        ],
        [
        InlineKeyboardButton('Анализатор рисков', callback_data='riskrunner'),
        InlineKeyboardButton('Безжалостный', callback_data='merciless')
        ],
        [
        InlineKeyboardButton('Северное сияние', callback_data='borealis'),
        InlineKeyboardButton('Линза Прометея', callback_data='prometheus_lens')
        ],
        [
        InlineKeyboardButton('Телесто', callback_data='telesto'),
        InlineKeyboardButton('Полярное копье', callback_data='polaris_lance')
        ],
        [
        InlineKeyboardButton('тройственный гуль', callback_data='trinity_ghoul'),
        InlineKeyboardButton('Волнолом', callback_data='wavesplitter')
        ],
        [
        InlineKeyboardButton('Повелитель волков', callback_data='lord_of_wolves'),
        InlineKeyboardButton('Йотун', callback_data='jotunn')
        ],
        [
        InlineKeyboardButton('Le Monarque', callback_data='le_monarque'),
        InlineKeyboardButton('Тарраба', callback_data='tarrabah')
        ],
        [
        InlineKeyboardButton('Клятва Эрианы', callback_data='erianas_vow'),
        InlineKeyboardButton('Божественность', callback_data='divinity')
        ],
        [
        InlineKeyboardButton('Симметрия', callback_data='symmetry'),
        InlineKeyboardButton('Руины дьявола', callback_data='devils_ruin')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай:', reply_markup = reply_markup)

def heavy_exotic(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Старатель', callback_data='prospector'),
        InlineKeyboardButton('Буксировочная пушка', callback_data='tractor_cannon')
        ],
        [
        InlineKeyboardButton('Легенда об Акрии', callback_data='legend_of_acrius'),
        InlineKeyboardButton('Д.А.Р.С.И.', callback_data='darci')
        ],
        [
        InlineKeyboardButton('Уорклиффская катушка', callback_data='wardcliff_coil'),
        InlineKeyboardButton('Колония', callback_data='colony')
        ],
        [
        InlineKeyboardButton('Нулевая мировая линия', callback_data='worldline_zero'),
        InlineKeyboardButton('Усыпляющий симулянт', callback_data='sleeper_simulant')
        ],
        [
        InlineKeyboardButton('Шепот червя', callback_data='whisper_of_the_worm'),
        InlineKeyboardButton('Тысяча голосов', callback_data='one_thousand_voices')
        ],
        [
        InlineKeyboardButton('Двухвостый лис', callback_data='two_tailed_fox'),
        InlineKeyboardButton('Черный коготь', callback_data='black_talon')
        ],
        [
        InlineKeyboardButton('Губитель королев', callback_data='queenbreaker'),
        InlineKeyboardButton('Владыка грома', callback_data='thunderlord')
        ],
        [
        InlineKeyboardButton('Анархия', callback_data='anarchy'),
        InlineKeyboardButton('Истина', callback_data='truth')
        ],
        [
        InlineKeyboardButton('Приносящая смерть', callback_data='deathbringer'),
        InlineKeyboardButton('Ксенофаг', callback_data='xenophage')
        ],
        [
        InlineKeyboardButton('Дыхание Левиафана', callback_data='leviathans_breath'),
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай:', reply_markup = reply_markup)

def titan_exotic(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Неприступная черепокрепость', callback_data='insurmountable_skullfort'),
        InlineKeyboardButton('Маска Тихого', callback_data='mask_of_the_quiet_one')
        ],
        [
        InlineKeyboardButton('Рог Хепри', callback_data='khepris_horn'),
        InlineKeyboardButton('Шлем Сэйнта-14', callback_data='helm_of_saint14')
        ],
        [
        InlineKeyboardButton('Вечный воин', callback_data='eternal_warrior'),
        InlineKeyboardButton('Одноглазая маска', callback_data='one_eyed_mask')
        ],
        [
        InlineKeyboardButton('Реактивный барьер АК3/0', callback_data='feedback_fence'),
        InlineKeyboardButton('Наплечники с клыками погибели', callback_data='doom_fang_pauldron')
        ],
        [
        InlineKeyboardButton('Синтоцепсы', callback_data='synthoceps'),
        InlineKeyboardButton('Надежная вечность', callback_data='aeon_safe')
        ],
        [
        InlineKeyboardButton('Пепельный обряд', callback_data='ashen_wake'),
        InlineKeyboardButton('Милость Червебога', callback_data='wormgod_caress')
        ],
        [
        InlineKeyboardButton('Урас Фьюриоса', callback_data='ursa_furiosa'),
        InlineKeyboardButton('Цитадель', callback_data='stronghold')
        ],
        [
        InlineKeyboardButton('Герб Альфа Волка', callback_data='crest_of_alpha_lupi'),
        InlineKeyboardButton('Боевая установка "Акций"', callback_data='actium_war_rig')
        ],
        [
        InlineKeyboardButton('Сердце священного пламени', callback_data='hallowfire_heart'),
        InlineKeyboardButton('Инструментарий', callback_data='armamentarium')
        ],
        [
        InlineKeyboardButton('Сердце внутреннего Света', callback_data='heart_of_inmost_light'),
        InlineKeyboardButton('Выходное пособие', callback_data='severance_enclosure')
        ],
        [
        InlineKeyboardButton('Бешенный лев', callback_data='lion_rampant'),
        InlineKeyboardButton('Миротворцы', callback_data='peacekeepers')
        ],
        [
        InlineKeyboardButton('Идущие по дюнам', callback_data='dunemarchers'),
        InlineKeyboardButton('Уклонение mk.44', callback_data='mk44_stand_asides')
        ],
        [
        InlineKeyboardButton('Знаки Антея', callback_data='antaeus_wards'),
        InlineKeyboardButton('Поножи Перегрин', callback_data='peregrine_greaves')
        ],[
        InlineKeyboardButton('Колыбель Феникса', callback_data='phoenix_cradle')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай:', reply_markup = reply_markup)

def warlock_exotic(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Череп лютой Ахамкары', callback_data='skull_of_dire_ahamkara'),
        InlineKeyboardButton('Корона Бурь', callback_data='crown_of_tempests')
        ],
        [
        InlineKeyboardButton('Око другого мира', callback_data='eye_of_another_world'),
        InlineKeyboardButton('Грех Незарека', callback_data='nezarecs_sin')
        ],
        [
        InlineKeyboardButton('Олень', callback_data='stag'),
        InlineKeyboardButton('Лик правды', callback_data='veritys_brow')
        ],
        [
        InlineKeyboardButton('Обожествляющая вуаль', callback_data='apotheosis_veil'),
        InlineKeyboardButton('Астроцитная вселенная', callback_data='astrocyte_verse')
        ],
        [
        InlineKeyboardButton('Нарукавники Солнца', callback_data='sunbracers'),
        InlineKeyboardButton('Браслеты Карнштейна', callback_data='karnstein_armlets')
        ],
        [
        InlineKeyboardButton('Вероломство зимы', callback_data='winters_guile'),
        InlineKeyboardButton('Деша вечности', callback_data='aeon_soul')
        ],
        [
        InlineKeyboardButton('Змеевидный аспект', callback_data='ophidian_aspect'),
        InlineKeyboardButton('Когти Ахамкары', callback_data='claws_of_ahamkara')
        ],
        [
        InlineKeyboardButton('Дух противоречия', callback_data='contraverse_hold'),
        InlineKeyboardButton('Специалист по побегам', callback_data='getaway_artist')
        ],
        [
        InlineKeyboardButton('Протокл "Звездный огонь"', callback_data='starfire_protocol'),
        InlineKeyboardButton('Крылья Священного Рассвета', callback_data='wings_of_sacred_dawn')
        ],
        [
        InlineKeyboardButton('Вечерняя звезда', callback_data='vesper_of_radius'),
        InlineKeyboardButton('Кровавая алхимия', callback_data='sanguine_alchemy')
        ],
        [
        InlineKeyboardButton('Хроматический огонь', callback_data='chromatic_fire'),
        InlineKeyboardButton('Протокол "Феникс', callback_data='phoenix_protocol')
        ],
        [
        InlineKeyboardButton('Скобы Заклинателя бури', callback_data='stormdancers_brace'),
        InlineKeyboardButton('Поперечные шаги', callback_data='transversive_steps')
        ],
        [
        InlineKeyboardButton('Сапоги лунофракиции', callback_data='lunafaction_boots'),
        InlineKeyboardButton('Геомагнитные стабилизаторы', callback_data='geomag_stabilizers')
        ],[
        InlineKeyboardButton('Прометиевая шпора', callback_data='promethium_spur')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай:', reply_markup = reply_markup)

def hunter_exotic(update, context):
    query = update.callback_query
    keyboard = [
        [
        InlineKeyboardButton('Радар тупиц', callback_data='knucklehead_radar'),
        InlineKeyboardButton('Звездный полуночник', callback_data='celestial_nighthawk')
        ],
        [
        InlineKeyboardButton('Врагоискатель', callback_data='foetracer'),
        InlineKeyboardButton('Потеря гравитонов', callback_data='graviton_forfeit')
        ],
        [
        InlineKeyboardButton('Корона червеоболочки', callback_data='wormhusk_crown'),
        InlineKeyboardButton('Капюшон киллера', callback_data='assassins_cowl')
        ],
        [
        InlineKeyboardButton('Хребет молодой Ахамкары', callback_data='young_ahamkaras_spine'),
        InlineKeyboardButton('Хитрые рукава Механиста', callback_data='mechaneers_tricksleeves')
        ],
        [
        InlineKeyboardButton('Скоротечная вечность', callback_data='aeon_swift'),
        InlineKeyboardButton('Клятва Синобу', callback_data='shinobus_vow')
        ],
        [
        InlineKeyboardButton('Перчатки обшитой Ахамкары', callback_data='sealed_ahamkara_grasps'),
        InlineKeyboardButton('Осколки Галанора', callback_data='shards_of_galanor')
        ],
        [
        InlineKeyboardButton('Хранитель клятвы', callback_data='oathkeeper'),
        InlineKeyboardButton('Рукопожатие лжеца', callback_data='liars_handshake')
        ],
        [
        InlineKeyboardButton('Жало Хепри', callback_data='khepris_sting'),
        InlineKeyboardButton('Поток Рэйдена', callback_data='raiden_flux')
        ],
        [
        InlineKeyboardButton('Везучая ежевика', callback_data='lucky_raspberry'),
        InlineKeyboardButton('Тень дракона', callback_data='dragons_shadow')
        ],
        [
        InlineKeyboardButton('Змеиная шкура', callback_data='ophidia_spathe'),
        InlineKeyboardButton('Жилет гвисина', callback_data='gwisin_vest')
        ],
        [
        InlineKeyboardButton('Шестой койот', callback_data='sixth_coyote'),
        InlineKeyboardButton('Везучие штаны', callback_data='lucky_pants')
        ],
        [
        InlineKeyboardButton('Установка "Орфей"', callback_data='orpheus_rig'),
        InlineKeyboardButton('Т0п0туны', callback_data='stomp_ee5')
        ],
        [
        InlineKeyboardButton('Шут под знаком близнецов', callback_data='gemini_jester'),
        InlineKeyboardButton('М0р03ники', callback_data='frost_ee5')
        ],[
        InlineKeyboardButton('Бомбардиры', callback_data='bombardiers')
        ],
        [
        InlineKeyboardButton('Назад', callback_data='exotic_keyboard'),
        InlineKeyboardButton('Главное меню', callback_data='key_keyboard')
        ]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=query.message.chat.id, text = 'Выбирай:', reply_markup = reply_markup)