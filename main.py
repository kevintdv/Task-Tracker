from dataclasses import dataclass
from time import sleep

@dataclass
class Task:
    name: str
    description: str
    completed: bool=False

options = {
    "1": "Add task",
    "2": "Remove task",
    "3": "Display tasks",
    "4": "Mark as done",
    "5": "Exit"
}

def showTasks():
    for index, task in enumerate(tasks, start=1):
        print(f"Task: {index}")
        print(f"Name: {task.name}")
        print(f"Description: {task.description}")
        print(f"Completed: {task.completed}")
    

tasks = []

while True:
    print("TASK MANAGER")
    print()
    for key, value in options.items():
        print(f"{key}: {value}")
    option_choice = input("Select an option: ")

    if option_choice == "1":
        task_name = input("Enter name of task: ")
        task_description = input("Enter description of task: ")
        tasks.append(Task(task_name, task_description))
        print("Task added...")
    
    elif option_choice == "2":
        if not tasks:
            print("No tasks to remove.")
            continue
        showTasks()
        remove_choice = input("Enter the task number which you would like to remove (Q to exit): ").lower()
        if remove_choice.isdigit():
            remove_choice = int(remove_choice) - 1
            if remove_choice >= 0 and remove_choice < len(tasks):
                tasks.pop(remove_choice)
                print("Removing task...")
            else:
                print("Invalid task number")
        elif remove_choice == "q":
            print("Exiting...")
    
    elif option_choice == "3":
        if not tasks:
            print("No tasks to display")
        else:
            showTasks()
    elif option_choice == "4":
        showTasks()
        mark_choice = input("Enter the task number which you would like to mark as done (Q to exit): ").lower()
        if mark_choice.isdigit():
            mark_choice = int(mark_choice) - 1
            if mark_choice >= 0 and mark_choice < len(tasks):
                tasks[mark_choice].completed = True
                print("Marking task as completed...")
            else:
                print("Invalid task number")
    elif option_choice == "5":
        print("Exiting program...")
        break
    sleep(3)
