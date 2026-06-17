print("1. CONTACT")
contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added successfully")
def find_contact(name):
    try:
        print(name, ":", contacts[name])
    except KeyError:
        print("Contact not found")
def list_contacts():
    if len(contacts) == 0:
        print("No contacts available")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)
while True:
        print("\n1. Add Contact")
        print("2. Find Contact")
        print("3. List Contacts")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name to search: ")
            find_contact(name)
        elif choice == "3":
            list_contacts()
        elif choice == "4":
            print("Exiting Contact Book...")
            break
        else:
            print("invalid choice")
            