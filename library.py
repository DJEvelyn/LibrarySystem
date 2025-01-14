from imports import * 

class Library:

    def __init__(self):
        self._books = {} # Dictionary of (Book:Amount)
        self._members = set() # Set

    def add_book(self, book : Book) -> None:
        if book in self._books.keys(): # If book is in library
            self._books[book] += 1 # Increase inventory
        else: # If not
            self._books[book] = 1 # Add one copy to library

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

        if not self.book_available():
            return None
        else:
            self._books[book] -= 1
            return book
    
    def return_book(self, book : Book) -> None:
        self.add_book(book)

    def see_book_inventory(self) -> list[Book]:
        return self._books.keys()
        






        




