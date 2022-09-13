import math

class Sym():
    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
    
    def add(self, v):
        if v != "?":
            self.n += 1
            self._has[v] = self._has.get(v,0) + 1
    
    def mid(self):
        most = -1
        for k,v in self._has.items():
            if v > most:
                mode, most = k, v
        return mode
    
    def div(self):
        def fun(p):
            return p*math.log(p, 2)
        
        e = 0
        for _,n in self._has.items():
            if n>0:
                p = n/self.n
                e -= fun(p)
        return e