class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address, email, phone):
        if name in self.contacts:
            print(f"Contact {name} already exists.")
        else:
            self.contacts[name] = {
                'address': address,
                'email': email,
                'phone': phone
            }
            print(f"Contact {name} added.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to show.")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"  Address: {info['address']}")
                print(f"  Email: {info['email']}")
                print(f"  Phone: {info['phone']}")
                print("-" * 20)

    def get_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name: {name}")
            print(f"  Address: {info['address']}")
            print(f"  Email: {info['email']}")
            print(f"  Phone: {info['phone']}")
        else:
            print(f"Contact {name} not found.")

def main():
    book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View All Contacts")
        print("4. View Specific Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            book.add_contact(name, address, email, phone)
        elif choice == '2':
            name = input("Enter name of the contact to delete: ")
            book.delete_contact(name)
        elif choice == '3':
            book.view_contacts()
        elif choice == '4':
            name = input("Enter name of the contact to view: ")
            book.get_contact(name)
        elif choice == '5':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
