import requests
import sys

def fetch_todo_list(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [task['title'] for task in todos if task['completed']]
        total_tasks = len(todos)
        employee_name = todos[0]['title'].split(" ")[1]  # Extracting the employee name differently

        print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
        for task_title in completed_tasks:
            print(f'\t{task_title}')

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)
