class Book:

    def __init__(self, title : str, author : str):
        self._title = title
        self._author = author
    
    def __str__(self):
        return f'{self._title} by {self._author}'


class Member:

    def __init__(self, name : str):
        self._name = name
        self._books = set() # Set of lent books
    
    def borrow_book(self, book : Book, library):
        if (borrowed_book := library.lend_book(book)):
            print(f'{self._name} has borrowed {book}')
            self._books.add(borrowed_book)

    def return_book(self, book : Book, library):
        if not book in self._books:
            print(f'{self._name} doesn\'t have that book')
            return False
        else:
            print(f'{self._name} has returned {book}.')
            library.return_book(book)
    
    def get_borrowed_books(self):
        print(self._books)

class Library:

    def __init__(self):
        self._books = {} # Dictionary of (Book:Amount)
        self._members = set() # Set

    def add_book(self, book : Book, copies = 1) -> None:
        if book in self._books.keys(): # If book is in library
            self._books[book] += copies # Increase inventory
        else: # If not
            self._books[book] = copies # Add one copy to library

    def register_member(self, name : str) -> Member:
        member = Member(name)
        self._members.add(member)
        return member
    
    def book_available(self, book : Book) -> bool:
        if not book in self._books.keys():
            print(f'{book} is not stocked at this library')
            return False
        elif book in self._books.keys() and self._books[book] <= 0:
            print(f'{book} is out of stock')
            return False
        else:
            return True
        
    def lend_book(self, book : Book) -> Book:
        if not self.book_available(book):
            return None
        else:
            self._books[book] -= 1
            return book
    
    def return_book(self, book : Book) -> None:
        self.add_book(book)

    def see_book_inventory(self) -> list[Book]:
        return self._books.keys()
        



        

