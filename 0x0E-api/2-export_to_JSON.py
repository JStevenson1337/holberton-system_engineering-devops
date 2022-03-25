#!/usr/bin/python3
"""Uses a REST API to retrieve information"""
import json
from os import sys
import requests

def new_func():
    try:
        user_id = sys.argv[1]
        id = int(user_id)

    except ValueError:
        print("ID not INT")

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    name = user.json()["name"]
    username = user.json()["username"]
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    file = user_id + ".json"
    return id,username,todos,file

if __name__ == "__main__":
    id, username, todos, file = new_func()

    with open(file, 'w') as f:
        Dict = {}
        Dict[id] = []
        for k in todos.json():
            if k['userId'] == id:
                dictionary = {"task": k['title'],
                              "completed": k['completed'],
                              "username": username}
                Dict[id].append(dictionary)
        json.dump(Dict, f)
