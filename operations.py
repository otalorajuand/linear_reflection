from sympy import symbols, solve
from line import Line
from parabole import Parabole

class Operations():

    def __init__(self, line, parabole):
        self.line = line
        self.parabole = parabole
        self.wall = self.get_wall()
        self.reflection_line = self.get_reflection_line()

    def interception_line_parabole(self):

        x = symbols('x', real=True)

        m = self.line.m if self.line.m is not None else 0
        b = self.line.b
        a = self.parabole.a

        expr = a * x**2 - (m * x + b)
        sol = solve(expr, x)

        if m == 0:
            x_inter = b
        elif m > 0:
            x_inter = sol[0]
        else:
            x_inter = sol[1]

        y_inter = a * (x_inter ** 2)

        return x_inter, y_inter

    def get_wall(self):

        a = self.parabole.a
        x_inter, y_inter = self.interception_line_parabole()

        m = 2 * a * (x_inter)
        b = y_inter - m * x_inter  

        return Line(m=m, b=b)

    def get_reflection_slope(self):

        x = symbols('x', real=True)

        if self.line.m == None:
            tan = tan = abs(1 / self.wall.m)
        else:
            tan = abs((self.line.m - self.wall.m)/(1 + self.line.m*self.wall.m))

        expr = tan - abs(x - self.wall.m)/abs(1 + x*self.wall.m)
        sol = solve(expr, x)

        if len(sol) <= 1:
            m = sol[0]
        else:
            m = sol[1] if sol[0] == self.line.m else sol[0]

        return m

    def get_reflection_intercept(self):

        x = symbols('x', real=True)
        a = self.parabole.a
        m = self.get_reflection_slope()

        if self.line.m == None:

            return 1 / (4 * a)
        
        else:
            
            expr = (self.line.m * x + self.line.b) - (self.wall.m * x + self.wall.b)
            sol = solve(expr, x)

            y1 = self.wall.m * sol[0] + self.wall.b
            return y1 - m*sol[0]
        
    def get_reflection_line(self):

        m = self.get_reflection_slope()
        b = self.get_reflection_intercept()

        return Line(m=m, b=b)

