import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,  CallbackQueryHandler, ConversationHandler
from handlers import greet_user, main_keyboard, key_keyboard, xur_keyboard
from xur import xur_here, all_xur, where_xur, xur_keyboard
from events import get_event
from events_keyboards import events_keyboard
from armory import types_of_weapons_list
from armory_keyboard import armory_keyboard, weapon_keyboard, light_ammo, special_ammo, heavy_ammo
from exotic import get_exotic_armor, get_exotic_weapon
from exotic_keyboard import warlock_exotic, titan_exotic, heavy_exotic, hunter_exotic, kinetic_exotic, energo_exotic, exotic_keyboard, exot_armor, exot_weapon

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
    dp.add_handler(MessageHandler(Filters.regex('({})'.format(types_of_weapons_list)), greet_user, pass_user_data= True))
    dp.add_handler(CallbackQueryHandler(xur_keyboard, pass_user_data=True, pattern = 'xur'))
    dp.add_handler(CallbackQueryHandler(all_xur, pass_user_data=True, pattern = 'all_xur'))
    dp.add_handler(CallbackQueryHandler(xur_here, pass_user_data=True, pattern = 'xur_here'))
    dp.add_handler(CallbackQueryHandler(exotic_keyboard, pass_user_data=True, pattern = 'exotic'))
    #dp.add_handler(CallbackQueryHandler(, pass_user_data=True, pattern = 'raids'))
    dp.add_handler(CallbackQueryHandler(armory_keyboard, pass_user_data=True, pattern = 'armory'))
    dp.add_handler(CallbackQueryHandler(events_keyboard, pass_user_data=True, pattern = 'events'))
    #dp.add_handler(CallbackQueryHandler(, pass_user_data=True, pattern = 'other'))
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
    dp.add_handler(CallbackQueryHandler(events_keyboard, pass_user_data=True, pattern = 'events_keyboard'))
    dp.add_handler(CallbackQueryHandler(key_keyboard, pass_user_data=True, pattern = 'key_keyboard'))
    
    dp.add_handler(CallbackQueryHandler(exot_weapon, pass_user_data= True, pattern = 'exot_weapon'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'sweet_business'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'sturm'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'vigilance_wing'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'rat_king'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'mida_multi_tool'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'crimson'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'jade_rabbit'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'huckleberry'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'suros'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'cerberus'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'wish_ender'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'malfeasance'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'ace_of_spades'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'chaperone'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'izanagis_burden'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'last_word'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'arbalest'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'thorn'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'outbreak_perfected'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'bad_juju'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'lumina'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'monte_carlo'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'bastion'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'coldheart'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'fighting_lion'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'sunshot'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'graviton_lance'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'hard_light'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'skyburners_oath'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'riskrunner'))    
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'merciless'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'borealis'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'prometheus_lens'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'telesto'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'polaris_lance'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'trinity_ghoul'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'wavesplitter'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'lord_of_wolves'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'jotunn'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'le_monarque'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'tarrabah'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'erianas_vow'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'divinity'))    
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'symmetry'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'devils_ruin'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'prospector'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'tractor_cannon'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'legend_of_acrius'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'darci'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'wardcliff_coil'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'colony'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'worldline_zero'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'sleeper_simulant'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'whisper_of_the_worm'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'one_thousand_voices'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'two_tailed_fox'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'black_talon'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'queenbreaker'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'thunderlord'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'anarchy'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'truth'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'deathbringer'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'xenophage'))
    dp.add_handler(CallbackQueryHandler(get_exotic_weapon, pass_user_data=True, pattern = 'leviathans_breath'))
    dp.add_handler(CallbackQueryHandler(kinetic_exotic, pass_user_data=True, pattern = 'kinetic_exotic'))
    dp.add_handler(CallbackQueryHandler(energo_exotic, pass_user_data=True, pattern = 'energo_exotic'))
    dp.add_handler(CallbackQueryHandler(heavy_exotic, pass_user_data=True, pattern = 'heavy_exotic'))

    dp.add_handler(CallbackQueryHandler(exot_armor, pass_user_data= True, pattern = 'exot_armor'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'insurmountable_skullfort'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'mask_of_the_quiet_one'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'khepris_horn'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'helm_of_saint14'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'eternal_warrior'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'one_eyed_mask'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'feedback_fence'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'doom_fang_pauldron'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'synthoceps'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'aeon_safe'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'ashen_wake'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'wormgod_caress'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'ursa_furiosa'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'stronghold'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'crest_of_alpha_lupi'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'actium_war_rig'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'hallowfire_heart'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'armamentarium'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'heart_of_inmost_light'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'severance_enclosure'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'lion_rampant'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'peacekeepers'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'dunemarchers'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'mk44_stand_asides'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'antaeus_wards'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'peregrine_greaves'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'phoenix_cradle'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'knucklehead_radar'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'celestial_nighthawk'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'foetracer'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'graviton_forfeit'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'wormhusk_crown'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'assassins_cowl'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'young_ahamkaras_spine'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'mechaneers_tricksleeves'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'aeon_swift'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'shinobus_vow'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'sealed_ahamkara_grasps'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'shards_of_galanor'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'oathkeeper'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'liars_handshake'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'khepris_sting'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'raiden_flux'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'lucky_raspberry'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'dragons_shadow'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'ophidia_spathe'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'gwisin_vest'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'sixth_coyote'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'lucky_pants'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'orpheus_rig'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'stomp_ee5'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'gemini_jester'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'frost_ee5'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'bombardiers'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'skull_of_dire_ahamkara'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'crown_of_tempests'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'eye_of_another_world'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'nezarecs_sin'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'stag'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'veritys_brow'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'apotheosis_veil'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'astrocyte_verse'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'sunbracers'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'karnstein_armlets'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'winters_guile'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'aeon_soul'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'ophidian_aspect'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'claws_of_ahamkara'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'contraverse_hold'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'getaway_artist'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'starfire_protocol'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'wings_of_sacred_dawn'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'vesper_of_radius'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'sanguine_alchemy'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'chromatic_fire'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'phoenix_protocol'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'stormdancers_brace'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'transversive_steps'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'lunafaction_boots'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'geomag_stabilizers'))
    dp.add_handler(CallbackQueryHandler(get_exotic_armor, pass_user_data=True, pattern = 'promethium_spur'))
    dp.add_handler(CallbackQueryHandler(titan_exotic, pass_user_data=True, pattern = 'titan_exotic'))
    dp.add_handler(CallbackQueryHandler(warlock_exotic, pass_user_data=True, pattern = 'warlock_exotic'))
    dp.add_handler(CallbackQueryHandler(hunter_exotic, pass_user_data=True, pattern = 'hunter_exotic'))


    mybot.start_polling()
    mybot.idle()


if __name__=="__main__":
    main()