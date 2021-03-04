"""
This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 20

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

#Velocity
class Velocity:
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0
 
#Point for the Ball and Paddle.
class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

#W07 CHANGE THIS CODE BELOW
class FlyingObject:
    """The FlyingObject has all the"""
    def __init__(self):
        self.center = point()
        self.velocity = Velocity()
 
# Bullet
class Bullet(FlyingObject):
    """Setting for Buullet"""
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
 
        self.center.x = 0
        self.center.y = 0
 
        self.velocity.dx = BULLET_SPEED  # 10
        self.velocity.dy = BULLET_SPEED  # 10
        self.alive = True

    def advance(self):
        """ Move horizontally. """
        self.center.x += self.velocity.dx
        """ Move Vertically. """
        self.center.y += self.velocity.dy
 
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)
 
    def is_off_screen(self, screen_width, screen_height):
        """ if off screen, delete bullet """
        if self.center.x > screen_width or self.center.y > screen_height or self.center.x < 0 or self.center.y < 0:
            """ off screen, the bullet is deleted """
            self.alive = False
 
    def fire(self, angle):
        """ fire mooving horizontally."""
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        """ fire moving vertically. """
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED

#Target
class Target(FlyingObject):
    """setting for Target"""
    def __init__(self):
        self.center = Point()
        self.center.x = random.uniform(0, SCREEN_WIDTH / 2)
        self.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
        self.velocity = Velocity()
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 5)
        self.radius = 0.0
        self.alive = True
 
    def advance(self):
        """horizontally."""
        self.center.x += self.velocity.dx
        """Vertically."""
        self.center.y += self.velocity.dy
 
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, TARGET_COLOR)
 
    def is_off_screen(self, screen_width, screen_height):
        """ if off screen, delete bullet"""
        if self.center.x > screen_width or self.center.y > screen_height or self.center.x < 0 or self.center.y < 0:
            self.alive = False

    def hit(self):
        """when you hit the target staetment"""
        if self.lives <= 1:
            self.alive = False
            return self.killPoints
        else:
            self.lives -= 1
            return 0
    

class Standard(Target):
    """Taget piont counting"""
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.killPoints = 1
        self.lives = 1
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, TARGET_COLOR)
 
class Safe(Target):
    """Taget piont counting"""
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.killPoints = 5
        self.lives = 1
 
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, arcade.color.RED)

class Strong(Target):
    """Taget piont counting"""
    def __init__(self):
        super().__init__()
        self.radius = 20
        self.killPoints = -10
        self.lives = 1
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, arcade.color.BLACK)
        

"""
Original Code
"""

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        random.seed()
        
        # decide if we should start a target
        #W07 ADDING THIS CODE BELOW
        #if len(self.targets) < 5:
        if random.randint(1, 50) == 1:    
            self.create_target()
            
        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()
        

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        #Standard = Standard()
        #Strong = Strong()
        #Safe = Safe()

        #self.targets.append(Strong)
        #self.targets.append(Safe)    
        #self.targets.append(Standard)

        """New code: Change this part to create target for standard, Strong, Safe"""
        targetNumber = random.randint(1, 3)
        if targetNumber == 1:
            target = Standard()
        elif targetNumber == 2:
            target = Strong()
        elif targetNumber == 3:
            target = Safe()

        self.targets.append(target)
        
    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """
        # NOTE: This assumes you named your targets list "targets"
        for bullet in self.bullets:
            for target in self.targets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
