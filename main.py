import math
from sympy import symbols, solve
import matplotlib.pyplot as plt
import numpy as np

m1 = 1.63
b1 = -6.6434

m2 = -0.181818181818182
b2 = 8.18181818181818

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


original_line = Line(m2, b2)
wall = Line(m1, b1)
reflection_line = original_line.reflection_line(wall)
m3 = reflection_line.m
b3 = reflection_line.b

# Plotting

x1 = np.linspace(-2, 2, 100)
y1 = 0.1 * x1 ** 2

x2 = np.linspace(-2, 2, 100)
y2 = m3*x2 + b3

fig = plt.figure(figsize = (10, 5))
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()
