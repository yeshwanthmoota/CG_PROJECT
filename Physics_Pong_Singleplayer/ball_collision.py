import math
from universal_constants_file import *

COUNTER1 = 0
COUNTER2 = 0

def wall_ball_collision(ball):
    global COUNTER1,COUNTER2
    COUNTER2 += 1
    angle = math.degrees(ball.current_theta)
    angle = 360 - angle
    ball.current_theta = math.radians(angle)
    # print(COUNTER)
    
    if(ball.x == RESTRIANT + BAT_WIDTH) or (ball.x + BALL_SIDE == WIDTH - RESTRIANT - BAT_WIDTH):
        COUNTER1 += 1
        if(COUNTER1 == 5):
            COUNTER1 = 0
            return 10
    if (COUNTER2 == 20):
        return 10
    return 7

def bat_ball_collision(ball):
    global COUNTER2
    COUNTER2 = 0
    angle = math.degrees(ball.current_theta)
    angle = 180 - angle
    ball.current_theta = math.degrees(angle)
    # print(COUNTER2)