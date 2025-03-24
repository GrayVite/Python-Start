# Dunder Methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                  They are automatically called by many of Python's built-in operations
#                  They allow developers to define or customize the bahaviour of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # Edits what is returned upon calling an object using print method
    def __str__(self):
        return f"{self.title} by {self.author}"
    

    # Checks to see if two objects are equal
    # other is the second passed object
    # It would be initiated by '==' opeartor 
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # Edits the lesser than (lt) function/operator
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # Edits the greater that (gt) function/operator
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    # Allows editing the addition opeator
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # Edits the 'in' operator
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    # Customizes the index operator
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolken", 310)
book2 = Book("Harry Potter and the Philospher's Stone", "J.K. Rowling", 323)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book2)
print(book3)

print(book2 < book3)
print(book2 > book3)

print(book1 + book2)

print("Lion" in book1)

# from customizing __getitem__
print(book2['title']) 
print(book1['name'])