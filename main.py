#!/usr/bin/python3
"""
Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

states = list(storage.all(State).values())

for state in states:
    print(f"- {state.id} ------- {state.name}")


