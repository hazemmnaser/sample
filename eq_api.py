import math as mh

class MathError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
class FeatureWarning(Warning):
    def __init__(self, msg):
        Warning.__init__(self, msg)
        self.msg = msg

# I mean mathematics functions not prgramming functions!
class func1(object):
    def __init__(self, m, p):
        self.m = m
        self.p = p
        self.roots = -(p/m)
        self.derivative = str(m)
        self.integral = str(m/2) + 'x^2 + ' + f'{p}x + c'
        self.std_form = f'{m}x + {p}'
    def eq1(self, x = None, y = None):
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
        self.a     = a
        self.b     = b
        self.c     = c
        self.delta = b**2 - 4 * a * c
        if self.delta > 0:
            self.roots = {'x1': ( -b - mh.sqrt(self.delta) ) /2*a, 'x2': ( -b + mh.sqrt(self.delta) ) / 2*a}
        elif self.delta == 0:
            self.roots = -b / 2 * a
        else:
            raise FeatureWarning('The complex numbers and complex roots isn\'t support now')
        self.derivative = str(2 * a) + f'x + {b}'
        self.integral   = str(a / 2) + 'x^3 + ' + str(b / 2) + 'x^2 + ' + f'{c}x + c'
        self.std_form   = f'{a}x^2 + {b}x + {c}'
    def eq2(self, x = None, y = None):
        if x is None and y is None:
            return self.std_form
        elif x is not None and y is None:
            return self.a * x ** 2 + self.b * x + self.c
        elif x is None and y is not None:
            delta2 = self.b**2 - 4 * self.a * (self.c - y)
            if delta2 > 0:
                return {'x1': ( -self.b - mh.sqrt(delta2) ) / 2 * self.a, 'x2': ( -self.b + mh.sqrt(delta2) ) / 2 * self.a }
            elif delta2 == 0:
                return -self.b / 2 * self.a
            else:
                raise FeatureWarning('Complex numbers and complex roots isn\'t support now')

roots      = lambda a: a.roots
derivative = lambda a: a.derivative
integral   = lambda a: a.integral
