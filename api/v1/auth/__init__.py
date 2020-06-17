#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

from api.v1.auth.access import *
