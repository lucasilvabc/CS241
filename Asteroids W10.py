from abc import ABC
from abc import abstractmethod
import arcade
import math
import random



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_SCALE = .75
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30
SHIP_SCALE = .75
SHIELD_RADIUS = 63
SHIELD_SCALE = .75
INITIAL_ROCK_COUNT = 5
ASTEROID_SCALE = .75
BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15
MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

class Point:
    
     def __init__(self, init_x, init_y):
         self.x = init_x
         self.y = init_y
 
class Velocity:
     
     def __init__(self, init_dx, init_dy):
         self.dx = init_dx
         self.dy = init_dy
 
class flying_object:
      
      def __init__(self):
          self.center = Point(0,0) 
          self.velocity = Velocity(0,0)
          self.angle = 0
          self.object = -1
          self.rotate = 0
          self.alive = True
          self.rotation = 0

      def advance(self):
          self.center.x += self.velocity.dx
          self.center.y += self.velocity.dy
          self.rotate += self.rotation
          if self.rotate == 359:
              self.rotate = 0

      def is_off_screen(self):
          if self.center.x > SCREEN_WIDTH:
              self.center.x = 0
          elif self.center.y > SCREEN_HEIGHT:
              self.center.y = 0
          elif self.center.x < 0:
              self.center.x = SCREEN_WIDTH
          elif self.center.y < 0:
              self.center.y = SCREEN_HEIGHT

class Shield(flying_object):
      
      def __init__(self, ship):
          self.ship = ship
          super().__init__()
          self.radius = SHIELD_RADIUS
          self.scale = SHIELD_SCALE
          self.shield_type = 3

      def draw(self):
          self.center.x = self.ship.center.x
          self.center.y = self.ship.center.y
          self.angle = self.ship.angle



          if self.shield_type == 3:
              
              img = "images/shield3.png"
              texture = arcade.load_texture(img)
              
              # Draw shield
              arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, self.angle - 90, 255)

          elif self.shield_type == 2:
              
              img = "images/shield2.png"
              texture = arcade.load_texture(img)
              
              # Draw shield
              arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, self.angle - 90, 255)

          elif self.shield_type == 1:
              
              img = "images/shield1.png"
              texture = arcade.load_texture(img)
              
              # Draw shield
              arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, self.angle - 90, 255)

          elif self.shield_type == -1:
              
              img = "images/playerShip1_damage3.png"
              texture = arcade.load_texture(img)
            
              # Draw shield
              arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, self.angle - 90, 255)

          elif self.shield_type < -1:
              
              self.ship.alive = False

class Ship(flying_object):
    def __init__(self):
        super().__init__()
        self.radius = SHIP_RADIUS
        self.center.x = SCREEN_WIDTH - 50
        self.center.y = 50
        self.scale = SHIP_SCALE

    def draw(self):
        img = "images/playerShip1_green.png"
        texture = arcade.load_texture(img)
        angle = self.angle - 90

        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, angle , 255)

    def rotate_right(self):
        self.angle -= SHIP_TURN_AMOUNT

    def rotate_left(self):
        self.angle += SHIP_TURN_AMOUNT
     
    def thrust_forward(self):
        self.velocity.dx += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT

     
    def thrust_backward(self):
        self.velocity.dx -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT

 
class Bullet(flying_object):
     def __init__(self):
         super().__init__()
         self.radius = BULLET_RADIUS
         self.scale = BULLET_SCALE
         self.frame_counter = 0

     def draw(self):
         img = "images/laserBlue01.png"
         texture = arcade.load_texture(img)
        
         # Draw bullet
         arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, self.angle - 90, 255)

     def fire(self, angle, ship_dx, ship_dy):
         self.velocity.dx = ship_dx + math.cos(math.radians(angle)) * BULLET_SPEED
         self.velocity.dy = ship_dy + math.sin(math.radians(angle)) * BULLET_SPEED

class Asteroid(flying_object):
     def __init__(self):
         super().__init__()
         self.scale = ASTEROID_SCALE
         self.asteroid_type = 0
         self.radius = 0

     def get_center_x(self):
         return self.center.x
     def get_center_y(self):
         return self.center.y

     def draw(self):
         if self.asteroid_type == 0:
             self.radius = BIG_ROCK_RADIUS
             
         elif self.asteroid_type == 1:
             self.radius = MEDIUM_ROCK_RADIUS

         elif self.asteroid_type == 2 or self.asteroid_type == 3:
             self.radius = SMALL_ROCK_RADIUS

         if self.asteroid_type == 0:
             img = "images/meteorGrey_big1.png"
             texture = arcade.load_texture(img)
             arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, 90 - self.rotate)
         if self.asteroid_type == 1:
             img = "images/meteorGrey_med1.png"
             texture = arcade.load_texture(img)
             arcade.draw_texture_rectangle(self.center.x, self.center.y, self.scale * texture.width, self.scale * texture.height, texture, 90 - self.rotate)
         if self.asteroid_type == 2 or self.asteroid_type == 3:
             img = "images/meteorGrey_small1.png"
             texture = arcade.load_texture(img)
             arcade.draw_texture_rectangle(self.center.x, self.center.y,  self.scale * texture.width, self.scale * texture.height, texture, 90 - self.rotate)


