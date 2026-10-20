from typing import Dict, TypedDict

# Biblioteca
# Book: Title, Author, Year, available, ID

class Book(TypedDict):
    title: str
    author: str
    year: int
    available: bool

class User(TypedDict):
    name:str
    id: str

Users = Dict[str, User]

Library = Dict[str, Book]

library : Library = {
    "REF-001": {
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "year": 1967,
        "available": True,
    },
    "REF-002": {
        "title": "Don Quijote de la Mancha",
        "author": "Miguel de Cervantes",
        "year": 1605,
        "available": True,
    },
    "REF-003": {
        "title": "El principito",
        "author": "Antoine de Saint-Exupéry",
        "year": 1943,
        "available": True,
    },
    "REF-004": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "available": True,
    },
    "REF-005": {
        "title": "Ficciones",
        "author": "Jorge Luis Borges",
        "year": 1945,
        "available": False,
    },
}

users: Users = {
    "1099207027" : {
        "name": "Hanner Garcia Duran",
        "id": "1099207027",
    }
}

def generate_next_ref() -> str:
    if not library:
        return "REF-001"

    nums = [int(book.split("-")[1]) for book in library.keys()]

    nextnum = max(nums) + 1
    
    return f"REF-{nextnum:03d}"
    
def check_available_books() -> None:
    contador = 0
    for ref, book in library.items():
        if book["available"]:
            print(f"{ref}: {book}")
            contador += 1
    if not contador:
        print("There aren't books, retry later")

def add_new_book() -> None:
    try:
        title = input("Enter the title: ").capitalize().strip()
        author = input("Enter the name of the author: ").capitalize().strip()
        year = int(input("Enter the year: "))
    except ValueError:
        print("Valor ingresado invalido")
        return

    ref = generate_next_ref()
    
    library[ref] = {
        "title": title, 
        "author": author, 
        "year": year,
        "available": True,
        }

def search_author() -> None:
    author = input("Enter the author name: ").strip().lower()
    encontrado = False
    for book in library.values():
        if book["author"].lower() == author:
            print(book)
            encontrado = True
    if not encontrado:
        print("book not found")
    
def search_title() -> None:
    title = input("Enter the title: ").strip().lower()
    encontrado = False
    for book in library.values():
        if book["title"].lower() == title:
            print(book)
            encontrado = True
    if not encontrado:
        print("book not found")

def register_user() -> None:
    name = input("Enter the name: ")
    id = input("Enter the id: ")
    if id in users:
        print("id ya existente")
        return
    users[id] = {
        "name": name, 
        "id": id
        }

def show_users():
    for user in users:
        print(users[user])

def main():
    print(f"{'='*12}WELCOME TO THE SYSTEM LIBRARY{'='*12}")
    while True:
        options = {"1": check_available_books,
                    "2": add_new_book, 
                    "3": search_author,
                    "4": search_title,
                    "5": register_user,
                    "6": show_users,
                    }
        print(
            """
            1: Check_available_books
            2: Add a new book
            3: Search book by author
            4: Search book by title
            5: Register user
            6: Show users
            7: Exit\n
            """)
        
        option = input("Select an option: ")

        if(option == "7"):
            print("exiting...")
            break

        action = options.get(option)

        if action:
            action()
        else:
            print("Opcion no disponible")



if __name__ == "__main__":
    main()