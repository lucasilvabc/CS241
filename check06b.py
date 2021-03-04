class Phone:

    def __init__(self):
        """ Initialize Variables """
        self.area_code = 123
        self.prefix = 123
        self.suffix = 1234

    def prompt_number(self):
        """ Prompt user for values """ 
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display(self):
        """ Display info """
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))


class SmartPhone(Phone):

    def __init__(self):
        """ Initialize Variables """
        Phone.__init__(self)
        self.email = "unknown"

    def prompt(self):
        """" Prompt user for values """
        Phone.prompt_number(self)
        self.email = input("Email: ")

    def display(self):
        """ Display info """
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))
        print(self.email)

def main():
    """ Call classes and functions """
    p = Phone()
    print("Phone:")
    p.prompt_number()
    print()
    p.display()
    print()
    sp = SmartPhone()
    print("Smart phone:")
    sp.prompt()
    print()
    sp.display()


if __name__ == "__main__":
    main()




