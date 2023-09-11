#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = "states"

    if getenv("ST") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete", lazy="dynamic")
    else:
        name = ""

        @property
        def cities(self):
            """
            cities getter
            """
            from models import storage

            cty_st = []
            for city in storage.all("City"):
                if city.state_id == self.id:
                    cty_st.append(city)
            return cty_st
