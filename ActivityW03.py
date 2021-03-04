class Rational:
    """ Comment """
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
    def display(self):
        if self.numerator > self.denominator:
            integer = self.numerator // self.denominator
            new_numerator = self.numerator % self.denominator
            print("{} {}/{}".format(integer, new_numerator, self.denominator))
        else:
            print("{}/{}".format(self.numerator,self.denominator))
    def prompt(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))
    def display_decimal(self):
        print(float(self.numerator/self.denominator))
    def reduce(self):
        divisor = 1
        mdc=1
        while divisor <= self.numerator:
            if self.numerator % divisor == 0 and self.denominator % divisor == 0:
                mdc = divisor
            divisor+=1
        new_numerator = self.numerator // mdc
        new_denominator = self.denominator // mdc
        print ("{}/{}".format(new_numerator, new_denominator))
​
    def multiply_by(self):
        new_numerator = int(input("Enter the numerator: "))
        new_denominator = int(input("Enter the denominator: "))
        self.numerator = new_numerator * self.numerator
        self.denominator = new_denominator * self.denominator
        print("Here is the result of multiplication: {}/{}".format(self.numerator,self.denominator))
​
""" def reduce(self):
        mdc(self.numerator, self.denominator)
        print("Reduced fraction: {}/{}")
    def mdc(self):
        if self.numerator % self.denominator == 0:
            return n
        else:
            return mdc(n, m % n)"""
​
def main():
    """n1 = Rational()
    n1.display()
    n2 = Rational()
    n2.prompt()
    n2.display()
    n2.display_decimal()"""
    n3 = Rational()
    n3.prompt()
    n3.multiply_by()
    n3.reduce()
​
if __name__ == "__main__":
    main()