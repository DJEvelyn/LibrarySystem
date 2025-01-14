from library_classes import *

# Create books
book_one = Book('1984', 'George Orwell')
book_two = Book('War and Peace', 'Leo Tolstoy')
book_three = Book('The Handmaid\'s Tale', 'Margaret Atwood')
book_four = Book('Pride and Prejudice', 'Jane Austin')

# Create library
my_library = Library()

# Add books to library
my_library.add_book(book_one)
my_library.add_book(book_two)
my_library.add_book(book_three)
my_library.add_book(book_four)

# Create members
member_one = my_library.register_member("John Smith")
member_two = my_library.register_member("Sarah Johnson")

# Borrow books
member_one.borrow_book(book_one, my_library)
member_two.borrow_book(book_one, my_library)
member_two.borrow_book(book_three, my_library)
member_one.return_book(book_one, my_library)
member_two.borrow_book(book_one, my_library)



