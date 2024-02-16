import math
from sympy import symbols, solve
import matplotlib.pyplot as plt
import numpy as np

m1 = 1.63
b1 = -6.6434

m2 = -0.181818181818182
b2 = 8.18181818181818

class Line():
  
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def reflection_line(self, wall):
       
        x = symbols('x', real=True)
        
        tan = abs((self.m - wall.m)/(1 + self.m*wall.m))
        expr = tan - abs(x - wall.m)/abs(1 + x*wall.m)
        sol = solve(expr, x)

        m3 = sol[1] if sol[0] == m2 else sol[0]

        expr = (self.m*x + self.b) - (wall.m*x + wall.b)
        sol = solve(expr, x)

        y1 = wall.m*sol[0] + wall.b
        b3 = y1 - m3*sol[0]

        print(f"The slope of the new line is: {m3}")
        print(f"The intercept with the Y axis is: {b3}")
        print(f"The equation of the new line is: y = {m3}*x + {b3}")

        return Line(m3, b3)


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
