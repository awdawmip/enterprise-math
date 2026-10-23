#!/usr/bin/env python3
"""C267 second exact arithmetic audit; recomputes 79 full grid weights.

Raw rational node/parameter input is imported from the sibling standalone
C267_NEGATIVE_BOX_REPLAY, but this file does NOT use its masses or evaluator.
This is author-level algorithmic crosscheck, not independent Driver review.
"""
from fractions import Fraction as R
from itertools import product
from C267_NEGATIVE_BOX_REPLAY import U,I,Z,Q,H,A,LO,HI
J=tuple(j for j in range(79) if j not in I)
EXPECT={
"0000":634607732977867253452378042222042125,
"0001":584964881163760745811605106041906851,
"0010":705893694315153068381387470031822698,
"0011":644129091641390744951454959275607623,
"0100":612699895421719514530257681513016892,
"0101":562796664154410611826643772632090578,
"0110":685591398193880639071563937949668779,
"0111":623376750766887715999954110470579400,
"1000":826898579973141666370360940583377567,
"1001":776321459015712476303239989099254951,
"1010":897362792208724281958704866806021651,
"1011":834657257088497410319329845732333449,
"1100":804090303133902076269964662665445070,
"1101":753256751829459868275422354275775051,
"1110":876165659775711699098307516358722403,
"1111":813013839174026518365745549977503284,
}
def weight(j,grid):
    out=R(1)
    for k,y in enumerate(grid):
        if j!=k:out*=(Z-y)/abs(grid[j]-y)
    return out

original={j:weight(j,U) for j in J}
mass={}
for j in J:
    x=U[j]
    b=R(Q)*A*original[j]/(H*((2-x*x)*(3-x*x))**3)
    mass[j]=b.numerator//b.denominator
    assert mass[j]>0

def full_grid_eval(values):
    grid=list(U)
    for i,v in zip(I,values):grid[i]=v
    out=R(0)
    for j in range(79):
        w=weight(j,grid)
        if j in J:
            out+=mass[j]*w/original[j]
        else:
            x=grid[j]
            out+=R(Q)*A*w/(H*((2-x*x)*(3-x*x))**3)
    return out

assert len(U)==79 and all(U[j]<U[j+1] for j in range(78))
assert len(EXPECT)==16
for bits in product((0,1),repeat=4):
    key="".join(map(str,bits))
    pt=tuple((HI[k] if b else LO[k]) for k,b in enumerate(bits))
    v=Q-full_grid_eval(pt)
    assert v>0 and v.numerator//v.denominator==EXPECT[key],key
m=min(EXPECT.values())
assert m==562796664154410611826643772632090578>0
if __name__=="__main__":
    print("C267_INDEPENDENT_FORMULA_EXACT_PASS",16,"min_integer_gap",m)
