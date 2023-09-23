#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        self.classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if cls:
            new_dict = {}
            if type(cls) == str:
                cls = eval(cls)
            for key, val in self.__objects.items():
                # print(type(val)), print(type(key)), print(type(cls))
                # print(f"==== {cls.__name__} ====")
                if key.split(".")[0] == cls.__name__:
                    # print("---OK---")
                    new_dict[key] = val
            return new_dict
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Loads storage dictionary from file
        """
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = self.classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects
        """
        if obj:
            # print(type(obj))
            key = obj.__class__.__name__ + "." + obj.id
            # print(list(self.__objects.keys()))
            if key in self.__objects.keys():
                del self.__objects[key]
                self.save()
            else:
                pass

    def dell(self):
        """
        deletes all objects
        """
        print("DELETING ALL OBJECTS")
        print("\t\tARE YOU SURE")
        if input("\t\t[YES/NO] ") in ["YES"]:
            self.__objects = {}
            self.save()

    def close(self):
        """
        Deserilizes the JSON file objects.
        """
        self.reload()
