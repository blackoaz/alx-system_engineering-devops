#!/usr/bin/python3
"""
Script for for fetching a given employee ID, returns information
about his/her TODO list progress and saving to JSON
"""
import json
import re
import requests
import sys


url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(url, id)).json()
            todos_res = requests.get('{}/todos'.format(url)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            with open("{}.json".format(id), 'w') as json_file:
                user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_name
                        },
                    todos
                    ))
                user_data = {
                        "{}".format(id): user_data
                        }
                json.dump(user_data, json_file)
