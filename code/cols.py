import re
from num import *
from sym import *


class Cols():
    """
    'Columns' Holds of summaries of columns.
    Columns are created once, then may appear in multiple slots.
    """
    def __init__(self, names):
        """
        Initialize the columns object with the given names.
        Arguments:
            names {list} -- List of column names.
        Returns:
            Cols -- A Cols object.
        """
        self.names = names # all column names
        self.all = [] # all the columns (including the skipped ones)
        self.kclass = None # the single dependent klass column (if it exists)
        self.x = [] # independent columns (that are not skipped)
        self.y = [] # dependent columns (that are not skipped)

        for i, name in enumerate(names):
            name = re.sub('\n', '' , name)
            col = Num(i, name) if re.search(r'^[A-Z]*', name) else Sym(i, name) # Numerics start with Uppercase.
            self.all.append(col)

            if not name.endswith(':'):
                if re.search(r'[+!-]', name):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if "!$" in name:
                    self.kclass = col

