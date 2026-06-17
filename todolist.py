print("2..TO DO LIST")
tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed")
    else:
        print("Task not found")
def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        i = 0
        while i < len(tasks):
            print(i + 1, ".", tasks[i])
            i += 1
while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Exiting To-Do List...")
        break
    else:
        print("Invalid choice")
