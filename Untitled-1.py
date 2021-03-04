class Robot:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100
        self.enough_fuel = True

    def fuel_amount(self):
        if self.fuel <= 0:
            print("Insufficient fuel to perform action")
            self.enough_fuel = False            

    def refuel(self):
        ''' If the user finds the correct location to refuel, then they can refuel. '''
        print("jackrabbit is looking for fuel...")
        if self.x == 1 and self.y == 1:
            if self.fuel < 250:
                self.fuel += 75
                print("jackrabbit has found a fueling station")
            else:
                print("jackrabbit has to much fuel") 
        elif self.x == 5 and self.y == 5:
            print("jackrabbit has found a canister of fuel")
            if self.fuel < 250:
                self.fuel += 50
            else:
                print("jackrabbit is fuel quantity is full")

    def left(self):
        self.fuel_amount()
        if self.enough_fuel:
            self.x -= 1
            self.fuel -= 5
            
    def right(self):
        self.fuel_amount()
        if self.enough_fuel:
            self.x += 1
            self.fuel -= 5
    
    def up(self):
        self.fuel_amount()
        if self.enough_fuel:
            self.y -= 1
            self.fuel -= 5
    
    def down(self):
        self.fuel_amount()
        if self.enough_fuel:
            self.y += 1
            self.fuel -= 5
            
    def fire(self):
        self.fuel_amount()
        if self.enough_fuel and self.fuel > 15:
            self.fuel -= 15
            print("Pew! Pew!")
        else:
            print("Insufficient fuel to perform action")
            
    def display_status(self):
        print(f"({self.x}, {self.y}) - Fuel: {self.fuel}")
    
        
def main():
        jackrabbit = Robot()
        command = None  
        while jackrabbit.fuel != "quit":
            jackrabbit.robot = input("Enter command: ").lower().strip()
            if jackrabbit.robot == "left":
                jackrabbit.left()
            elif jackrabbit.robot == "right":
                jackrabbit.right()
            elif jackrabbit.robot == "up":
                jackrabbit.up()
            elif jackrabbit.robot == "down":
                jackrabbit.down()
            elif jackrabbit.robot == "fire":
                jackrabbit.fire()
            elif jackrabbit.robot == "status":
                jackrabbit.display_status()    
            elif jackrabbit.robot == "refuel":
                jackrabbit.refuel()
        print("Goodbye.")        
                
            
            
if __name__ == "__main__":
    main()