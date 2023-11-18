
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return "Contact already exists"
        else:
            contacts[name] = phone
            return "Contact added."
    except (ValueError, IndexError):
        return "Not enough infomation."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact not found."
    except (ValueError, IndexError):
        return "Not enough infomation."

def show_contact(args,contacts):
    try:
        name = args[0]
        return contacts.get(name, "Contact not found.")
    except (ValueError, IndexError):
        return "Not enough infomation."
    
def print_contacts(contacts):
    if contacts:
        for contact, phone in contacts.items():
            print (f"{contact}: {phone}")
    else: 
        print ("Contact list is empty")
   
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print_contacts(contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
