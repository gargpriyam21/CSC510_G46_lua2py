import re
import sys
from helpers import *
from num import *
from sym import *
from data import *
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
    for i in range(1,101):
        num.add(i)
    mid, div = int(num.mid()), num.div()
    print(mid,div)
    return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

def test_bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1,1001):
        num.add(i)
    oo(num.nums())
    return 32 == len(num._has)

def test_csv():
    global n
    n = 0

    def fun1(row):
        global n
        n = n + 1
        if n > 10 :
            return
        else:
            oo(row)

    csv('./data/auto93.csv', fun1)
    return True

def test_data():
    d = Data('./data/auto93.csv')
    for col in d.cols.y:
        oo(col)
    return True

def test_stats():
    data = Data('./data/auto93.csv')
    def div(col):
        return col.div()
    
    def mid(col):
        return col.mid()

    print("xmid", o(data.stats(2, data.cols.x, mid)))
    print("xdiv", o(data.stats(3, data.cols.x, div)))
    print("ymid", o(data.stats(2, data.cols.y, mid)))
    print("ydiv", o(data.stats(3, data.cols.y, div)))

    return True

def ALL():
    tests = dir(test_lua2py)
    tests = list(filter(lambda x: x[0:4] == "test", tests))
    tests.remove("test_lua2py")

    status = True
    for t in tests:
        print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
        kstatus = run_tests(t)
        if kstatus == False:
            status = False
    return status

def run_tests(k):
    tests = dir(test_lua2py)
    tests = list(filter(lambda x: x[0:4] == "test", tests))
    tests.remove("test_lua2py")

    if k not in tests and k != "ALL":
        return
    
    random.seed(10019)

    old = {}
    for u,v in the.items():
        old[u] = v
    
    if the['dump'] == True:
        fun =  getattr(test_lua2py, k)
        status = fun()
        print("!!!!!!", msg(status), k, status)
    else:
        try:
            fun =  getattr(test_lua2py, k)
            status = fun()
            print("!!!!!!", msg(status), k, status)
        except:
            status = False
            print("!!!!!!", msg(status), k, status)

    for u,v in old.items():
        the[u] = v