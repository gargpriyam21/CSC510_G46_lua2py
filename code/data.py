from copy import deepcopy
from row import *
from helpers import csv, the
from cols import *


class Data():
    def __init__(self,src):
        self.cols = None
        self.rows = []
        
        if type(src) is str:
           csv(src, self.add)
        else:
            for row in src:
                self.add(row)

    def add(self, xs: Row):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = xs if type(xs) == Row else Row(xs)
            self.rows.append(row)
            for col in self.cols.x + self.cols.y:
                col.add(row.cells[col.at])
    
    def stats(self, places = 2, showCols = None, fun = None):
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

                