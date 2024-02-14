import requests
import sys
import csv

def fetch_and_export_to_csv(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0]['title'].split(" ")[0].title() # Extracting the employee name differently

        csv_filename = f'{employee_id}.csv'

        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for task in todos:
                task_title = task['title']
                completed_status = str(task['completed'])
                csv_writer.writerow([employee_id, employee_name, completed_status, task_title])

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_and_export_to_csv(employee_id)
