"""
Create a class for a Book that has the following member variables:
    title : string
    author : string
    publication_year : int
"""
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        print("{} ({}) by {}".format(self.title,self.publication_year, self.author))

"""
create a class for a TextBook that extends a Book and adds the following member variable:
subject : string
"""
class TextBook(Book):
    def __init__(self):
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))
        
"""
create a class for a PictureBook that that extends a Book and adds the following member variable:

illustrator : string
"""

class PictureBook(Book):
    def __init__(self):
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))


def main():
    b = Book()
    t = TextBook()
    p = PictureBook()

    b.prompt_book_info()
    print()
    b.display_book_info()
    print()

    t.prompt_book_info()
    t.prompt_subject()
    print()
    t.display_book_info()
    t.display_subject()
    print()

    p.prompt_book_info()
    p.prompt_illustrator()
    print()
    p.display_book_info()
    p.display_illustrator()

if __name__ == "__main__":
    main()
