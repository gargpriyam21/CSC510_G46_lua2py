import re
import sys
from helpers import *
from num import *
from sym import *
from test import test_lua2py
import random

def test_the():
    oo(the)
    return True

def test_sym():
    sym = Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    oo({"mid":mode, "div":entropy})
    return mode=="a" and 1.37 <= entropy and entropy <=1.38

def test_num():
    num = Num()
    for i in range(1,100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid,div)
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def test_bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1,1000):
        num.add(i)
    oo(num.nums())
    return 32 == len(num._has)

