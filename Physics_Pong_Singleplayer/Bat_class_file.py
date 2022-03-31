import pygame

from universal_constants_file import *

class Bat:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    # def draw_bat(self, gameDisplay):
    #     pygame.draw.rect(gameDisplay, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))
    def left_draw_bat(self, gameDisplay):
        pygame.draw.rect(gameDisplay, BLUE, pygame.Rect(self.x, self.y, BAT_WIDTH, BAT_HEIGHT))
    def right_draw_bat(self, gameDisplay):
        pygame.draw.rect(gameDisplay, RED, pygame.Rect(self.x, self.y, BAT_WIDTH, BAT_HEIGHT))
    
    @staticmethod
    def bat_movement(keys_pressed, left_bat, right_bat, ball):
        if ball.x < GAME_LEVEL: # Computer bot movement. # defined a hitting range
            if (((ball.y + BALL_SIDE/2)  < left_bat.y + BAT_HEIGHT/2) and (left_bat.y > 0 + UP_DOWN_BORDER_HEIGHT)):
                left_bat.y -= BAT_SPEED
            if ((ball.y + BALL_SIDE/2) > left_bat.y + BAT_HEIGHT/2) and (left_bat.y + BAT_HEIGHT + UP_DOWN_BORDER_HEIGHT < HEIGHT):
                left_bat.y += BAT_SPEED
        if ball.x + BALL_SIDE > GAME_LEVEL: # When bot is out of hitting range resetting the paddle 
            if (left_bat.y +  BAT_HEIGHT/2) > HEIGHT/2:
                left_bat.y -= BAT_SPEED
            elif (left_bat.y +  BAT_HEIGHT/2) < HEIGHT/2:
                left_bat.y += BAT_SPEED
            else:
                pass # (left_bat.y +  BAT_HEIGHT/2) is equal to (HEIGHT/2 - BAT_HEIGHT/2)

        if keys_pressed[pygame.K_UP] and right_bat.y > 0 + UP_DOWN_BORDER_HEIGHT:
            right_bat.y -= BAT_SPEED
        if keys_pressed[pygame.K_DOWN] and right_bat.y + BAT_HEIGHT + UP_DOWN_BORDER_HEIGHT < HEIGHT:
                right_bat.y += BAT_SPEED