contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
    else:
        print("Contact list is empty.")

def search_contact(search_term):
    found = False
    for name, info in contacts.items():
        if search_term in name or search_term in info['phone']:
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact(name, phone=None, email=None, address=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Test the functions
add_contact("John Doe", "123-456-7890", "john@example.com", "123 Main St")
add_contact("Jane Smith", "987-654-3210", "jane@example.com", "456 Oak St")

view_contacts()

print("\nSearch for 'John':")
search_contact("John")

print("\nUpdate 'Jane Smith' phone number:")
update_contact("Jane Smith", phone="555-555-5555")
view_contacts()

print("\nDelete 'John Doe':")
delete_contact("John Doe")
view_contacts()
