#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{sys.argv[1]}").json()
    EMPLOYEE_NAME = user['name']
    USERNAME = user['username']
    todo = requests.get(f"{base_url}/todos?userId={sys.argv[1]}").json()
    TOTAL_NUMBER_OF_TASKS = len(todo)
    NUMBER_OF_DONE_TASKS = sum(1 for task in todo if task['completed'])
    with open(sys.argv[1] + '.csv', 'w', newline='') as csvfile:
        for task in todo:
            input_variable = [sys.argv[1], USERNAME,
                              task.get('completed'), task.get('title')]
            my_writer = csv.writer(csvfile, delimiter=',',
                                   quoting=csv.QUOTE_ALL)
            my_writer.writerow(input_variable)
