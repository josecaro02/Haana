from models.user import Users
from models.reviews import Reviews
from models.stores import Stores
from models.product import Product
from models.locations import Locations
from models.web import Web


def create_account(name: str, email: str, passwd: str) -> Users:

    user = Users(name=name, email=email, passwd=passwd)
    user.save()
    return user


def find_account(email: str) -> Users:

    user = Users.objects(email=email).first()
    return user


def write_review(store_id: str, user_id: str,
                 description: str, score: str) -> Reviews:

    review = Reviews()
    review.store_id = store_id
    review.user_id = user_id
    review.description = description
    review.score = score
    review.save()
    return review


def show_reviews(store_id) -> Reviews:

    query = Reviews.objects(store_id=store_id)
    dic = []
    for i in query:
        temp = {}
        for k in i:
            if temp[k]:
                temp[k] = i[k]
        dic.append(temp)
    return dic


def create_location(department: str, city: str, address: str, pin: str) -> Locations:
    location = Locations()
    location.department = department
    location.city = city
    location.address = address
    location.pin = pin
    return location

def create_web_info(logo: str, color: str, background: str) -> Web:
    web = Web()
    web.logo = logo
    web.color = color
    web.background = background
    return web

def show_stores(type_store: str, location: str) -> Stores:

    query = Stores.objects(location__department=location)
    if query:
        dic = []
        for i in query:
            temp = {}
            for k in i:
                temp[k] = i[k]
            dic.append(temp)
        return dic

def create_product(name: str, value: str, description: str,
                   img_link: str) -> Product:
    product = Product()
    product.name = name
    product.value = value
    product.description = description
    product.img_link = img_link
    return product


def create_store(name: str, phone: str, type_: str,
                 subtype: str,
                 owner_id: str) -> Stores:
    store = Stores(name=name, phone=phone, type_=type_, sub_type=subtype, owner_id=owner_id)
    store.save()
    product = Product(name="MedBox", value="18000", description="medium box of luis", link="http://luiskfc")
    store.products.append(product)
    store.save()

    product = Product(name="MedBox_1", value="18000", description="medium box of luis", link="http://luiskfc")
    store.products.append(product)
    store.save()
    return store

def update_product():
    update = Stores.objects.get(pk = "5ed9c7df901ca46ea5562580")
    i = 0
    for prod in update.products:
        if (prod.name == "MedBox_1"):
            d = i
            update.products[d].name = "dos papitas"
            update.save()

        i += 1

def create_product():
    new_product = Stores.objects.get(pk = "5ed9c7df901ca46ea5562580")
    product = Product(name="LargeBox", value="20000", description="large box of luis", link="http://luiskfc")

    new_product.products.append(product)
    new_product.save()
