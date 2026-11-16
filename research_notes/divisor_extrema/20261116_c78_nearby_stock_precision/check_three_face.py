"""Exact cube-phase checks for the critical-window cubic examples."""
from fractions import Fraction as F
from itertools import product
import json

def count_phases(k):
    # L=1/k. All bounding-box vertices are at lattice multiples of 1/k.
    single=0
    for i,j,z in product(range(k), repeat=3):
        coincident=False
        for a,b in product(range(-k,k+1), repeat=2):
            if (a or b) and 0<=i+a<k and 0<=j+b<k and 0<=z+a+b<k:
                coincident=True
                break
        single+=not coincident
    assert single==2
    return F(single,k**3)

def degrees():
    base = {(15,42),(6,51)}
    numerator = base | {(a+15,b) for a,b in base}
    denominator = {(0,0),(51,9),(66,9),(117,18)}
    n,d = max(map(sum,numerator)),max(map(sum,denominator))
    first=n+d-1
    witness={"numerator":n,"denominator":d,"first_numerator":first,
             "minor_numerator":2*first, "exponent_gain":str(F(1,4*first))}
    assert (n,d,first,2*first)==(72,135,206,412)
    return witness

if __name__=='__main__':
    print(json.dumps({"volumes":{str(k):str(count_phases(k)) for k in range(2,10)},
                      "degree_certificate":degrees()},indent=2))
