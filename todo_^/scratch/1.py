tasks = []

with open("tasks.txt", 'w+') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue # skip empty lines
        status, task = line.split(":", 1) # split into 2 parts only
        tasks.append({
            "task": task.strip(),
            "status": bool(status.strip())
        })
    f.close()

def task_write():
    with open("tasks.txt", 'w+') as f:
        for t in tasks:
            status = tasks["status"]
            task = tasks["task"]
            f.write(f"{int(status)}: {task}\n")
        f.close()
def display_menu():
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Edit")
    print("3. Show Tasks")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def display_tasks():
    for index, taskANDstatus in enumerate(tasks):tasks = []

def display_menu():
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Edit")
    print("3. Show Tasks")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def display_tasks():
    for index, taskANDstatus in enumerate(tasks):
        task = tasks[taskANDstatus]["task"]
        status = "Done" if tasks[taskANDstatus]["status"] else "Not Done"
        print(f"{index + 1}. {task} - {status}")

def main():

    while True:
        # Display the menu options
        display_menu()
        
        # Get the user's choice
        choice = input("Enter your choice: ")

        # Option 1: Aff Task
        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "status": False})
                print("Task added!")
        
        # Option 2: Edit Task
        elif choice == '2':
            # Check if there are tasks available to edit
            if tasks:
                display_tasks()
                # Prompt the user to enter the index of the task to edit
                try:
                    task_index = int(input("Enter task index to edit: ")) - 1
                    # Check if the entered index is valid
                    if 0 <= task_index < len(tasks):
                        # Prompt the user to enter a new task
                        new_task = input("Enter new task: ")
                        # Update the task at the specified index
                        tasks[task_index]["task"] = new_task
                        print("Task edited successfully.")
                    else:
                        print("Invalis index.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No Tasks available to edit.")

        
        # Option 3: Show Tasks
        elif choice == '3':
            print("\nTasks:")
            display_tasks()
        
        # Option 4: Mark Tasks
        elif choice == '4':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["status"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        
        # Option 5: Delete Task
        elif choice == '5':
            # Check if there are tasks avialable to delete
            if tasks:
                # Display the current tasks with their indices
                display_tasks()
                # Prompt the user to enter the index of the task to delete
                try:
                    task_index = int(input("Enter task index to delete: ")) -1
                    # Check if the entered index is valid
                    if 0 <= task_index < len(tasks):
                        # Remove the task at the specidied index
                        tasks.pop(task_index)
                        print("Task deleted successfully.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No task avilable to delete.")


        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        task = tasks[taskANDstatus]["task"]
        status = "Done" if tasks[taskANDstatus]["status"] else "Not Done"
        print(f"{index + 1}. {task} - {status}")

def main():

    while True:
        # Display the menu options
        display_menu()
        
        # Get the user's choice
        choice = input("Enter your choice: ")

        # Option 1: Aff Task
        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "status": False})
                print("Task added!")
        
        # Option 2: Edit Task
        elif choice == '2':
            # Check if there are tasks available to edit
            if tasks:
                display_tasks()
                # Prompt the user to enter the index of the task to edit
                try:
                    task_index = int(input("Enter task index to edit: ")) - 1
                    # Check if the entered index is valid
                    if 0 <= task_index < len(tasks):
                        # Prompt the user to enter a new task
                        new_task = input("Enter new task: ")
                        # Update the task at the specified index
                        tasks[task_index]["task"] = new_task
                        print("Task edited successfully.")
                    else:
                        print("Invalis index.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No Tasks available to edit.")

        
        # Option 3: Show Tasks
        elif choice == '3':
            print("\nTasks:")
            display_tasks()
        
        # Option 4: Mark Tasks
        elif choice == '4':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["status"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        
        # Option 5: Delete Task
        elif choice == '5':
            # Check if there are tasks avialable to delete
            if tasks:
                # Display the current tasks with their indices
                display_tasks()
                # Prompt the user to enter the index of the task to delete
                try:
                    task_index = int(input("Enter task index to delete: ")) -1
                    # Check if the entered index is valid
                    if 0 <= task_index < len(tasks):
                        # Remove the task at the specidied index
                        tasks.pop(task_index)
                        print("Task deleted successfully.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No task avilable to delete.")


        elif choice == '6':
            print("Exiting the To-Do List.")
            tasks_write()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()