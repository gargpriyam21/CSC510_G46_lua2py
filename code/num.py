import math
import random
from helpers import per, the 


class Num():
    """
    'Num' is a class for 'Columns' that hold numeric attributes.
    """
    def __init__(self, c = 0, s = ""):
        """
        Initialize the Num object with the given column number and name.
        Arguments:
            c {int} -- Column number.
            s {str} -- Column name.
        Returns:
            Num -- A Num object.
        """
        self.n = 0 # items seen
        self.at = c # column position
        self.name = s # column name
        self._has = {} # kept data
        self.lo = float("inf") # lowest seen
        self.hi = float("-inf") # highest seen
        self.isSorted = True # no updates since last sort
        self.w = -1 if s.find("-$") else 1
    
    def nums(self):
        """
        Return the numbers in the Num object in sorted order.
        Returns:
            list -- The numbers in the Num object.
        """
        if not self.isSorted:
            if type(self._has) == dict:
                self._has = self._has.values()
            self._has = sorted(self._has)
            self.isSorted = True
        return self._has
    
    def add(self, v, pos = None):
        """
        Add a value to the Num object.
        Reservoir sampler. Keep at most 'the.nums' numbers
        Arguments:
            v {float} -- The value to add.
            pos {int} -- The position to add the value.
        """
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
        """
        Return the diversity of the Num object.
        Returns:
            float -- The diversity of the Num object.
        """
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1)) / 2.58

    def mid(self):
        """"
        Return the median of the Num object.
        Returns:
            float -- The median of the Num object.
        """
        return per(self.nums(), 0.5)