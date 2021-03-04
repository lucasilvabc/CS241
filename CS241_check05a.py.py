
class Ship:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        
    def advance(self):
        
        self.ship.x += self.ship.dx
        self.ship.y += self.ship.dy
        
    def draw(self):
        print("Drawing ship at ({}, {})".format(self.ship.x, self.ship.y))
        
        
class Game:
    
    def __init__(self, dx, dy):
        
        self.ship = Ship()
        
        self.ship.dx = dx
        self.ship.dy = dy
        
    def on_draw(self):
        
        Ship.draw(self)
        
        
    def update(self):
        
        Ship.advance(self)