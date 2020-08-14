import pygame
import neat
import time
import os
import random
import threading
import time

# initiates pygame
pygame.init()

# FPS number
FPS = 60
# fps time clock
fps = pygame.time.Clock()
# makes a variable with the loaded grid picture as background
bg = pygame.image.load("grid.jpg")

# class for cubes
class cube(object):     # TODO: make better and usefull snake class
    w = 0

# class for the snake
class snake(object):    # TODO: make better and usefull snake class
    SIZE = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

# TODO: make a food spawning function

# TODO: make a 2D array which saves what is on every block, like is there a snake on block 0,4 or food on block 2,3 etc.

# TODO: find out a way for the snake to grow and the body to move

# the main game function
def main():
    # window size
    WIN_WIDTH = 900
    WIN_HEIGTH = 900
    # displaying the window
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))
    # game window title
    pygame.display.set_caption("Machine learning Pygame")

    # blocksize in px
    blocksize = 108
    # space between blocks in px
    block = 113
    # snake head position
    posX = 0
    posY = 0

    # game loop
    flag = True
    # initial direction
    direction = "right"
    # ingame clock
    clock = pygame.time.Clock()

    # movement countdown
    countdown = 10
    # movement boolean, if it is true the snake will move
    timetomove = False

    while flag:
        # initial screen load color
        win.fill((255, 0, 0))
        # screen color
        win.fill([255, 255, 255])
        # screen loading with the specified background image on position 0, 0
        win.blit(bg, (0, 0))


        # for every even that happens
        for event in pygame.event.get():
            print(event)

            # whenever a key gets pressed
            if event.type == pygame.KEYDOWN:
                # specifying between the possible keys pressed, possible is: left, right, up, down
                if event.key == pygame.K_RIGHT:
                    # prevents the snake from going backwards
                    if direction == "left":
                        print("cant move there")
                    else:
                        # setting the direction
                        direction = "right"
                        print("Moving right")
                        # adding 10 to the countdown, so it will immediatly set the condition for the snake to be moved
                        countdown = countdown + 10
                if event.key == pygame.K_LEFT:
                    if direction == "right":
                        print("cant move there")
                    else:
                        direction = "left"
                        print("Moving left")
                        countdown = countdown + 10
                if event.key == pygame.K_UP:
                    if direction == "down":
                        print("cant move there")
                    else:
                        direction = "up"
                        print("Moving up")
                        countdown = countdown + 10
                if event.key == pygame.K_DOWN:
                    if direction == "up":
                        print("cant move there")
                    else:
                        direction = "down"
                        print("Moving down")
                        countdown = countdown + 10

        # adding 1 to countdown after every cycle
        countdown = countdown + 1
        # after 10 cycles or having pressed a direction key
        if countdown > 10:
            # countdown gets reset to 0 for another run
            countdown = 0
            # sets the timetomove boolean to true so the snake can move
            timetomove = True
        else:
            # pauses the game for a 10th of a second until it cycles through again
            time.sleep(0.1)
            # sets the timetomove on false again if it was on true before
            timetomove = False

        # runs when the boolean is set on true
        if timetomove:
            # runs when this is the current direction
            if direction == "right":
                # basically checking that the snake is not on the edge of the screen
                if posX <= 6:
                    # letting the snake move one block in that direction
                    posX = posX + 1
                else:
                    # runs when the snake is on the edge of the screen and resets the position to the other side
                    posX = 0
            if direction == "left":
                if posX >= 1:
                    posX = posX - 1
                else:
                    posX = 7
            if direction == "up":
                if posY >= 1:
                    posY = posY - 1
                else:
                    posY = 7
            if direction == "down":
                if posY <= 6:
                    posY = posY + 1
                else:
                    posY = 0
        else:
            # for debug shows it the countdown works
            # TODO: Remove debug
            print(countdown)

        # draws the rectangle which is actually a square
        # win is that it will be drawn in the screen
        # RGB numbers
        # block is multyplied by posX,
        # block is the pixel amount until the next block spot and posX and posY is the amount of blocks to move
        # blocksize sets the size of the block
        pygame.draw.rect(win, (255, 0, 0), ((block * posX), (block * posY), blocksize, blocksize))
        # update function
        draw_window(win)
        # the fps tick
        fps.tick(FPS)

def draw_window(win):
    # graphical updates will only then be re-rendered on the screen
    pygame.display.update()
# running main and with that the game
main()