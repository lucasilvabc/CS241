class Robot:
    ''' Creates behaviors/ moviments that my Roblox can perform based on user input. '''
    def __init__(self):
        self.fuel_quantity  = 100
        self.enough_fuel = True
        self.x_coordinate = 10
        self.y_coordinate = 10

    def fuel_amount(self):
        ''' Represents the amount of fuel my Roblox has. '''
        if self.fuel_quantity <= 0:
            print("Insufficient fuel to perform action")
            self.enough_fuel = False

    def refuel(self):
        ''' If the user finds the correct location to refuel, then they can refuel. '''
        print("Roblox is looking for fuel...")
        if self.x_coordinate == 1 and self.y_coordinate ==1:
            if self.fuel_quantity < 250:
                self.fuel_quantity += 75
                print("Roblox has found a fueling station")
            else:
                print("Roblox has to much fuel") 
        elif self.x_coordinate == 5 and self.y_coordinate == 5:
            print("Roblox has found a canister of fuel")
            if self.fuel_quantity < 250:
                self.fuel_quantity +=50
            else:
                print("Roblox is fuel quantity is full")

    def move_right(self):
        ''' This will move Roblox to the right when the user runs it. '''
        self.fuel_amount()
        if self.enough_fuel:
            self.fuel_quantity -= 5
            self.x_coordinate += 1 

    def move_left(self):
        ''' This will move Roblox to the left when the user runs it. '''
        self.fuel_amount()
        if self.enough_fuel:
            self.fuel_quantity -= 5
            self.x_coordinate -= 1 

    def move_up(self):
        ''' This will move Roblox up when the user runs it. '''
        self.fuel_amount()
        if self.enough_fuel:
            self.fuel_quantity -= 5
            self.y_coordinate -= 1 

    def move_down(self):
        ''' This will move Roblox down when the user runs it. '''
        self.fuel_amount()
        if self.enough_fuel:
            self.fuel_quantity -= 5
            self.y_coordinate += 1

    def fire_laser(self):
        ''' The user must have sufficient fuel to fire the laser. Takes 15 fuel '''
        self.fuel_amount()
        if self.enough_fuel and self.fuel_quantity > 15:
            self.fuel_quantity -= 15
            print("Pew! Pew!")
        else:
            print("Insufficient fuel to perform action")

    def display(self):
        ''' Displays the status of where Roblox is and how much fuel it has. '''
        print(f"({self.x_coordinate}, {self.y_coordinate}) - Fuel: {self.fuel_quantity}")


def main():
    ''' The user will input certain commands for Roblox to perform an action. '''
    Roblox = Robot()
    command = None
    while command != "quit":
        command = input("Enter command: ").lower().strip()
        if command == "right":
            Roblox.move_right()
        elif command == "left":
            Roblox.move_left()
        elif command == "up":
            Roblox.move_up()
        elif command == "down":
            Roblox.move_down()
        elif command == "fire":
            Roblox.fire_laser()
        elif command == "status":
            Roblox.display()
        elif command == "refuel":
            Roblox.refuel()
    print("Goodbye.")     

if __name__ == "__main__":
    main()                                 
                                                                     