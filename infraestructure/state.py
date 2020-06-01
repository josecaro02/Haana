from typing import Optional
from models.user import Users
import services.data_service as svc

active_account: Optional[Users] = None


def reload_account():
    global active_account
    if not active_account:
        return
    active_account = svc.find_account(active_account.email)
