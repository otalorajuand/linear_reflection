from sympy import symbols, solve


class Line():

    global x
    x = symbols('x', real=True)
  
    def __init__(self, m=None, b=0):
        self.m = m
        self.b = b

    def wall(self):

        m = self.m if self.m is not None else 0

        expr = 0.1 * x**2 - (m * x + self.b)
        sol = solve(expr, x)

        if m == 0:
            x_inter = self.b
        elif m > 0:
            x_inter = sol[0]
        else:
            x_inter = sol[1]

        y_inter = 0.1 * (x_inter ** 2)
        m = 0.2 * (x_inter)
        b = y_inter - m * x_inter  

        return Line(m, b)



    def reflection_slope(self):

        wall = self.wall()

        if self.m == None:
            tan = tan = abs(1 / wall.m)
        else:
            tan = abs((self.m - wall.m)/(1 + self.m*wall.m))

        expr = tan - abs(x - wall.m)/abs(1 + x*wall.m)
        sol = solve(expr, x)

        m = sol[0]

        return m
    
    def reflection_intercept(self, reflection_slope):

        wall = self.wall()

        if self.m == None:

            return 1 / (4*0.1)
        
        else:
            
            expr = (self.m*x + self.b) - (wall.m*x + wall.b)
            sol = solve(expr, x)

            y1 = wall.m*sol[0] + wall.b
            return y1 - reflection_slope*sol[0]


    def reflection_line(self):

        m = self.reflection_slope()
        b = self.reflection_intercept(m)

        return Line(m, b)