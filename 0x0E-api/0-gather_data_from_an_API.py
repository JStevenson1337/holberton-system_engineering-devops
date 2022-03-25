#!/usr/bin/python3
""" Call an API """
from os import sys
import requests


if __name__ == "__main__":
    user_id = sys.argv[1]
    id = int(user_id)
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    name = user.json().get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    tasks = []
    for task in todos.json():
        if task.get("userId") == id:
            tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                            len(tasks), len(todos.json())))

    for task in tasks:
        print("\t{}. {}".format(task.get("completed"), task.get("title")))

