class Complex:

    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def prompt(self):
        self.real = int(input("Please enter the real part: "))
        self.imaginary = int(input("Please enter the imaginary part: "))

    def display(self):
        print("{} + {}i" .format(self.real, self.imaginary))  

def main():
    c1 = Complex()
    c2 = Complex()
    print("The values are:")
    c1.display()
    c2.display()
    print()
    c1.prompt()
    print()
    c2.prompt()
    print()
    print("The values are:")
    c1.display()
    c2.display()

if __name__ == "__main__":
    main()             

