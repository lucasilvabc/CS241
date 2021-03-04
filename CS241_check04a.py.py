# TJ OBrien - check04a                                                              

class person:

    def __init__(self):
        self.name = "anonymous"
        self.year = "unknown"

    def display(self):
        print("{} (b. {})".format(self.name, self.year))

    def __str__(self):
        return str(self.name), str(self.year)


class book:

    def __init__(self):
        self.title = "untitled"
        self.author = person()
        self.publisher = "unpublished"

    def display(self):
        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        self.author.display()


def main():

    info = book()
    info.display()

    print('')

    print("Please enter the following:")
    info.author.name = input("Name: ")
    info.author.year = input("Year: ")
    info.title = input("Title: ")
    info.publisher = input("Publisher: ")

    print('')

    info.display()

if __name__ == "__main__":
    main()