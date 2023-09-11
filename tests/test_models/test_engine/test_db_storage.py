#!/usr/bin/python3
"""
DBStorage Unittests
"""

from models import storage
import os
from models.base_model import BaseModel, Base
import unittest


class test_fileStorage(unittest.TestCase):
    """
    DBStorage Unittests
    """

    def test_all(self):
        """
        all
        """
        new = BaseModel()
        tmp = storage.all()
        self.assertIsInstance(tmp, dict)

    def test_save(self):
        """
        save
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_new(self):
        """
        new
        """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            tmp = obj
            self.assertTrue(tmp is obj)
