#!/usr/bin/python3
"""
Script for for fetching a given employee ID, returns information
about his/her TODO list progress and saving the date in a csv file
"""
import re
import requests
import sys


url = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(url, id)).json()
            todos_res = requests.get('{}/todos'.format(url)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                            '"{}","{}","{}","{}"\n'.format(
                                id,
                                user_name,
                                todo.get('completed'),
                                todo.get('title')
                                )
                            )
