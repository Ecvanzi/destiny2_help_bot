from pymongo import MongoClient
import settings


db = MongoClient(settings.MONGO_LINK)[settings.MONGO_DB]


def save_xur_place(db, Xur_place):
    db.xur_tab.update({}, {"$set": {"xur_place": Xur_place}}, False, True)

def save_xur_img(db, Xur_image_url):
    db.xur_tab.update({}, {"$set": {"xur_image_url": Xur_image_url}}, False, True)


def save_xur_weapon(db, xur_first_weapon, xur_second_weapon, xur_third_weapon, xur_fourth_weapon):
    db.xur_tab.update({},
    {"$set": {
        "xur_first_weapon": xur_first_weapon ,  
        "xur_second_weapon": xur_second_weapon , 
        "xur_third_weapon": xur_third_weapon , 
        "xur_fourth_weapon": xur_fourth_weapon 

}},False, True)
