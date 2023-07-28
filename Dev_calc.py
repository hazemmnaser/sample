# Copyright (c) 2023 hazemmnaser 
# All rights reserved 
# By depend on free software rights, you have freedom to do anything; 
# However, you must include the copyright of the original software owner. 
# This project is licensed under the GPLv2 license, for more informations, 
# read the <<LICENSE>> file 
 
from tkinter import *
from random import random
from math import *
from eq_api import *

class Coord(Canvas):
    """
    Coordinate system for mathematics for Drawing a equations, contain a methods for draw equations.
    """

    my_id = []
    colors = ["red", "yellow", "orange", "cyan", "blue", "purple", "green", "maroon"]

    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)

        # this is the point of coordinate system o(0, 0)
        self.x0 = kwargs["width"] / 2
        self.y0 = kwargs["height"] / 2

        # first line is from o(0, 0) to w(a, 0) in the right
        self.create_line(
            self.x0, self.y0, kwargs["width"], self.y0, width=3, arrow=LAST
        )
        # 2nd line is from o(0, 0) to (0, b) in the top
        self.create_line(self.x0, self.y0, self.x0, 0, width=3, arrow=LAST)
        # 3rd line is from o(0, 0) to (0, b) in the under
        self.create_line(
            self.x0, self.y0, self.x0, kwargs["height"], width=3, arrow=LAST
        )
        # 4rd line is from o(0, 0) to (a, 0) in the left
        self.create_line(self.x0, self.y0, 0, self.y0, width=3, arrow=LAST)

        # dev elements for y axis
        for i in range(10, kwargs["width"], 20):
            self.create_line(i, kwargs["height"], i, 0)

        # dev elements for x axis
        for i2 in range(10, kwargs["height"], 20):
            self.create_line(kwargs["width"], i2, 0, i2)

    def equation_1(self, m, p):
        """
        Draw equation from one degrees on "Coord" object
        """
        # The resolve of equation in zero
        y = self.y0 - 0
        x = self.x0 + (-p / m * 20)

        # The resolve of equation in twoenty
        x1 = self.x0 + 20 * 20
        y1 = self.x0 - (20 * m + p) * 20

        # Store the lines ids in my_id attribute
        self.my_id.append(
            self.create_line(x, y, x1, y1, fill=self.colors[int(random() * 8)])
        )
    
    def equation_2(self, a, b, c):
        """Draw The function from two degrees on "Coord" object"""
        # Store the parabola peak
        self.x00 = -b/2*a
        # It is known that any function of form "f(x) = ax^2 + bx + c" -
        # where is a > 0, is decrement from "-infinity" to peak -
        # and increment from peak to "+infinity", and Vice versa.

        # "i" is an increasing variable representing the second part of parabola 
        i = self.x00
        # "j" is a decrement variable representing the first part of parabola
        j = self.x0
        # The purpose of define "f2" is for short
        f2 = func2(a, b, c)
        while True:
            # Interpretation of these four lines is as next:
            # 1.first two lines to fetch coordinates to the end of the allocated-
            # screen at second part of parabola.
            # 2.second two lines to fetch coordinates from end of allocated screen-
            # to peak
            # The coordinates are decrement and increment by one
            yn1 = self.y0 - f2.eq2(i) * 20
            yn2 = self.y0 - f2.eq2(i + 0.5) * 20
            yn3 = self.y0 - f2.eq2(j) * 20
            yn4 = self.y0 - f2.eq2(j - 0.5) * 20
            # Store lines ids in list for method my_delete
            self.my_id.append(
                    self.create_line(self.x0 + i * 20, yn1, self.x0 + (i+0.5) * 20, yn2)
            )
            self.my_id.append(
                    self.create_line(self.x0 + j * 20, yn3, self.x0 + (j-0.5) * 20, yn4)
            )
            j = j - 0.5
            i = i + 0.5
            # In case the allocated screen is finish, The loop will stop
            if i > self.y0 * 2:
                break
    def my_delete(self):
            for i in self.my_id:
                self.delete(i)
            
if __name__ == '__main__':
    root = Tk()
    root.title('Dev calc')
    coord = Coord(root, width = 500, height = 500, bg = 'ivory')
    coord.pack()
    coord.equation_2(-1, 3, 0)
    root.mainloop()
