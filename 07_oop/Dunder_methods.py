#Python uses special methods wrapped in double underscores (called "Dunder" methods or Magic Methods) to control how objects behave
#There is __init__ for object initialization, 
#__str__ for string representation, 
# __add__ for addition, etc
#You can even create your own Dunder methods to customize behavior

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # The __str__ magic method overrides what happens when you print the object
    def __str__(self):
        return f"'{self.title}' written by {self.author}"

my_book = Book("King of Wrath", "Ana Huang")

print(my_book)