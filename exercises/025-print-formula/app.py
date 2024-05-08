import math

def print_formula(d):
    c = 50
    h = 30
    Q = math.sqrt((2*c*d)/h)
    if Q - int(Q) < 0.5:
        return math.floor(Q)
    else:
        return math.ceil(Q)

print_formula(100)