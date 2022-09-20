import math

class Sym():
    """
    'Sym' is a class for 'Columns' that hold symbolic attributes.
    """
    def __init__(self, c = 0, s = ""):
        self.n = 0 # items seen
        self.at = c # column position
        self.name = s # column name
        self._has = {} # kept data
    
    def add(self, v):
        """
        Add a value to the Sym object.
        Arguments:
            v {str} -- The value to add.
        """
        if v != "?":
            self.n += 1
            self._has[v] = self._has.get(v,0) + 1
    
    def mid(self):
        """
        Return the most common value in the Sym object.
        Returns:
            str -- The most common value in the Sym object.
        """
        most = -1
        for k,v in self._has.items():
            if v > most:
                mode, most = k, v
        return mode
    
    def div(self):
        """
        Return the entropy of the Sym object.
        Returns:
            float -- The entropy of the Sym object.
        """
        def fun(p):
            """
            Inner function to calculate p*log(p)
            Arguments:
                p {float} -- The probability of a value.
            Returns:
                float -- The p*log(p) of the value.
            """
            return p*math.log(p, 2)
        
        e = 0
        for _,n in self._has.items():
            if n>0:
                p = n/self.n
                e -= fun(p)
        return e