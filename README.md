# 📚 Library Management System (Python)

## 📌 Project Description

This is a simple **Library Management System** built using Python.
It is a menu-driven program that allows users to manage books in a library efficiently.

---

## 🚀 Features

* ➕ Add new books
* 📖 Issue books
* 🔄 Return books
* 📋 Display all books
* ⚠️ Handles invalid inputs

---

## 🛠️ Technologies Used

* Python 3
* Dictionaries (for data storage)
* Functions (for modular code)

---

## 📂 How It Works

* The program stores book details in a **dictionary**.

* Each book has:

  * Book ID
  * Book Name
  * Author Name
  * Status (Available / Issued)

* A **menu-driven system** allows users to choose operations.

---

## ▶️ How to Run

1. Install Python
2. Download or clone this repository
3. Open terminal / command prompt
4. Run the file:

```bash
python library.py
```

---

## 🧪 Sample Output

```
--- Library Management System ---
1. Add Book
2. Issue Book
3. Return Book
4. Display Books
5. Exit

Enter your choice: 1
Enter Book ID: 101
Enter Book Name: Python Basics
Enter Author Name: John
Book added successfully!
```

---

## 🧠 Logic Explanation

* A dictionary is used to store book data.

* Each function performs a specific task:

  * `add_book()` → Adds book details
  * `issue_book()` → Marks book as issued
  * `return_book()` → Marks book as returned
  * `display_books()` → Displays all books

* A loop keeps the program running until the user exits.

---



## 📌 Future Improvements

* Add user details while issuing books
* Search book feature
* GUI version using Tkinter
* Database integration

---

## 🙌 Conclusion

This project demonstrates basic Python concepts like dictionaries, functions, and loops while building a real-world application.

---
