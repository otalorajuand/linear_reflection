from sympy import symbols, solve


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

        m = sol[0] if sol[1] == self.m else sol[1]

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