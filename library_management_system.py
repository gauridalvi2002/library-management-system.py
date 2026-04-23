# Library Management System

library = {}


def add_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        print("Book already exists!")
        return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "name": name,
        "author": author,
        "issued": False
    }

    print("Book added successfully!")



def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id not in library:
        print("Book not found!")
        return

    if library[book_id]["issued"]:
        print("Book already issued!")
    else:
        library[book_id]["issued"] = True
        print("Book issued successfully!")



def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id not in library:
        print("Book not found!")
        return

    if not library[book_id]["issued"]:
        print("Book was not issued!")
    else:
        library[book_id]["issued"] = False
        print("Book returned successfully!")



def display_books():
    if not library:
        print("No books in library.")
        return

    print("\nAvailable Books:")
    for book_id, details in library.items():
        status = "Issued" if details["issued"] else "Available"
        print(f"ID: {book_id} | Name: {details['name']} | Author: {details['author']} | Status: {status}")



def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")



menu()