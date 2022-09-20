from copy import deepcopy
from row import *
from helpers import csv, the
from cols import *


class Data():
    """
    Data‘ is a holder of ‘rows‘ and their sumamries (in ‘cols‘).
    """
    def __init__(self,src):
        """
        Initialize the data object with the given source.
        Arguments:
            src {str} -- The source of the data.
        Returns:
            Data -- A Data object.
        """
        self.cols = None # summaries of data
        self.rows = [] # kept data
        
        if type(src) is str:
           csv(src, self.add)
        else:
            for row in src:
                self.add(row)

    def add(self, xs: Row):
        """
       Add a row to data. Calls add() to update the cols with new values
        Arguments:
            xs {Row} -- The row to add.
        """
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = xs if type(xs) == Row else Row(xs)
            self.rows.append(row)
            for col in self.cols.x + self.cols.y:
                col.add(row.cells[col.at])
    
    def stats(self, places = 2, showCols = None, fun = None):
        """
        Print the statistics of the data object.
        Arguments:
            places {int} -- The number of decimal places to show.
            showCols {list} -- The columns to show.
            fun {function} -- The function to apply to the columns.
        """
        if not showCols:
            showCols = self.cols.y
        if not fun: 
            fun = self.cols.mid
        
        t = {}
        for col in showCols:
            v = fun(col)
            if type(v) is float:
                v = round(v, places)
            t[col.name] = v
        return t

                