import math
from sympy import symbols, solve

m1 = 1.63
b1 = -6.6434

m2 = -0.181818181818182
b2 = 8.18181818181818

x = symbols('x', real=True)

wall = m1*x + b1
line = m2*x + b2

tan = abs((m2 - m1)/(1 + m2*m1))

# solving for the slope of the new line

expr = tan - abs(x - m1)/abs(1 + x*m1)
sol = solve(expr, x)

if sol[0] == m2:
  m3 = sol[1]
  
else:
  m3 = sol[0]

print(f"The slope of the new line is: {m3}")

# solving for the intercept of the new line
expr = line - wall
sol = solve(expr, x)

y1 = m1*sol[0] + b1
b3 = y1 - m3*sol[0]

print(f"The intercept with the Y axis is: {b3}")
print(f"The equation of the new line is: y = {m3}*x + {b3}")
