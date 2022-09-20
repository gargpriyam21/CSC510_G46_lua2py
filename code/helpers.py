import math
import re
import sys
import random

# The global variable help having the default values of the command line arguments.
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
    """
    Coerce a string to a number, if possible.
    Arguments:
        s {str} -- The string to coerce.
    Returns:
        int/float/str -- The coerced value.
    """

    def fun(s1):
        """
        Helper inner function to rerurn the coerced value.
        Arguments:
            s1 {str} -- The string to coerce.
        Returns:
            int/float/str -- The coerced value.
        """

        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    
    return int(s) if s.isnumeric() else None or fun(s)

def create_the():
    """
    Create the global variable 'the'.
    Returns:
        dict -- The global variable 'the'.
    """
    the = {}
    tup_list = re.findall(r'[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help)

    for k,x in tup_list:
        the[k] = coerce(x)
    return the

# The global variable 'the' having the default values of the command line arguments.
the = create_the()

def per(t, p = 0.5):
    """
    Return the p percentile of the list t.
    Arguments:
        t {list} -- The list of values.
    Keyword Arguments:
        p {float} -- The percentile to return. (default: {0.5})
    Returns:
        float -- The p percentile of the list t.
    """
    p = math.floor((p * len(t)) + 0.5) 
    return t[max(0, min(len(t), p)-1)]

def push(t,x):
    """
    Push a value onto a list.
    Arguments:
        t {list} -- The list to push onto.
        x {any} -- The value to push.
    Returns:
        list -- The list with the value pushed.
    """
    t.append(x)
    return x

def csv(fname, fun, sep=','):
    """
    Read a csv file and apply a function to each line.
    Arguments:
        fname {str} -- The name of the file to read.
        fun {function} -- The function to apply to each line.
    Keyword Arguments:
        sep {str} -- The separator to use. (default: {','})
    """
    # sep = "([^" + sep + "]+)"
    with open(fname, "r") as src:
        lines_csv = src.readlines()
        for line in lines_csv:
            row = line.split(sep)
            fun(row)

def cli(t):
    """
    Parse the command line arguments.
    Arguments:
        t {dict} -- The dictionary to store the arguments in.
    Returns:
        dict -- The dictionary with the arguments stored.
    """
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
    """
    Print the object t.
    Arguments:
        t {dict/list/str} -- The object to print.
    Returns:
        str -- The string representation of the object.
    """
    if type(t) == list:
        t = list(map(lambda x: str(x), t))
        out_string = "{" + " ".join(t)[:-1] + "}"
        print(out_string)
        return out_string
    elif type(t) == dict:
        out_string = o(t)
        print(out_string)
        return out_string
    else:
        obj_dict = vars(t)
        del obj_dict['_has']
        out_string = (o(vars(t)))
        print(out_string)
        return out_string

def o(t):
    """
    Return the string representation of the object t embedded in {}.
    Arguments:
        t {dict} -- The object to print.
    Returns:
        str -- The string representation of the object.
    """
    out_string = "{"
    for k,v in t.items():
        out_string += ":" + str(k) + " " + str(v) + " "
    out_string = out_string.strip()
    out_string += "}"
    return out_string

def msg(status):
    """
    Print a status message.
    Arguments:
        status {str} -- The status message to print.
    Returns:
        str -- The status message.
    """
    return "PASS" if status else "FAIL"

