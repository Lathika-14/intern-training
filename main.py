from contact import add_contact, find_contact, list_contacts
from todolist import add_task, remove_task, show_tasks
while True:
    print("\nMAIN MENU")
    print("1. Contact Book")
    print("2. To-Do List")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        while True:
            print("\nCONTACT BOOK")
            print("1. Add Contact")
            print("2. Find Contact")
            print("3. List Contacts")
            print("4. Back to Main Menu")

            c = input("Enter choice: ")

            if c == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                add_contact(name, phone)

            elif c == "2":
                name = input("Enter name to search: ")
                find_contact(name)

            elif c == "3":
                list_contacts()

            elif c == "4":
                break

            else:
                print("Invalid choice")

    elif choice == "2":
        while True:
            print("\nTO-DO LIST")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Show Tasks")
            print("4. Back to Main Menu")

            t = input("Enter choice: ")

            if t == "1":
                task = input("Enter task: ")
                add_task(task)

            elif t == "2":
                task = input("Enter task to remove: ")
                remove_task(task)

            elif t == "3":
                show_tasks()

            elif t == "4":
                break

            else:
                print("Invalid choice")

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice")