#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

engine_type = getenv("ST")

if engine_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    # print("\t\t--DB ENGINE--")
else:
    # print("\t\t--FILE ENGINE--")
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
