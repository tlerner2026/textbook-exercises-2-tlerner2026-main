"""
Tal Lerner
Python Programming in Context
Try It Out
Page 32
"""

from turtle import *

def draw_spiral(max_side):
    """
    Draw Rectangular Spiral. Draw a segment and also rotate right with the same number.
    """
    for side_length in range(1, max_side + 1, 5):
        forward(side_length)
        right(side_length)

# Call your function here:
draw_spiral(100)