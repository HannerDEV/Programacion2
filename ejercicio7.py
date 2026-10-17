from typing import Dict, TypedDict

# Biblioteca
# Book: Title, Author, Year, available, ID
Library = {
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
        "available": True,
    },
}

def Check_available_books():
    pass


def main():
    print(f"{"="*12}BIENVENIDO AL SISTEMA DE BIBLIOTECA{"="*12}")
    while True:
        options = {1: Check_available_books,
                    2: "Add a new book", 
                    3: "Search book by author",
                    4: "Search book by title",
                    5: "Register user"}
        print(
            """
            1: Check_available_books
            2: Add a new book
            3: Search book by author
            4: Search book by title
            5: Register user
            6: Exit\n
            """)
        
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Opcion no disponible")

        if(option == 6):
            print("exiting...")
            break
        action = options.get(option)

        if action:
            action()
        else:
            print("Opcion no disponible")


while __name__ == "__main__":
    main()