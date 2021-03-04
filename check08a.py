class GPA:
    def __init__(self):
        self.gpa_value = 0.0
    def get_gpa(self):
        return self.gpa_value
    def set_gpa(self, value):
        self.gpa_value = value

    """Conver GPA 4.0 to A, 3.0 to B, 2.0 to C, 1.0 to F, 0 to F """
    def get_letter(self):
        if self.get_gpa() < 4.0:
            if self.get_gpa() < 3.0:
                if self.get_gpa() < 2.0:
                    if self.get_gpa() < 1.0:
                        return 'F'
                    return 'D'
                return 'C'
            return 'B'
        return 'A'
        
    def set_letter(self, letter):
        if letter == 'A':
            self.set_gpa(4.0)
        elif letter == 'B':
            self.set_gpa(3.0)
        elif letter =='C':
            self.set_gpa(2.0)
        elif letter =='D':
            self.set_gpa(1.0)
        elif letter =='F':
            self.set_gpa(0.0)

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()