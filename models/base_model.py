#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

fmt = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        init
        """
        now = datetime.now()
        self.id = str(uuid4())
        self.created_at = now
        self.updated_at = now

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    try:
                        self.__dict__[key] = datetime.strptime(kwargs, fmt)
                    except Exception as e:
                        pass
                if key not in ["__class__"]:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        try:
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
        except Exception as e:
            pass
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        """
        Deletes the current BaseModel instance
        """
        from models import storage
        storage.delete(self)
