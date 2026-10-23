#!/usr/bin/env python3
"""C267 independent standalone exact proof for a four-dimensional F<Q box.

This proves a continuous NEGATIVE subbox of the C195/H168 auxiliary model
via the coordinatewise convexity / 16-vertex upper-envelope theorem.
No native GF(2)-BRC correspondence and no independent Driver admission.
"""
from fractions import Fraction as R
from itertools import product

NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)

U=tuple(R(a,b) for a,b in zip(NUM,DEN))
I=(5,50,55,56);J=tuple(k for k in range(79) if k not in I)
Z=R(141421356237309504880,10**20);Q=2**128;H=2**166
A=R(6912*50000**2,17**2)
assert all(U[j]<U[j+1] for j in range(78)) and U[-1]<Z and Z*Z<2

# Exact fixed positive integer masses, with the published floor convention.
B={}
for j in J:
    t=R(Q)*A/H/((2-U[j]*U[j])*(3-U[j]*U[j]))**3
    for r in range(79):
        if r!=j:t*=(Z-U[r])/abs(U[j]-U[r])
    B[j]=t.numerator//t.denominator
    assert B[j]>0

def evaluate(v):
    """Compute the unrounded complete 79-branch F(v), no floating point."""
    fixed=R(0)
    for j in J:
        t=R(B[j])
        for k,x in zip(I,v):
            t*=(Z-x)*abs(U[j]-U[k])/((Z-U[k])*abs(U[j]-x))
        fixed+=t
    moving=R(0)
    for k,x in zip(I,v):
        t=R(Q)*A/H/((2-x*x)*(3-x*x))**3
        for j in J:t*=(Z-U[j])/abs(x-U[j])
        for p,y in zip(I,v):
            if p!=k:t*=(Z-y)/abs(x-y)
        moving+=t
    return fixed+moving

CENTER=(R(1,100),R(141,200),R(99,125),R(101,125))
RADIUS=R(1,1250)
LO=tuple(c-RADIUS for c in CENTER)
HI=tuple(c+RADIUS for c in CENTER)
assert all(U[k-1]<LO[i]<HI[i]<U[k+1] for i,k in enumerate(I))
assert HI[2]<LO[3] and HI[3]<Z

# Pair-hull bounding intervals are copied exactly from the C254 source records.
PARENTS={
    (1,13):(('3/407','34/49','60/77','4/5'),('7/477','18/25','59/74','9/11')),
    (9,16):(('1/135','7/10','18/23','49/61'),('3/205','12/17','4/5','9/11')),
    (9,19):(('1/135','7/10','18/23','49/61'),('3/205','5/7','4/5','9/11')),
}
for pair,(low,high) in PARENTS.items():
    assert all(R(a)<=LO[i]<HI[i]<=R(b) for i,(a,b) in enumerate(zip(low,high))),pair

corners=[]
for bits in product((0,1),repeat=4):
    v=tuple(HI[i] if bit else LO[i] for i,bit in enumerate(bits))
    f=evaluate(v)
    gap=R(Q)-f
    assert gap>0,(bits,f)
    corners.append((bits,gap))
minimum=min(v for _,v in corners)
min_floor=minimum.numerator//minimum.denominator
assert min_floor>0
if __name__=='__main__':
    print('C267_16_VERTEX_EXACT_PASS',len(corners),'minimum_integer_gap_floor',min_floor)
    print('C267_BOX',tuple(map(str,LO)),tuple(map(str,HI)))
    print('C267_CONTAINED_NEGATIVE_PARENT_HULLS',sorted(PARENTS))
    for bits,gap in corners:
        print('C267_VERTEX', ''.join(map(str,bits)), 'integer_gap_floor',gap.numerator//gap.denominator)
