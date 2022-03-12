"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Construct all the bricks, ball and paddle we need to play the breakout game and the rules that should
be apply in the game such as bounce back the all and bounce and remove when the ball meets the bricks
and paddle
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,x=(self.window.width-paddle_width) / 2, y=self.window.height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window.width / 2 - ball_radius, y=self.window.height / 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        self.total_bricks = brick_rows * brick_cols

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = 0

        # Initialize our mouse listeners
        onmouseclicked(self.random_start_speed)
        onmousemoved(self.move_paddle)

        # Draw bricks
        self.color_bar = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = self.color_bar[i // (brick_cols//5)]
                self.window.add(brick, x=(brick_width+brick_spacing)*i, y=brick_offset + (brick_height+brick_spacing)*j)

        # draw lives
        self.lives_icon = "❤️❤️❤️"
        self.lives = GLabel(f'{self.lives_icon}️', x=0, y=20)
        self.lives.font = '-15'
        self.window.add(self.lives)

        # other variables that need to used in methods
        self.brick_offset = brick_offset
        self.brick_height = brick_height
        self.paddle_offset = paddle_offset
        self.game_start = False
        self.ball_radius = ball_radius

    def move_paddle(self, mouse):
        # function that controls the paddle move with the ball
        if mouse.x - self.paddle.width / 2 > 0 and mouse.x < self.window.width - self.paddle.width / 2:
            self.window.add(self.paddle, x=mouse.x - self.paddle.width / 2, y=self.window.height - self.paddle_offset)

    def random_start_speed(self, mouse):
        # function that give the ball a random speed and direction to drop
        if self.game_start is False:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.game_start = True
        else:
            pass

    def x_getter(self):
        # get the speed of x direction
        return self.__dx

    def y_getter(self):
        # get the speed of y direction
        return self.__dy

    def x_bounce(self):
        # function to bounce in x direction
        self.__dx = -self.__dx

    def y_bounce(self):
        # function to bounce in x direction
        self.__dy = -self.__dy

    def check_for_collisions(self):
        # function that can check whether the ball has met the bricks or paddle
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            return self.window.get_object_at(self.ball.x, self.ball.y)
        elif self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y) is not None:
            return self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2) is not None:
            return self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        elif self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2) is not None:
            return self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
        else:
            return None

    def reduce_life(self, num_lives):
        if num_lives == 2:
            self.lives_icon = "❤️❤️"
        elif num_lives == 1:
            self.lives_icon = "❤️"
        else:
            self.lives_icon = "️"
        print(self.lives_icon)
        self.window.remove(self.lives)
        self.lives = GLabel(f'{self.lives_icon}️', x=0, y=20)
        self.lives.font = '-15'
        self.window.add(self.lives)








