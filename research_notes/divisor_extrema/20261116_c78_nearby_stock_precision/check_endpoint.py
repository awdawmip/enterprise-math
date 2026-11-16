"""Integer checks on the scale-dependent angular count in ENDPOINT_SHARPENING."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json


def angular_check(R, vertex, gamma=F(1,20)):
    # Unit tangent (a,b)/sqrt(a²+b²). Norm is Euclidean throughout.
    a,b=vertex
    ns=a*a+b*b
    def coordinate(x,y):
        return (a*x+b*y)**2
    def good(x,y):
        h2=x*x+y*y
        # (h dot t)^4 >= gamma^4 / (R² |h|²).
        return F(coordinate(x,y)**2*R*R*h2,ns*ns)>=gamma**4
    rows=[]
    for x,y in product(range(-4*R,4*R+1),repeat=2):
        if not 0<x*x+y*y<=16*R*R:
            continue
        rows.append((x,y))
    if not all(good(x,y) for x,y in rows):
        return None
    narrow = [(x,y) for x,y in rows if coordinate(x,y)*R*R<=ns]
    assert all(x*x+y*y >= gamma**4*R*R for x,y in narrow)
    return dict(R=R, direction=vertex, tested_differences=len(rows),
                strip_differences=len(narrow))


def main():
    cases=[]
    for R in (4,8,16):
        for vertex in [(137,97),(239,131),(412,215),(937,234)]:
            row=angular_check(R,vertex)
            if row:
                cases.append(row)
                break
    assert len(cases)==3 and F(11,4)-F(1,3)==F(29,12)
    return dict(good_angle_checks=cases, adjacent_sufficient="29/12",
                sharp_stock_gap_power="1/3")


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
