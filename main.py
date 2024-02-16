import math
from sympy import symbols, solve
import matplotlib.pyplot as plt
import numpy as np
from line import Line


m2 = 2
b2 = 30
m1 = -2
b1 = -10
original_line = Line(m2, b2)
wall = Line(m1, b1)
reflection_line = original_line.reflection_line(wall)
m3 = reflection_line.m
b3 = reflection_line.b

# Plotting
"""
class Plot():

    def __init__(self, )
"""

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
