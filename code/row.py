from copy import deepcopy

class Row():
    def __init__(self,t):
        self.cells = t
        self.cooked = deepcopy(t)
        self.isEvaled = False
