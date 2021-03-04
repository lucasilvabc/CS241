class student_info:
    def __init__(self):
        self.a = input("Please enter your first name: ") 
        self.b = input("Please enter your last name: ") 
        self.c = int(input("Please enter your id number: "))

    def show_info(self):
        print('')
        print("Your information:")
        print("{} - {} {}".format(self.c, self.a, self.b))

def main():
    my_class = student_info()
    my_class.show_info()

if __name__ == "__main__":
    main()    