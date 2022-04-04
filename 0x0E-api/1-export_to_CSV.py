#!/usr/bin/python3
""" Anoter API Call """
import csv
import requests
from sys import argv

def new_func(user, toDo, completedTask):
    for task in toDo:
        if task.get("completed") is True:
            completedTask.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completedTask), len(toDo)))
    for task in completedTask:
        print("\t {}".format(task))

if __name__ == "__main__":

    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    toDo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

    completedTask = []

    new_func(user, toDo, completedTask)

    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in toDo:
            writer.writerow([int(id), user.get("username"),
                            task.get("completed"), task.get("title")])
