from line import Line
from plot import Plot
from parabole import Parabole
from operations import Operations


# Plotting

if __name__ == "__main__":

    intercept = 10
    slope = None

    parabole = Parabole(a=0.1)
    line = Line(m = slope, b = intercept)
    operations = Operations(line=line, parabole=parabole)
    wall = operations.wall
    reflected_line = operations.reflection_line


    plot = Plot(original_line=line, 
                reflection_line=reflected_line, 
                parabole=parabole)
    #plot.show()
    plot.animation()