import arcade

class DemoApp(arcade.Window):
    """
    This class defines the demo application.
    It produces a rectangle on the screen.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        
        arcade.set_background_color(arcade.color.WHITE)
        
    def on_draw(self):
        """
        Called every time we need to draw the window
        :return
        """
        arcade.start_render()
        
        arcade.draw_rectangle_filled(100, 100, 50, 20, arcade.color.BLUE)
        
    def update(self, delta_time: float):
        """
        The purpose of this method is to move everything foward.
        :param delta_time:
        :return:
        """
        pass

window = DemonApp(500, 400)
arcade.run()