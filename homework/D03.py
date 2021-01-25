import numpy as np

def pa(x):
    return 20 * (np.log10(x/20))

print(pa(20000))

def db(x):
    return 20 * np.power(10, x/20)

print(np.round(db(30)/db(50), decimals=1))
