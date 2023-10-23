#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{sys.argv[1]}").json()
    # user_data = user.json()
    EMPLOYEE_NAME = user['name']
    todo = requests.get(f"{base_url}/todos?userId={sys.argv[1]}").json()
    # todo_data = todo_response.json()
    TOTAL_NUMBER_OF_TASKS = len(todo)
    NUMBER_OF_DONE_TASKS = sum(1 for task in todo if task['completed'])

    print("Employee {} is done with tasks ({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in todo:
        if task['completed']:
            print(f"\t {task['title']}")
