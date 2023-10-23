#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()

    all_employees_data = {}
    for user in users:
        user_id = user.get('id')
        todo = requests.get(f"{base_url}/todos?userId={user_id}").json()
        all_employees_data[user_id] = []
        for task in todo:
            all_employees_data[user_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
                })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_employees_data, file)
