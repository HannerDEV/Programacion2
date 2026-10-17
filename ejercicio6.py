from typing import Dict,TypedDict

class Contact (TypedDict):
    phone_number: str
    email: str
    address: str
    birthday: str

Address_Book = Dict[str, Contact]

def request_field(prompt: str, obligatorio: bool = True) -> str:
    while True:
        valor = input(prompt).strip().title()
        if valor or not obligatorio:
            return valor
        print("The field cannot be empty")

def show_address_book(address_book: Dict[str, Contact]) -> None:
    for i, (nombre, contacto) in enumerate(sorted(address_book.items()), start=1):
        print(f"Contacto #{i}: {nombre:<10}")
        print(f"Phone number: {contacto['phone_number']:<10}")
        print(f"Email: {contacto['email']:<10}")
        print(f"Address: {contacto['address']:<10}")
        print(f"Birthday: {contacto['birthday']:<10}\n")

def add_contact(address_book: Dict[str, Contact]) -> None:
    username = request_field("Enter full name:")

    if username in address_book:
        print(f"The contact {username} is already in address book")
        return

    phone_number = request_field("Enter the phone number: ")
    email = request_field("Enter the email: ")
    address = request_field("Enter the address: ")
    birthday = request_field("Enter the birthday: ")

    address_book[username] = {
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "birthday": birthday,
    }
    print(f"Contacto {username} registrado exitosamente!\n")

def edit_contact(address_book: Dict[str, Contact]):
    username = request_field("Enter full name:")

    if username not in address_book:
        print("Contact not found")
        return

    phone_number = request_field("Enter the phone number: ", False)
    email = request_field("Enter the email: ", False)
    address = request_field("Enter the address: ", False)
    birthday = request_field("Enter the birthday: ", False)

    address_book[username] = {
        "phone_number": phone_number,
        "email": email,
        "address": address,
        "birthday": birthday,
    }

def delete_contact(address_book: Dict[str, Contact]):
    username = request_field("Enter full name:")

    encontrado = address_book.pop(username, False)
    
    if not encontrado:
        print(f"The contact {username} is not in adress book")
        return
    print("The contact was sucessfully deleted")
    

def main()-> None:
    address_book: Address_Book = {}
    options = {
        "1": show_address_book,
        "2": add_contact, 
        "3": edit_contact, 
        "4": delete_contact }

    
    print(f"{"="*12} WELCOME TO THE ADDRESS BOOK {"="*12}\n")

    while True:
        print("""
        1. Show address book
        2. Add contact
        3. Edit contact
        4. Delete contact
        5. Exit\n
        """)

        option = input("Enter an option: ").strip()
        if option == "5":
            print("Exiting...")
            break

        accion = options.get(option)
        if accion:
            accion(address_book)
        else:
            print("Invalid option, enter again:")

if __name__ == "__main__":
    main()