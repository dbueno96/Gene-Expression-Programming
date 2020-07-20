import math

def add(x,y): 
    try: 
        return float(x)+float(y) 
    except OverflowError: 
        return 10e6
def sub(x,y): 
    if abs(x)==float('inf') and abs(y)==float('inf'):
        return 0
    else:
        try: 
            return float(x)-float(y)
        except OverflowError: 
            return 10e6

def mult(x,y):
    if (x== float('inf') or x==float('-inf')) and y ==0: 
        return 0
    elif x==0 and (x==float('-inf') or y == float('inf')):
        return 0 
    try: 
        return float(x)*float(y)
    except OverflowError: 
        if (x and not y) or (not x and y):
            return -1*10e6
        else: 
            return 10e6
def div(x,y): 
    if (x== float('inf') or x==float('-inf')) and (y== float('inf') or y==float('-inf')):
        return 0
    if y != 0:
        try: 
            return(x//y)
        except OverflowError: 
            return 10e6
    else:
        return 10e6
def absolut(x):
    return abs(x)


def module(x,y):
    if x == float('inf') or x==float('-inf'):
        return x
    elif y==  float('inf') or y==float('-inf'):
        return 0
    if y != 0:
        try: 
            return float(x)% float(y)
        except OverflowError: 
            return 0
    else : 
        return x

def sqrt(x): 
    if x <0: 
        try: 
            return math.sqrt(-x)
        except OverflowError: 
            return 10e6
    else:
        try: 
            return math.sqrt(x)
        except OverflowError: 
            return 10e6

def max_val(x,y):
    return max(x,y)
def min_val(x,y):
    return min(x,y)

def sqr(x): 
    try: 
        return math.pow(x,2)
    except OverflowError: 
            return 10e6

def sin(x): 
    if x== float('inf') or x==float('-inf'): 
        return 0
    else:
        try: 
            return 10*math.sin(x)
        except OverflowError: 
            return 0

def cos(x): 
    if x== float('inf') or x==float('-inf'): 
        return 0
    else:
        try:
            return 10*math.cos(x)
        except OverflowError: 
            return 0

def atan(x):
    try: 
        return 10*math.atan(x)
    except OverflowError: 
        return 0
    
def identity(x): 
    return x



def cond2(x,y,z,w): 
    if x>y : 
        return z
    else: 
        return w

def cond3(x,y,z,w):
    if x < y :
        return z
    else : 
        return w
def cond4 (x,y,z,w): 
    if x == y: 
        return z
    else:
        return w
    
def cond5(x,y,z,w): 
    if x!=y: 
        return z
    else: 
        return w

def literal(i): 
    return i



OPERATORS = ((literal, 0,'#'),      #0
             (add, 2, '+'),         #1
             (sub, 2, '-'),         #2
             (mult,2, '*'),         #3
             (div, 2, '/'),         #4
             (absolut, 1, '||'),    #5
             (module, 2, '%'),      #6
             (sqrt, 1, 'Sqrt'),     #7
             (max_val, 2, 'max'),   #8
             (min_val, 2, 'min'),   #9
             (sqr, 1, '^2'),        #10
             (identity, 1, 'I'),    #11
             (sin, 1, 'sin'),       #12
             (cos, 1, 'cos'),       #13
             (atan,1, 'atan'),      #14
             (cond2, 4, 'if >'),    #15
             (cond3, 4, 'if <'),    #16
             (cond4, 4, 'if =='),   #17
             (cond5, 4, 'if !='))   #18

