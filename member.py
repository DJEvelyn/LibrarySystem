from imports import * 

class Member:

    def __init__(self, name : str):
        self._name = name
        self._books = set() # Set of lent books
    
    def borrow_book(self, book : Book, library : Library):
        if (borrowed_book := library.lend_book(book)):
            self._books.add(borrowed_book)
    
    def get_borrowed_books(self):
        print(self._books)


    