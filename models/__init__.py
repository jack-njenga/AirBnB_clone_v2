#!/usr/bin/python3
"""
This module instantiates an object of either
class FileStorage or DBStorage
"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv

engine_type = getenv("HBNB_TYPE_STORAGE")

if engine_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    # print("\t\t--DB ENGINE--")
else:
    # print("\t\t--FILE ENGINE--")
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

__all__ = ["User", "Place", "State", "City", "Amenity", "Review", "storage"]
