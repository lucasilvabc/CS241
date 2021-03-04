"""
Demonstrates abstract base classes.
"""

#Import anything you need for Abstract Base Classes / methods
from abc import ABC
from abc import abstractmethod

#Convert this to an ABC 
class Shape(ABC):
    def __init__(self):
        self.name = ""
    
    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))

    #Add an abstractmethod here called get_area
    @abstractmethod
    def get_area(self):
        pass

#Create a Circle class here that derives from Shape
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0.0
    
    def get_area(self):
        return 3.14 * self.radius * self.radius

#Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"
        self.length = 0.0
        self.width = 0.0

    def get_area(self):
        return self.length * self.width

def main():

    #Declare your list of shapes here
    shape_list = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            #Declare your Circle here, set its radius, and
            # add it to the list
            circle = Circle()
            circle.radius = radius
            shape_list.append(circle)
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            #DDeclare your Rectangle here, set its length
            # and width, and add it to the list
            rectangle = Rectangle()
            rectangle.length = length
            rectangle.width =  width
            shape_list.append(rectangle)
    #Entering shapes, now lets print them all out:

    #Loop through each shape in the list, and call its display function
    for shapes in shape_list:
        shapes.display()

if __name__ == "__main__":
    main()
