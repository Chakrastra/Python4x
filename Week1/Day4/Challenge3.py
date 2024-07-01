# Phonebook manager

def phone_book_manager():
    phone_book = {}

    def add_contact(name, number):
        phone_book[name] = number
        print(f"Contact {name} added to the phone book.")

    def remove_contact(name):
        if name in phone_book:
            del phone_book[name]
            print(f"Contact {name} removed from the phone book.")
        else:
            print(f"Contact {name} does not exist in the phone book.")

    def lookup_number(name):
        if name in phone_book:
            print(f"Phone number for {name} is {phone_book[name]}.")
        else:
            print(f"Contact {name} does not exist in the phone book.")

    def display_contacts_sorted():
        if phone_book:
            print("Contacts in the phone book:")
            for name in sorted(phone_book):
                print(f"- {name}:{phone_book[name]}")
        else:
            print("The phone book is empty.")

    while True:
        print("\nChoose what do you want to do:")
        print("\n1. Add a new contact")
        print("2. Remove a contact")
        print("3. Lookup a phone number")
        print("4. Display all contacts sorted alphabetically")
        print("5. Quit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)
        elif choice == '2':
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter name to lookup: ")
            lookup_number(name)
        elif choice == '4':
            display_contacts_sorted()
        elif choice == '5':
            print("Exiting Phone Book Manager. Thank you!")
            break
        else:
            print("Invalid choice.")

phone_book_manager()































