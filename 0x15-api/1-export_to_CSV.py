#!/usr/bin/python3
"""
Checks student output for returning info from REST API and exports to CSV
"""

import requests
import sys
import csv

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def fetch_user_name(user_id):
    """ Fetch user name """
    resp = requests.get(users_url).json()
    name = None
    for i in resp:
        if i['id'] == user_id:
            name = i['name']
    return name


def export_to_csv(user_id, tasks):
    """ Export data to CSV """
    user_name = fetch_user_name(user_id)
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


def fetch_and_export(user_id):
    """ Fetch tasks and export to CSV """
    resp = requests.get(f'{todos_url}?userId={user_id}').json()
    export_to_csv(user_id, resp)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_and_export(employee_id)
