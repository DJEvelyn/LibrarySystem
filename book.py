from imports import * 

class Book:

    def __init__(self, title : str, author : str):
        self._title = title
        self._author = author
    
    def __str__(self):
        return f'{self._title} by {self._author}'