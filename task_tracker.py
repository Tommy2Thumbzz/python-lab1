import os
import json
from datetime import datetime

filename = "tasks.json"
tasks = []

# Load tasks from JSON file
if os.path.exists(filename):
    with open(filename, "r") as file:
        tasks = json.load(file)
def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            json.dump(tasks, file)

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark task(s) as done")
    print("5. Quit")

    choice = input("Enter your choice (1-5)")

    if choice == "1":
        new_tasks = input("Enter task(s) separated by commas: ")
        for task in new_tasks.split(","):
            cleaned = task.strip()
            if cleaned:
                tasks.append({"name": cleaned, "done": False})
        print(f"Added {len(new_tasks.split(','))} task(s).")
        save_tasks()

    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['name']} [{status}]")

            if all(task["done"] for task in tasks):
                print("🎉 All tasks are done! Great job!")
        else:
            print("No tasks yet. Add some!")

    elif choice == "3":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['name']} [{status}]")

            to_remove = input("Enter task number(s) to remove (comma-separated): ")
            indexes = sorted(
                [int(i.strip()) for i in to_remove.split(",") if i.strip().isdigit()],
                reverse=True
            )

            for idx in indexes:
                if 0 < idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    print(f"Removed: {removed['name']}")
                else:
                    print(f"Invalid task number: {idx}")

            save_tasks()
        else:
            print("No tasks to remove.")

    elif choice == "4":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['name']} [{status}]")

            done_input = input("Enter task number(s) to mark as done (comma-separated): ")
            indexes = [int(i.strip()) for i in done_input.split(",") if i.strip().isdigit()]

            for idx in indexes:
                if 0 < idx <= len(tasks):
                    tasks[idx - 1]["done"] = True
                    print(f"Marked: {tasks[idx - 1]['name']} ✅")
                else:
                    print(f"Invalid task number: {idx}")

            save_tasks()
        else:
            print("No tasks to mark.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")

    
        