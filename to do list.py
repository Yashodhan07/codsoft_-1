import os
import json

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

# Function to add a task
def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        del tasks[task_index - 1]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Display tasks\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
