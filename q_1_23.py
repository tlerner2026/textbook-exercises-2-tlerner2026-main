"""
Tal Lerner
Python Programming in Context
Try It Out
Page 28
"""

from turtle import *

def draw_half_square(side_length):
    """
    Draw a half square. From were the turtle is facing it will make a rectangle
    that is longer on the top than the bottom. It will end in the same place and
    position were it started.
    
    side_length is the basic length of each side.
    """
#draw long side
    forward(2*side_length)
    right(90)
#draw short side    
    forward(side_length)
    right(90)
#draw long side
    forward(2*side_length)
    right(90)
#draw short side
    forward(side_length)
    right(90)
    ##########################################

# This code calls the function:
draw_half_square(50)
