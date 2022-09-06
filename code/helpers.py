import math
import re
import sys
import random

help = """
CSV :   summarized csv file
(c) 2022 Tim Menzies<timm@ieee.org> BSD-2 license

USAGE: lua seen.lua (OPTIONS]

OPTIONS:
    -e  --eg        start-up example                        = None
    -d  --dump      on test failure, exit with stack dump   = false
    -f  --file      file with csv data                      = ../data/auto93.csv
    -h  --help      show help                               = false
    -n  --nums      number of nums to keep                  = 512
    -s  --seed      random seed                             = 10019
    -S  --Seperator feild separator                         = ,
"""

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    return int(s) if s.isnumeric() else None or fun(s)

def create_the():
    the = {}
    tup_list = re.findall(r'[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help)

    for k,x in tup_list:
        the[k] = coerce(x)
    return the

the = create_the()

def per(t, p = 0.5):
    p = math.floor((p * len(t)) + 0.5) 
    return t[max(1, min(len(t), p))]

def push(t,x):
    t.append(x)
    return x

def csv(fname, fun, sep, src, s, t):
    # sep = "([^" + sep + "]+)"
    with open(fname, "r") as src:
        lines_csv = src.readlines()
        for line in lines_csv:
            row = line.split(sep)
            fun(row)

def cli(t):
    for slot, v in t.items():
        v = str(v)
        for n, x in enumerate(sys.argv):
            if x == "-"+slot[0:1] or x=="--"+slot:
                if v == "true":
                    v = "false"
                elif v == "false":
                    v = "true"
                else:
                    v = sys.argv[n+1]
        t[slot] = coerce(v)
    if t['help'] == True:
        sys.exit(print("\n"+help+"\n"))
    
    return t

def oo(t):
    if type(t) == list:
        t = list(map(lambda x: str(x), t))
        out_string = "{" + " ".join(t) + "}"
        print(out_string)
        return out_string
    else:
        out_string = o(t)
        print(out_string)
        return out_string

def o(t):
    out_string = "{"
    for k,v in t.items():
        out_string += ":" + str(k) + " " + str(v) + " "
    out_string = out_string.strip()
    out_string += "}"
    return out_string

def msg(status):
    return "PASS" if status else "FAIL"

