#!/usr/bin/python3
import pymongo
import os

host_db = os.getenv("HAANA_HOST_DB", "localhost")
port_db = os.getenv("HAANA_PORT_DB", "27017")
name_db = os.getenv("HAANA_DB_NAME", "co_haana")

myclient = pymongo.MongoClient(f"mongodb://{host_db}:{port_db}/")
mongo_db = myclient[name_db]
