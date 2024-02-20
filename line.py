from sympy import symbols, solve
import numpy as np
import matplotlib.pyplot as plt


class Line():

    global x
    x = symbols('x', real=True)
  
    def __init__(self, m=None, b=0):
        self.m = m
        self.b = b

    """
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

    """

    def __str__(self):
        return f'The line has a slope of {self.m} and an intercept of {self.b}'

    def __repr__(self):
        return f'Line(m=\'{self.m}\', b={self.b})'