class Game(arcade.Window):
     
     def __init__(self, width, height):
         
         super().__init__(width, height)
         

         self.held_keys = set()

         self.ship = Ship()
         self.shield = Shield(self.ship)
         self.bullets = []
         self.asteroids = []
         self.asteroid_medium_count = 0 
         self.asteroid_small_count = 0 
         self.game_over = False
         self.game_over_count = 0



     def setup(self):
         self.background = arcade.load_texture("images/Space_background.jpg")
         
         for i in range(INITIAL_ROCK_COUNT):
             self.create_target(0, Asteroid())
        
         self.ship.angle = 135


     def on_draw(self):
         
         arcade.start_render()

         
         arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

         
         if self.ship.alive:
             self.ship.draw()
             self.shield.draw()

         

         
         for asteroid in self.asteroids: asteroid.draw()

         
         for bullet in self.bullets: bullet.draw()

         if self.game_over:
             """ Game Over Sprite """
             img = "images/text_gameover.png"
             texture = arcade.load_texture(img)
             arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, texture.width, texture.height, texture, 0)

             
             score_text = "---------(PRESS SPACE TO PLAY AGAIN)---------"
             start_x = (SCREEN_WIDTH / 2) - 150
             start_y = (SCREEN_HEIGHT / 2) - 60
             arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE)


     def update(self, delta_time):
         
         self.check_keys()
         self.check_off_screen()

         # Advance ship
         self.ship.advance()


         # Advance asteroids
         for asteroid in self.asteroids:
             asteroid.advance()

         # Advance bullets
         for bullet in self.bullets:
             bullet.advance()
             bullet.frame_counter += 1
             #TEST: print("Frame counter: ", bullet.frame_counter)
             if bullet.frame_counter == BULLET_LIFE:
                 bullet.alive = False
                 bullet.frame_counter = 0

         """Clean Up process"""
         self.check_collisions()
         self.cleanup_sprites()
         self.check_game_over()


     def create_target(self, target_type, previous_target):
         
         original_angle = random.uniform(0, 360)

         if target_type == 0: # only created on set up of game
             asteroid = previous_target
             asteroid.center.x = random.uniform(10, SCREEN_WIDTH * .75)
             asteroid.rotation = BIG_ROCK_SPIN
             asteroid.center.y = random.uniform(SCREEN_HEIGHT * .25, SCREEN_HEIGHT)
             asteroid.velocity.dx = math.cos(math.radians(original_angle)) * BIG_ROCK_SPEED
             asteroid.velocity.dy = math.sin(math.radians(original_angle)) * BIG_ROCK_SPEED
             asteroid.asteroid_type = 0

         elif target_type == 1: # 2 medium asteroids (large asteroid hit)
             asteroid = Asteroid()
             asteroid.asteroid_type = 1
             if self.asteroid_medium_count == 0:
                 asteroid.rotation = MEDIUM_ROCK_SPIN
                 asteroid.velocity.dx = previous_target.velocity.dx + 2
                 asteroid.velocity.dy = previous_target.velocity.dy
                 self.asteroid_medium_count = 1
             elif self.asteroid_medium_count == 1:
                 asteroid.rotation = MEDIUM_ROCK_SPIN
                 asteroid.velocity.dx = previous_target.velocity.dx - 2
                 asteroid.velocity.dy = previous_target.velocity.dy
                 self.asteroid_medium_count = 0

             # random_angle = random.uniform(0, 360)
             asteroid.center.x = previous_target.center.x
             asteroid.center.y = previous_target.center.y

         elif target_type == 2: # single small asteroid (large asteroid hit)
             asteroid = Asteroid()
             asteroid.asteroid_type = 2
             asteroid.rotation = SMALL_ROCK_SPIN
             asteroid.velocity.dx = previous_target.velocity.dx
             asteroid.velocity.dy = previous_target.velocity.dy + 5
             random_angle = random.uniform(0, 360)
             asteroid.center.x = previous_target.center.x
             asteroid.center.y = previous_target.center.y

         elif target_type == 3: # 2 small asteroids (medium asteroid hit)
             asteroid = Asteroid()
             asteroid.asteroid_type = 3
             if self.asteroid_small_count == 0:
                 asteroid.rotation = SMALL_ROCK_SPIN
                 asteroid.velocity.dx = previous_target.velocity.dx + 1.5
                 asteroid.velocity.dy = previous_target.velocity.dy + 1.5
                 self.asteroid_small_count = 1
             elif self.asteroid_small_count == 1:
                 asteroid.rotation = SMALL_ROCK_SPIN
                 asteroid.velocity.dx = previous_target.velocity.dx - 1.5
                 asteroid.velocity.dy = previous_target.velocity.dy - 1.5
                 self.asteroid_small_count = 0

             random_angle = random.uniform(0, 360)
             asteroid.center.x = previous_target.center.x
             asteroid.center.y = previous_target.center.y

         else:
             print("Target creating error")

         self.asteroids.append(asteroid)

     def check_keys(self):
         
         if arcade.key.LEFT in self.held_keys:
             self.ship.rotate_left()

         if arcade.key.RIGHT in self.held_keys:
             self.ship.rotate_right()

         if arcade.key.UP in self.held_keys:
             self.ship.thrust_forward()

         if arcade.key.DOWN in self.held_keys:
             self.ship.thrust_backward()
         # Machine gun mode...
         #if arcade.key.SPACE in self.held_keys:
         # pass
     def on_key_press(self, key: int, modifiers: int):
         
         if self.ship.alive: # Only fire if ship is alive
             self.held_keys.add(key)

             if key == arcade.key.SPACE:
                 # DONE: Fire the bullet here!
                 bullet = Bullet()
                 bullet_angle = self.ship.angle
                 bullet.angle = self.ship.angle + 90
                 bullet.center.x = self.ship.center.x
                 bullet.center.y = self.ship.center.y
                 ship_velocity_dx = self.ship.velocity.dx
                 ship_velocity_dy = self.ship.velocity.dy
                 bullet.fire(bullet_angle, ship_velocity_dx, ship_velocity_dy)
                 self.bullets.append(bullet)

         if self.game_over:
             if key == arcade.key.SPACE:
                 arcade.close_window()
                 window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
                 window.setup()
                 arcade.run()

             else:
                 print("Game Finalized by User")
     def on_key_release(self, key: int, modifiers: int):
         
         if key in self.held_keys:
             self.held_keys.remove(key)

     def cleanup_sprites(self):
         
         for bullet in self.bullets:
             if not bullet.alive:
                 self.bullets.remove(bullet)

         for asteroid in self.asteroids:
             if not asteroid.alive:
                 self.asteroids.remove(asteroid)



     def check_collisions(self):
         

         for bullet in self.bullets:
             for asteroid in self.asteroids:

                 # Make sure they are both alive before checking for a collision
                 if bullet.alive and asteroid.alive:
                     too_close = bullet.radius + asteroid.radius

                     if (abs(bullet.center.x - asteroid.center.x) < too_close and abs(bullet.center.y - asteroid.center.y) < too_close):
                         # its a hit!
                         bullet.alive = False
                         asteroid.alive = False

                         if asteroid.asteroid_type == 0:
                             self.create_target(1, asteroid)
                             self.create_target(1, asteroid)
                             self.create_target(2, asteroid)
                         elif asteroid.asteroid_type == 1:
                             self.create_target(3, asteroid)
                             self.create_target(3, asteroid)

             
         for asteroid in self.asteroids:
            
             if asteroid.alive and self.ship.alive and self.shield.shield_type == -1:

                 too_close = asteroid.radius + self.ship.radius
                 if (abs(self.ship.center.x - asteroid.center.x) < too_close and abs(self.ship.center.y - asteroid.center.y) < too_close):

                     asteroid.alive = False
                     self.ship.alive = False

             
         for asteroid in self.asteroids:
             if asteroid.alive and self.ship.alive:

                 too_close = asteroid.radius + self.shield.radius
                 if (abs(self.shield.center.x - asteroid.center.x) < too_close and abs(self.shield.center.y - asteroid.center.y) < too_close):
                     asteroid.alive = False
                     self.shield.shield_type -= 1


     def check_off_screen(self):
         
         for asteroid in self.asteroids:
             asteroid.is_off_screen()

         for bullet in self.bullets:
             bullet.is_off_screen()

         self.ship.is_off_screen()

     def check_game_over(self):
         if not self.ship.alive:
             self.game_over = True
         else:
             self.game_over = False
         return self.game_over 


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()
arcade.run()