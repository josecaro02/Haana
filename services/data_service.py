from models.user import Users
from models.reviews import Reviews
from models.stores import Stores


def create_account(name: str, email: str, passwd: str) -> Users:

    user = Users()
    user.name = name
    user.email = email
    user.passwd = passwd
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
