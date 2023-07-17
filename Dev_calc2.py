from tkinter import *
from random import random
from math import *

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
        Draw equation from one degrees on Coord object
        """
        # The resolve of fraction in zero
        y = self.y0 - 0
        x = self.x0 + (-p / m * 20)

        # the resolve of fraction in twoenty
        x1 = self.x0 + 20 * 20
        y1 = self.x0 - (20 * m + p) * 20

        # store the lines ids in my_id attribute
        self.my_id.append(
            self.create_line(x, y, x1, y1, fill=self.colors[int(random() * 8)])
        )
    
    def equation_2(self, a, b, c):
        delta = b**2 - 4 * a * c
        if delta > 0:
            self.e2x1 = x1 = (-b - sqrt(delta)) / 2 * a
            self.e2x2 = x2 = (-b + sqrt(delta)) / 2 * a
            y1 = 0
            y2 = 0
            x00 = -b / 2 * a
            y00 = a * x00**2 + b*x00 + c
            self.my_id.append(
                    self.create_line(self.x0 - x00 * 20, self.y0 - y00 * 20, 
                                     self.x0 - (x1-1) * 20, self.y0 - (y1-1) * 20)
            )
            self.my_id.append(
                    self.create_line(self.x0 - x00 * 20, self.y0 - y00 * 20,
                                     self.x0 - x2 * 20, self.y0 - y2 * 20)
            )
        elif delta == 0:
            self.e2x0 = x00 = -b / 2 * a
            sty = a * x00**2 + b*x00 + c
            sty2 = a * (x00 + 0.5) ** 2 + b*(x00+0.5) + c
            self.my_id.append(
                self.create_line(self.x0 - x00 * 20, self.y0 -sty * 20, 
                                 self.x0 -(x00 + 1)  * 20, self.y0 - sty2 * 20)
            )
            self.my_id.append(
                self.create_line(self.x0 + x00 * 20, self.y0 -sty * 20,
                                 self.x0 + (x00 + 1) * 20, self.y0 - sty2 * 20)
            )

        else:
            raise Exception('Can not solve equation in |R')
        i = 0
        while True:
            i = (i + 0.5)
            yn1 = self.y0 - (a*i**2 + i*b + c) * 20
            yn2 = self.y0 - (a*(i+1)**2 + (i+1)*b + c) * 20
            self.my_id.append(
                    self.create_line(self.x0 - i * 20, yn1, self.x0 - (i+1) * 20, yn2)
            )
            self.my_id.append(
                    self.create_line(self.x0 + i * 20, yn1, self.x0 + (i+1) * 20, yn2)
            )

            if i >= 2 * self.x0:
                break
    def my_delete(self):
        for i in self.my_id:
            self.delete(i)


if __name__ == "__main__":
    root = Tk()
    c = Coord(height = 500, width = 500, bg="ivory")
    c.pack()
    c.equation_2(2,-8, -1)
    root.mainloop()
