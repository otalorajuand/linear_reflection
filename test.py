from sympy import symbols, solve
import numpy as np
from line import Line
from plot import Plot
from parabole import Parabole

def interception_line_parabole(line, parabole):

    x = symbols('x', real=True)

    m = line.m if line.m is not None else 0
    b = line.b
    a = parabole.a

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

line_test = Line(parabole=None,m=3, b=4)
parabole_test = Parabole(0.2)


x, y = interception_line_parabole(line_test, parabole_test)
print(x, y)