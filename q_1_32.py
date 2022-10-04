"""
Tal Lerner
Python Programming in Context
Try It Out
Page 32
"""

from turtle import *

def draw_spiral(max_side):
    """
    Draw a spiral. It will draw a line each time a different length
    and then turn 80 and repeat.
    """
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(80)

# This calls the function:
draw_spiral(100)