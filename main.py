import math
from sympy import symbols, solve
import matplotlib.pyplot as plt
import numpy as np


class Line():

    global x
    x = symbols('x', real=True)
  
    def __init__(self, m=None, b=0):
        self.m = m
        self.b = b

    def reflection_slope(self, wall):

        if self.m == None:
            tan = tan = abs(1/wall.m)
        else:
            tan = abs((self.m - wall.m)/(1 + self.m*wall.m))

        expr = tan - abs(x - wall.m)/abs(1 + x*wall.m)
        sol = solve(expr, x)

        m = sol[1] if len(sol) > 1 else sol[0]

        return m
    
    def reflection_intercept(self, wall, reflection_slope):

        if self.m == None:

            return 1 / (4*0.1)
        
        else:
            
            expr = (self.m*x + self.b) - (wall.m*x + wall.b)
            sol = solve(expr, x)

            y1 = wall.m*sol[0] + wall.b
            return y1 - reflection_slope*sol[0]


    def reflection_line(self, wall):

        m = self.reflection_slope(wall)
        b = self.reflection_intercept(wall, m)

        print(f"The slope of the new line is: {m}")
        print(f"The intercept with the Y axis is: {b}")
        print(f"The equation of the new line is: y = {m}*x + {b}")

        return Line(m, b)


m2 = None
b2 = 5
m1 = 0.2 * b2
b1 = 0.1*(b2**2) - m1*b2
original_line = Line(m2, b2)
wall = Line(m1, b1)
reflection_line = original_line.reflection_line(wall)
m3 = reflection_line.m
b3 = reflection_line.b

# Plotting

x1 = np.linspace(-20, 20, 100)
y1 = 0.1 * x1 ** 2

x = symbols('x', real=True)
expr = m3*x + b3 - 0.1*x**2

sol = solve(expr, x)

if b2 <= 0:
  y_min = m3*float(sol[0]) + b3
else:
  y_min = m3*float(sol[1]) + b3


x3 = np.linspace(float(sol[0]), float(sol[1]), 100)
y3 = m3*x3 + b3


fig = plt.figure(figsize = (8, 8))
plt.vlines(x = b2, ymin = y_min, ymax = 40, color='green')
plt.vlines(x = 0, ymin = 0, ymax = 40, color='black')
plt.hlines(y = 0, xmin = -20, xmax = 20, color='black')
plt.plot(x1, y1)
plt.plot(x3, y3, color='green')
plt.scatter(0, 2.5)
plt.show()
