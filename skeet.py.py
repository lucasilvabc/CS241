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
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Velocity:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class FlyingObject:
    def __init__(self, x, y, dx, dy):
        self.center = Point(x, y)
        self.velocity = Velocity(dx, dy)
        
class StandardTarget(FlyingObject):
    def __init__(self):
        super().__init__(0, random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT), random.uniform(1, 5), random.uniform(-2, 5))
        self.radius = TARGET_RADIUS
        self.alive = True
    
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, TARGET_RADIUS, TARGET_COLOR)

    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x > screen_width - 10):
            return True
        elif (self.center.y > (screen_height - 10) or self.center.y < 5):
            return True
        else:
            return False
        
    def hit(self):
        self.alive = False
        return 1
    
class StrongTarget(FlyingObject):
    def __init__(self):
        super().__init__(0, random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT), random.uniform(1, 3), random.uniform(-2, 3))
        self.radius = TARGET_RADIUS
        self.alive = True
        self.hits = 0
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(3), text_x, text_y, TARGET_COLOR, font_size=20)
        
    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x > screen_width - 10):
            return True
        elif (self.center.y > (screen_height - 10) or self.center.y < 5):
            return True
        else:
            return False
        
    def hit(self):
        if self.hits > 1:
            self.alive = False
            return 5
        else:
            self.hits = self.hits + 1
            return 1
    
class SafeTarget(FlyingObject):
    def __init__(self):
        super().__init__(0, random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT), random.uniform(1, 3), random.uniform(-2, 3))
        self.radius = TARGET_SAFE_RADIUS
        self.alive = True
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy        
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, TARGET_SAFE_RADIUS, TARGET_SAFE_RADIUS, TARGET_SAFE_COLOR, 0)

    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x > screen_width - 10):
            return True
        elif (self.center.y > (screen_height - 10) or self.center.y < 5):
            return True
        else:
            return False
        
    def hit(self):
        self.alive = False
        return -10
    
class Bullet(FlyingObject):
    def __init__(self):
        super().__init__(0, 0, BULLET_SPEED, BULLET_SPEED)
        self.radius = BULLET_RADIUS
        self.alive = True
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BULLET_RADIUS, BULLET_COLOR)
        
    def is_off_screen(self, screen_width, screen_height):
        if (self.center.x > screen_width - 5):
            return True
        elif (self.center.y > screen_height - 5):
            return True
        else:
            return False
        
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point(0, 0)
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

        # decide if we should start a target
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
        randomNumber = random.randint(1, 50)
        
        if randomNumber < 20:
            tar1 = StandardTarget()
            self.targets.append(tar1)
        elif (randomNumber >= 20) and (randomNumber < 40):
            tar2 = StrongTarget()
            self.targets.append(tar2)
        else:
            tar3 = SafeTarget()
            self.targets.append(tar3)

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
