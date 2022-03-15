"""
Name: Yu-Ju Fang
Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Construct a breakout game which is played by controlling a paddle to bounce the
ball in order to destroy all the bricks in screen. if the ball drop out of the screen
player will lose one live, each player only have three lives to win the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# background music
from tkinter import *
import tkinter.font as font
import pygame

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts

window = Tk()
window.title('Breakout')


def start_game():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES
    game_running = True

    # Add animation loop here!
    while game_running:
        pause(FRAME_RATE)

        # click to game start
        if graphics.game_start is True:
            graphics.ball.move(graphics.x_getter(), graphics.y_getter())

        # bounce if ball collide with left or right wall or top of the wall
        if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.x_bounce()
        if graphics.ball.y < 0:
            graphics.y_bounce()

        # if collide with paddle bounce back, if collide with bricks remove and bounce back
        if graphics.check_for_collisions() is not None:
            graphics.y_bounce()
            if graphics.check_for_collisions() is not graphics.paddle or graphics.check_for_collisions() is not graphics.lives:
                graphics.window.remove(graphics.check_for_collisions())
                graphics.total_bricks -= 1

        # if ball pass lower than the height of the window reduce a life a click to restart
        if graphics.ball.y > graphics.window.height:
            num_lives -= 1
            graphics.reduce_life(num_lives)
            graphics.window.add(graphics.ball, x=graphics.window.width / 2 - graphics.ball_radius,
                                y=graphics.window.height / 2 - graphics.ball_radius)
            graphics.game_start = False
            if num_lives == 0:
                game_running = False

        # check whether all bricks are remove
        if graphics.total_bricks == 0:
            game_running = False


def main():
    canvas = Canvas(window,width=500, height=500, highlightthickness=0, bg='orange')
    canvas.create_text(250, 250, text='Welcome to the Breakout game', fill='black', font=('微軟正黑', 30, 'bold'))
    canvas.grid(column=1, row=1, rowspan=2)
    start = Button(window, text='Start', command=start_game, bg='orange')
    start.grid(column=1, row=2)
    window.mainloop()


if __name__ == '__main__':
    main()
