class Library:
    book_list=[]

    @classmethod
    def entry_book(self,Books):
        self.book_list.append(Books)

    @classmethod
    def view_all_books(self):
        if not self.book_list:
            print("No books available in the library.")
        else:
            for book in self.book_list:
                print(book.view_book_info())

class Book:
    def __init__(self,book_id,title,author,availability=True):
        self._book_id=book_id
        self._title=title
        self._author=author
        self._availability=availability
    
    def borrow_book(self):
        if self._availability:
            self._availability=False
            return f"You have successfully borrowed '{self._title}'."
        else:
            return f"Sorry, '{self._title}' is currently not available."
    
    def return_book(self):
        if not self._availability:
            self._availability=True
            return f"'{self._title}' has been successfully returned."
        else:
            return f"'{self._title}' was not borrowed."

    def view_book_info(self):
        availability_status = "Available" if self._availability else "Not Available"
        return (f"ID: {self._book_id} ,"
                f"Title: {self._title} ,"
                f"Author: {self._author} ,"
                f"Availability: {availability_status}")
    
    def __repr__(self):
        return (f'Book_ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Availability: {self._availability}\n')

book1=Book(101,'Python Programming','shahinur',True)
book2=Book(102,'Java Programming','shakil',True)
book3=Book(103,'C Programming','riad',True)

Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            Library.view_all_books()

        elif choice == "2":
            book_id = input("Enter the Book ID to borrow: ")
            book = None
            for b in Library.book_list:
                if str(b._book_id) == book_id:
                    book = b
                    break
            if book:
                print(book.borrow_book())
            else:
                print("Book not found.")

        elif choice == "3":
            book_id = input("Enter the Book ID to return: ")
            for b in Library.book_list:
                if str(b._book_id) == book_id:
                    book = b
                    break
            if book:
                print(book.return_book())
            else:
                print("Book not found.")

        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()



    

