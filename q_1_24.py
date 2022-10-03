"""
Tal Lerner
Python Programming in Context
Try It Out
Page 28
"""

from turtle import *

def draw_rectangle(width, height):
    """
    Draw a rectangle. Draw a line going forward from in the direction the pen
    is facing. Turn right and draw the height. Then, repeat the code again to 
    complete the rectangle
    """
    ############################################
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    ##########################################

# This code calls the function:
draw_rectangle(50, 300)
