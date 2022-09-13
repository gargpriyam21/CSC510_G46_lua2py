import re
from num import *
from sym import *


class Cols():
    def __init__(self, names):
        self.names = names
        self.all = []
        self.kclass = None
        self.x = []
        self.y = []

        for i, name in enumerate(names):
            name = re.sub('\n', '' , name)
            col = Num(i, name) if re.search(r'^[A-Z]*', name) else Sym(i, name)
            self.all.append(col)

            if not name.endswith(':'):
                if re.search(r'[+!-]', name):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if "!$" in name:
                    self.kclass = col

