#!/usr/bin/python3
"""
New db engine
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

user = getenv("HBNB_MYSQL_USER")
pwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
env = getenv("HBNB_ENV")

obj_classes = {
        "City": City,
        "State": State,
        "User": User,
        "Place": Place
        }


class DBStorage():
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        init
        """
        url = "mysql+mysqlconnector://root:root\
                @localhost:3306/hbnb_dev_db"
        url2 = "mysql+mysqlconnector://hbnb_dev:\
                hbnb_dev_pwd@localhost:3306/hbnb_dev_db"
        url3 = f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}"
        self.__engine = create_engine(url3, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Querys on the database session
        """
        all_obj = {}
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
                objs = self.__session.query(cls)
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_obj[key] = obj
        else:
            for obj in obj_classes.values():
                objects = self.__session.query(obj).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_obj[key] = obj
        return all_obj

    def new(self, obj):
        """
        Adds the object given to the current database
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj(if present from the database)
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Recreates all tables in the database
        """
        # print("===> Reloading")
        # print("===>", Base.metadata)
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """
        Closses the current session
        """
        self.reload()
        self.__session.close()
