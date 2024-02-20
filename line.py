from sympy import symbols, solve
import numpy as np
import matplotlib.pyplot as plt


class Line():

    global x
    x = symbols('x', real=True)
  
    def __init__(self, m=None, b=0):
        self.m = m
        self.b = b

    def __str__(self):
        return f'The line has a slope of {self.m} and an intercept of {self.b}'

    def __repr__(self):
        return f'Line(m=\'{self.m}\', b={self.b})'