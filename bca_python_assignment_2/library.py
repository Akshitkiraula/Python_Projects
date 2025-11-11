"""
Name: Akshit kirula
Date: 18/11/2025
Project: Library Inventory & Borrowing System (Mini Project)

Description:
A Python CLI program to manage library books, borrowing, and returning.
Implements:
- Dictionaries, lists, sets
- Functions, loops, conditionals
- List comprehensions
- File handling (Bonus)
"""

import csv
import os

# -------------------------------------------------------------
# GLOBAL DATA STRUCTURES
# -------------------------------------------------------------

books = {}         # Stores all book records
borrowed = {}      # Stores student->book mapping


# -------------------------------------------------------------
# BONUS: Load book data from CSV (if file exists)
# -------------------------------------------------------------
def load_data():
    global books
    if os.path.exists("books.csv"):
        with open("books.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                book_id, title, author, copies = row
                books[book_id] = {
                    "title": title,
                    "author": author,
                    "copies": int(copies)
                }


# -------------------------------------------------------------
# BONUS: Save book data to CSV
# -------------------------------------------------------------
def save_data():
    with open("books.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for book_id, data in books.items():
            writer.writerow([book_id, data["title"], data["author"], data["copies"]])


# -------------------------------------------------------------
# UTILITY: Print menu
# -------------------------------------------------------------
def print_menu():
    print("\n========== LIBRARY BOOK MANAGER ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    print("===========================================")


# -------------------------------------------------------------
# TASK 2: Add Book
# -------------------------------------------------------------
def add_book():
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter number of copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print("\n✅ Book added successfully!")
    save_data()


# -------------------------------------------------------------
# TASK 3: Display Books in Table Format
# -------------------------------------------------------------
def view_books():
    if not books:
        print("\nNo books available.")
        return

    print("\n--------- BOOK LIST -----------")
    print("ID\tTitle\tAuthor\tCopies")
    print("--------------------------------")

    for book_id, info in books.items():
        print(f"{book_id}\t{info['title']}\t{info['author']}\t{info['copies']}")


# -------------------------------------------------------------
# SEARCH FUNCTIONS
# -------------------------------------------------------------
def search_by_id(book_id):
    return books.get(book_id, None)


def search_by_title(title_part):
    return [
        (bid, info)
        for bid, info in books.items()
        if title_part.lower() in info["title"].lower()
    ]


# -------------------------------------------------------------
# TASK 3: Search Book
# -------------------------------------------------------------
def search_book():
    print("\nSearch by:")
    print("1. Book ID")
    print("2. Title substring")

    choice = input("Enter choice: ")

    if choice == "1":
        bid = input("Enter Book ID: ").strip()
        result = search_by_id(bid)
        if result:
            print(f"\n✅ Book Found: {result}")
        else:
            print("\n❌ Book Not Found")

    elif choice == "2":
        text = input("Enter part of title: ").strip()
        results = search_by_title(text)

        if results:
            print("\n✅ Matches Found:")
            for bid, info in results:
                print(f"{bid}: {info}")
        else:
            print("\n❌ No matching books found.")
    else:
        print("Invalid choice.")


# -------------------------------------------------------------
# TASK 4: Borrow Book
# -------------------------------------------------------------
def borrow_book():
    student = input("Enter Student Name: ").strip()
    bid = input("Enter Book ID to borrow: ").strip()

    if bid not in books:
        print("❌ Book does not exist.")
        return

    if books[bid]["copies"] > 0:
        books[bid]["copies"] -= 1
        borrowed[student] = bid
        print(f"✅ {student} borrowed {bid}")
        save_data()
    else:
        print("❌ No copies available.")


# -------------------------------------------------------------
# TASK 5: Return Book + List Comprehension
# -------------------------------------------------------------
def return_book():
    student = input("Enter Student Name: ").strip()

    if student not in borrowed:
        print("❌ This student has not borrowed any book.")
        return

    bid = borrowed[student]
    books[bid]["copies"] += 1
    del borrowed[student]

    print(f"✅ Book {bid} returned by {student}.")
    save_data()

    print("\nBorrowed books list:")
    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    print("\n".join(borrowed_list) if borrowed_list else "None")


# -------------------------------------------------------------
# MAIN LOOP (TASK 6)
# -------------------------------------------------------------
def main():
    load_data()

    while True:
        print_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("\n📘 Exiting… Goodbye!")
            save_data()
            break
        else:
            print("Invalid option. Try again.")


# -------------------------------------------------------------
# PROGRAM STARTS HERE
# -------------------------------------------------------------
if __name__ == "__main__":
    main()
