from sympy import symbols, solve
import numpy as np
import matplotlib.pyplot as plt


class Line():

    global x
    x = symbols('x', real=True)
  
    def __init__(self, parabole, m=None, b=0):
        self.m = m
        self.b = b
        self.parabole = parabole

    def wall(self):

        m = self.m if self.m is not None else 0
        a = self.parabole.a

        expr = a * x**2 - (m * x + self.b)
        sol = solve(expr, x)

        if m == 0:
            x_inter = self.b
        elif m > 0:
            x_inter = sol[0]
        else:
            x_inter = sol[1]

        y_inter = a * (x_inter ** 2)
        m = 2 * a * (x_inter)
        b = y_inter - m * x_inter  

        return Line(m, b)

    def get_reflection_slope(self):

        wall = self.wall()

        if self.m == None:
            tan = tan = abs(1/wall.m)
        else:
            tan = abs((self.m - wall.m)/(1 + self.m*wall.m))

        expr = tan - abs(x - wall.m)/abs(1 + x*wall.m)
        sol = solve(expr, x)

        if len(sol) <= 1:
            m = sol[0]
        else:
            print('hello')
            print(sol[0], self.m, sol[0] == self.m)
            m = sol[1] if sol[0] == self.m else sol[0]

        return m
    
    def get_reflection_intercept(self, reflection_slope):

        wall = self.wall()
        a = self.parabole.a

        if self.m == None:

            return 1 / (4 * a)
        
        else:
            
            expr = (self.m*x + self.b) - (wall.m*x + wall.b)
            sol = solve(expr, x)

            y1 = wall.m*sol[0] + wall.b
            return y1 - reflection_slope*sol[0]


    def get_reflection_line(self):

        m = self.get_reflection_slope()
        b = self.get_reflection_intercept(m)

        return Line(m, b)
    
    def plot(self):

        a = self.parabole.a

        m3 = self.get_reflection_line().m
        b3 = self.get_reflection_line().b

        m2 = self.m
        b2 = self.b

        expr = m3*x + b3 - a * x**2
        sol = solve(expr, x)

        y_min = m3 * float(sol[0]) + b3
        y_max = m3 * float(sol[1]) + b3

        # Reflection line
        x3 = np.linspace(float(sol[0]), float(sol[1]), 100)
        y3 = m3*x3 + b3

        if m2 == None:
            plt.vlines(x = b2, 
                       ymin = y_min if b2 <=0 else y_max, 
                       ymax = 40, 
                       color='green')

        else:

            x2 = np.linspace(float(sol[0]), float(sol[1]), 100)
            y2 = m2*x2 + b2

            plt.plot(x2, y2, color='green')

        plt.plot(x3, y3, color='green')