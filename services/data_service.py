from models.user import Users


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
