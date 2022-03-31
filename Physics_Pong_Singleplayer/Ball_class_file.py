import pygame
import random
import math

from universal_constants_file import *
from ball_collision import *


class Ball:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_ball_speed = BALL_SPEED
        self.current_theta = 0


    def ball_movement(self):
        # points scored
        # for restricting position left and right
        if self.x <= RESTRIANT - BALL_SIDE: # off left side of screen 
            return 1
        elif self.x >= WIDTH - RESTRIANT + BALL_SIDE: #off right side of screen
            return -1

        # wall collisions
        # for restricting position up and down
        if(self.y < 0 + UP_DOWN_BORDER_HEIGHT): # UP_WALL
            self.y = UP_DOWN_BORDER_HEIGHT
            code = wall_ball_collision(self)
            return code
        elif(self.y + BALL_SIDE > HEIGHT -UP_DOWN_BORDER_HEIGHT): #DOWN_WALL
            self.y = HEIGHT - UP_DOWN_BORDER_HEIGHT - BALL_SIDE
            code = wall_ball_collision(self)
            return code  
        self.x += self.current_ball_speed * round(math.cos(self.current_theta),1)
        self.y += self.current_ball_speed * round(math.sin(self.current_theta),1)
        return 0


        
    def draw_ball(self, gameDisplay):
        if (self.x <= RESTRIANT - BALL_SIDE) and (self.x >= WIDTH - RESTRIANT + BALL_SIDE): # off left side of screen 
            pass # Making Ball dissappear off the screen
        else:
            pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(self.x, self.y, BALL_SIDE, BALL_SIDE))
            # r = (BALL_SIDE) / 2
            # g = math.sqrt(2)
            # pygame.draw.circle(gameDisplay, WHITE, (int(self.x + r*g), int(self.y + r*g)), int(r)) # To print out a circle ball.



    def initial_ball_movement(self): # To provide the initial push to the ball just after a point scored or at the beginning
        self.x = WIDTH/2 - BALL_SIDE/2 # x - position reset
        self.y = HEIGHT/2 - BALL_SIDE/2 # y - position reset
        degrees_1 = random.randrange(60, 121, 20)
        degrees_2 = random.randrange(240, 301, 20)
        degrees = random.choice([degrees_1, degrees_2])
        theta = math.radians(degrees)
        self.current_ball_speed = BALL_SPEED
        self.current_theta = theta
        self.ball_movement()