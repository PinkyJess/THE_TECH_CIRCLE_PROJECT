import json 
file_path ="contact.json"
def load_contacts():

    try:
        with open(file_path,"r")as file:
            return json.load(file)
    except:
        return {}

def save_contacts(contacts):
    with open(file_path,"w") as file:
        json.dump(contacts,five)

        def add_contact(name,phone):
            contacts = load_contacts()
            contacts[name]= phone
            save_contacts(contact)
            print(f"contact'{name}'added successfully.")

def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\n---contact list---")
        for name,phone in contacts.items():
            print(f"name:{name},phone:{phone}")
        else:
            print("no contacts found.")

def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"Found:{name}-{contacts[name]}")
    else:
        print(f"contact'{name}'not found")


while True:
    print("\ncontact book menu")
    print("1.add contact")
    print("2.view  contacts")
    print("3.search contact")
    print("4.quit")
    
    choice= input ("choose an option(1-4): ")

    if choice == '4':
        print("Goodbye!")
        break
    elif choice == '1':
        name = input("Enter name")
        phone = input("Enter phone number:")
        add_contacts(name,phone)
    
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name=input("enter the name to search:")    
        search_contact(name)
    else:
        print("invalid choice.please try again.") 