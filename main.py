#!/usr/bin/python3
"""
Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City
from models.user import User
states = list(storage.all(State).values())
users = list(storage.all("User").values())
id = "00a11245-12fa-436e-9ccc-967417f8c30a"
print(users[0])
users_dict = {}
for user in users:
    name = f"{user.first_name} {user.last_name}" 
    users_dict[user.id] = name
    # print(name, "=", user.id)

print("================================================")
print(users_dict["00a11245-12fa-436e-9ccc-967417f8c30a"])
