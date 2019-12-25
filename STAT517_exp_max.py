import random



class Cell:

    def __init__(self,n,low_bound,high_bound):
        self.x = 0.0;
        self.max = low_bound;
        self.round = n;
        self.low = low_bound;
        self.high = high_bound;
        
    def var(self):
        self.x = random.uniform(self.low,self.high);

    def find_max(self):
        self.var();
        if self.max<self.x:
            self.max=self.x
            
    def result(self):
        print(self.max)


    def loop(self):
        while self.round>=1:
            self.round-=1;
            self.find_max();
        self.result();

n=5;
cell=Cell(n,0,1);
cell.loop();
print(n/(n+1));
