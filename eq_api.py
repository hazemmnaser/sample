# Copyright (c) 2023 hazemmnaser
# All rights reserved
# By depend on free software rights, you have freedom to do anything;
# However, you must include the copyright of the original software owner.
# This project is licensed under the GPLv2 license, for more informations,
# read the <<LICENSE>> file

import math as mh

# This error has raised when found unlogic expression

class MathError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

# This warning has occured when found un supported expression like complex numbers
class FeatureWarning(Warning):
    def __init__(self, msg):
        Warning.__init__(self, msg)
        self.msg = msg

# I mean mathematics functions, not prgramming functions!
class func1(object):
    """object type mathematical functions, contain methods for other mathematical using."""
    def __init__(self, m, p):
        # Store m and p
        self.m = m
        self.p = p
        # Store roots
        self.roots = -(p/m)
        # Store derivative function
        self.derivative = str(m)
        # Store integral function
        self.integral = str(m/2) + 'x^2 + ' + f'{p}x + c'
        # Store the regulare expression
        self.std_form = f'{m}x + {p}'
    def eq1(self, x = None, y = None):
    """Find the roots in points and emulation matheamtical functions f(x) = mx + p"""
        if x is None and y is None:
            return self.std_form
        elif x is not None and y is None:
            return self.m * x + self.p
        elif x is None and y is not None:
            return (y - self.p)/self.m
        else:
            raise MathError('You can set ether x or y only.')

class func2(object):
    def __init__(self, a, b, c):
        # Store arguments
        self.a     = a
        self.b     = b
        self.c     = c
        # Store the discriminant of equation
        self.delta = b**2 - 4 * a * c
        # In case delta bigger than zero there are two roots
        if self.delta > 0:
            self.roots = {'x1': ( -b - mh.sqrt(self.delta) ) /2*a, 'x2': ( -b + mh.sqrt(self.delta) ) / 2*a}
        # In case delta equals zero a single root is the peak of parabola 
        elif self.delta == 0:
            self.roots = -b / 2 * a
        # In case delta lower than a zero, there are two complex roots, but not supported until now :-(
        else:
            raise FeatureWarning('The complex numbers and complex roots isn\'t support now')
        # Store derivative
        self.derivative = str(2 * a) + f'x + {b}'
        # Store unlimited integration
        self.integral   = str(a / 2) + 'x^3 + ' + str(b / 2) + 'x^2 + ' + f'{c}x + c'
        # Store the regular equation
        self.std_form   = f'{a}x^2 + {b}x + {c}'
    def eq2(self, x = None, y = None):
        """Find the roots in points and emulation matheamtical functions f(x) = ax^2 + bx + c"""
        if x is None and y is None:
            return self.std_form
        elif x is not None and y is None:
            # Substitute x into the function
            return self.a * x ** 2 + self.b * x + self.c
        elif x is None and y is not None:
            # Resolve the equation at point y
            delta2 = self.b**2 - 4 * self.a * (self.c - y)
            # Same explination from line 49 to line 55
            if delta2 > 0:
                return {'x1': ( -self.b - mh.sqrt(delta2) ) / 2 * self.a, 'x2': ( -self.b + mh.sqrt(delta2) ) / 2 * self.a }
            elif delta2 == 0:
                return -self.b / 2 * self.a
            else:
                raise FeatureWarning('Complex numbers and complex roots isn\'t support now')

# Only some macros :-)
roots      = lambda a: a.roots
derivative = lambda a: a.derivative
integral   = lambda a: a.integral
