"""Exact rational-plane certificate for the six normalized three-vector signatures.
Within 1/2<=a<2, measure-zero cell faces are sampled as well as open cells.
Every possible true/rival distance equality or competing active coordinate
change belongs to the arrangement, as does each proposed domain boundary.
"""
from fractions import Fraction as Q
from functools import reduce
from itertools import product,combinations
from math import gcd
S=((0,0,0),(0,0,-1),(0,-1,1),(-1,1,-1),(1,-1,0),(-1,0,0))
def normalize(line):
    if not any(line):return None
    g=reduce(gcd,line);z=tuple(x//g for x in line)
    return tuple(-x for x in z) if next(x for x in z if x)<0 else z

def planes():
    # Signed affine terms sigma*(a*s_ji+c-s_ki) of every distance.
    terms=set((sgn*x,sgn,-sgn*y) for x,y,sgn in product((-1,0,1),(-1,0,1),(-1,1)))
    return {line for l,r in combinations(terms,2) if (line:=normalize(tuple(a-b for a,b in zip(l,r))))}

def cuts(order):
    seq=sorted(set(order))
    return sorted(set(seq+[(l+h)/2 for l,h in zip(seq,seq[1:])]))

def good(a,c):
    D=[[max(abs(a*x+c-y) for x,y in zip(sa,sb)) for sb in S] for sa in S]
    return all(row[i]<z for i,row in enumerate(D) for j,z in enumerate(row) if i!=j)

def run():
    lines=planes()|{(2,0,-1),(1,0,-2),(0,2,1),(2,-2,-1),(1,-2,0)}
    amin,amax=Q(1,2),Q(2)
    xx={amin,amax}
    for a,b,c in lines:
        if not b and a and amin<=-Q(c,a)<=amax:xx.add(-Q(c,a))
    for (a,b,c),(d,e,f) in combinations(lines,2):
        det=a*e-b*d
        if det and amin<=(q:=Q(b*f-e*c,det))<=amax:xx.add(q)
    n=0
    for a in cuts(xx):
        yy={-(x*a+z)/y for x,y,z in lines if y}
        ys=cuts(yy)
        for c in [ys[0]-1,*ys,ys[-1]+1]:
            if a==2: continue
            proposed=(a>Q(1,2) and c>-Q(1,2) and c<a-Q(1,2) and 2*c<a)
            assert good(a,c)==proposed,(a,c)
            n+=1
    return n

if __name__=='__main__': print('rational arrangement witnesses',run())
