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

def wall(line, parabole):

    a = parabole.a
    x_inter, y_inter = interception_line_parabole(line, parabole)

    m = 2 * a * (x_inter)
    b = y_inter - m * x_inter  

    return Line(m=m, b=b)

def get_reflection_slope(line, wall):

    x = symbols('x', real=True)

    if line.m == None:
        tan = tan = abs(1 / wall.m)
    else:
        tan = abs((line.m - wall.m)/(1 + line.m*wall.m))

    expr = tan - abs(x - wall.m)/abs(1 + x*wall.m)
    sol = solve(expr, x)

    if len(sol) <= 1:
        m = sol[0]
    else:
        m = sol[1] if sol[0] == line.m else sol[0]

    return m

def get_reflection_intercept(line, wall, parabole, reflection_slope):

    x = symbols('x', real=True)
    a = parabole.a

    if line.m == None:

        return 1 / (4 * a)
    
    else:
        
        expr = (line.m * x + line.b) - (wall.m * x + wall.b)
        sol = solve(expr, x)

        y1 = wall.m * sol[0] + wall.b
        return y1 - reflection_slope*sol[0]
    
def get_reflection_line(line, wall, parabole):

    m = get_reflection_slope(line = line, 
                             wall = wall)
    
    b = get_reflection_intercept(line = line, 
                                 wall = wall, 
                                 parabole = parabole, 
                                 reflection_slope = m)

    return Line(m=m, b=b)

line_test = Line(m=3, b=4)
parabole_test = Parabole(a=0.2)
wall_test = wall(line=line_test, parabole=parabole_test)
reflection_line_test = get_reflection_line(line = line_test,
                                           wall = wall_test,
                                           parabole = parabole_test)
