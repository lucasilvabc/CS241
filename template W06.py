class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
    
    def prompt_for_point(self):
        self.x = float(input("Enter x: "))
        self.y = float(input("Enter y: "))
    
    def display(self):
        print("Center:\n({}, {}) ".format(self.x, self.y))
    
class Circle():
    def __init__(self):
        self.center = Point()
        self.radius = 0
    
    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = float(input("Enter radius: "))
        
    def display(self):
        self.center.display()
        print("Radius: {}".format(self.radius))
    
def main():
    circle1 = Circle()
    circle1.prompt_for_circle()
    circle1.display()
    
if __name__ == "__main__":
    main()