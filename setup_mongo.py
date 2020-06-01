#!/usr/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["co_haana"]
store = db["stores"]
test_store = {
    "_id": "1A",
    "created_at": "2020-05-31 1:23:04",
    "name": "Sushijana",
    "phone": "3777777",
    "type": "restaurant",
    "is_active": "True",
    "sub_type": "sushi",
    "location": {
        "department": "Cundinamarca",
        "city": "Bogota",
        "address": "Cl. 78 #53-70",
        "pin": "info del pin"},
    "owner_id": "1",
    "products": {
        "CALIFORNIA ROLL":   {
            "value": "15900",
            "description": "Palmito de cangrejo, aguacate y queso crema. FOrrado con caviar.",
            "img_link": "https://en.wikipedia.org/wiki/California_roll#/media/File:California_Sushi_(26571101885).jpg"}
                },
    "web_info":   {
        "logo": "https://pbs.twimg.com/profile_images/378800000090536918/e9316ae987489291b3d9482e74872155_400x400.jpeg",
        "color": "FF5733",
        "background": "FF5736"}
}
store.insert_one(test_store)
user = db["users"]
test_user = {
    "_id": "1",
    "name": "Jose Caro",
    "type": "Owner",
    "email": "1278@holbertonschool.com",
    "passwd": "leidy_perez",
    "phone": "3203443504"
}
user.insert_one(test_user)
review = db["reviews"]
test_review = {
    "_id": "2B",
    "store_id": "1A",
    "user_id": "1",
    "description":"Excelente servicio comida fresca aunque un poco lenta la preparacion pero eso asegura la frescura del producto",
    "score": "4.6"
}
review.insert_one(test_review)
