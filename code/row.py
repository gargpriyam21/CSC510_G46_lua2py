from copy import deepcopy

class Row():
    """
    ‘Row‘ holds one record of data.
    """
    def __init__(self,t):
        """
        Initialize the row object with the given list.
        Arguments:
            t {list} -- The list to initialize the row with.
        Returns:
            Row -- A Row object."""
        self.cells = t # one record
        self.cooked = deepcopy(t) # used if we discretize data
        self.isEvaled = False # true if y−values evaluated
