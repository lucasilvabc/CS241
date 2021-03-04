class GPA:
    def __init__(self):
        self._gpa_value = 0.0
    """
    Change your getters and setters
    to begin with underscores,
    """    
    def _get_gpa(self):
        return self._gpa_value
    """
    Change the variable that you stored the GPA value
    in to begin with an underscore.
    """
    def _set_gpa(self, value):
        self._gpa_value = value
    def _get_letter(self):
        if self._get_gpa() < 4.0:
            if self._get_gpa() < 3.0:
                if self._get_gpa() < 2.0:
                    if self._get_gpa() < 1.0:
                        return 'F'
                    return 'D'
                return 'C'
            return 'B'
        return 'A'
    def _set_letter(self, letter):
        if letter == 'A':
            self._set_gpa(4.0)
        elif letter == 'B':
            self._set_gpa(3.0)
        elif letter =='C':
            self._set_gpa(2.0)
        elif letter =='D':
            self._set_gpa(1.0)
        elif letter =='F':
            self._set_gpa(0.0)
    """
    Add a property named gpa for the _get_gpa() and _set_gpa(value)
    functions using the syntax:
    property(_get_gpa, _set_gpa) in your class.
    """
    gpa = property(_get_gpa, _set_gpa)
    
    """
    Add a property named letter that calls the _get_letter() and _set_letter(value) functions.
    This time, specify the property using
    the @property syntax for the getter and @letter.setter syntax for the setter.
    """
    @property
    def letter(self):
        return self._get_letter()
    @letter.setter
    def letter(self,letter):
        self._set_letter(letter)

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    """
    Change your main function to use these properties instead of calling your functions.
    """
    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()
