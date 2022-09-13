import math
import random
from helpers import per, the 


class Num():
    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = float("inf")
        self.hi = float("-inf")
        self.isSorted = True
        self.w = -1 if s.find("-$") else 1
    
    def nums(self):
        if not self.isSorted:
            if type(self._has) == dict:
                self._has = self._has.values()
            self._has = sorted(self._has)
            self.isSorted = True
        return self._has
    
    def add(self, v, pos = None):
        if v != "?":
            v = float(v)
            self.n += 1
            self.lo = min(self.lo,v)
            self.hi = max(self.hi,v)
            if len(self._has) < the['nums']:
                pos = 1 + len(self._has)
            elif random.random() < the['nums']/self.n:
                pos = random.randint(1,len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = float(v)
    
    def div(self):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        return per(self.nums(), 0.5)