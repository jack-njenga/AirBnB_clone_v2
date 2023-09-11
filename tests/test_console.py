#!/usr/bin/python3
"""
Console unit tests
"""
from console import HBNBCommand
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """
    Console unit tests
    """
    obj_cls = ["Place", "Review", "Amenity",
               "City", "State", "BaseModel", "User",]

    def test_create(self):
        """
        test create feature
        """
        with patch("sys.stdout", new=StringIO()) as f:
            classes = self.obj_cls
            for className in classes:
                cmd_ = "create {}".format(className)
                self.assertFalse(HBNBCommand().onecmd(cmd_))

    def test_all(self):
        """
        all feature tests
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            HBNBCommand().onecmd("create User")
            self.assertFalse(HBNBCommand().onecmd('all'))
            self.assertNotEqual("[]", f.getvalue().strip)
