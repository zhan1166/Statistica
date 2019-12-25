import random
import matplotlib.pyplot as plt
import math


##plot exponential distribution
##f(x) = exp(-x); 0<x<inf

##F(x) = U = 1-exp(-x);
##x = -log(-U);

class Cell:

    def __init__(self):
        self.u=0.0;
        self.x = 0.0;
##        self.low = low_bound;
##        self.high = high_bound;
        
    def var(self):
        self.u = random.uniform(0,1);
        self.x = -1*math.log(1-self.u);
        print(self.x);

cell = Cell();
cell.var();
        
        
