tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def delete_task(task_index):
    if task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index!")

# Function to display all tasks
def display_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
    else:
        print("No tasks found.")

# Main function
def main():
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: ")) - 1
            delete_task(task_index)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
