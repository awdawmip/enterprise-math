"""Verify the entire degree-six kernel on divisors of 720, using exact integers and fractions."""
from fractions import Fraction
from math import isqrt
import json

DENOMINATORS = [d for d in range(2, 721) if 720 % d == 0]
# Each row records signed multiplicities. All reductions proposed this basis offline.
# The checks below independently certify it spans the entire integer kernel.
BASIS = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -5, 8, 0, -14, 14, 0, 0, -8, 0, 5, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 3, -12, 29, -47, 0, 12, 25, 12, -25, -5, -1, -6, 0, 23, -6, 0, 3, -4, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 1, -6, 9, -2, -28, 23, 2, 20, -30, 15, -6, 4, -3, -8, 16, 3, -18, 9, -2, 3, -2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 9, -12, 8, -4, 1, -3, 0, 6, -6, 4, -3, 1],
    [0, 0, 0, 0, 0, -3, 23, -48, 64, -75, 0, 43, 7, -14, 20, -32, 18, -10, 0, 6, -1, 0, 7, -2, 0, -5, 0, 2, 0],
    [0, 0, 0, 0, 0, -3, 19, -31, 16, 56, -43, -44, 10, 19, 15, 4, -16, 10, -13, -7, 8, -10, 4, 6, 2, 0, 1, -2, -1],
    [0, 0, 0, 0, 0, 1, -3, -3, 27, -65, -7, 62, 13, -19, -13, 7, 6, -14, 2, -11, 4, 16, 6, 1, -9, 2, -2, -1, 0],
    [0, 0, 0, 0, 0, -5, 33, -58, 49, -8, 0, -21, -17, 24, 32, -36, -10, 27, 0, -7, -9, 0, 3, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 4, -11, 13, -4, -15, 35, -20, 3, -4, -5, 8, 1, -10, 8, 2, -1, -4, 0, 1],
    [0, 0, 0, 0, 0, 2, -17, 38, -53, 45, 7, 11, -32, -15, -12, 9, 29, 14, -2, -13, -1, -16, -1, -7, 9, 3, 2, 0, 0],
    [0, 0, 0, 0, 0, -2, 14, -26, 24, -2, 5, -41, 15, 15, 20, -16, 3, -13, -12, 10, 0, 9, -2, -1, 3, 1, -4, 1, -1],
    [0, 0, 0, 0, 0, -4, 28, -53, 56, -16, -50, 38, 11, -20, 10, 4, 25, -16, -23, 5, 2, 7, -2, -5, -1, 3, 3, -2, 0],
    [0, 0, 0, 0, 0, 0, 2, -8, 19, -20, -16, -3, 48, -10, -18, -2, -16, 15, 18, -4, -8, 1, -2, 8, 0, -3, -2, 2, -1],
    [0, 0, 0, 0, 0, -3, 18, -28, 16, -24, 66, -54, 0, -11, 18, 33, -21, -10, 5, -3, 4, -8, 1, -6, 1, 5, -1, 1, 1],
    [0, 0, 0, 0, 0, -1, 8, -17, 21, 16, -63, 31, 12, -4, 3, -7, 6, -13, -1, 4, 6, 1, 1, -1, 0, 1, -3, -2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -5, 16, -30, 25, -2, -11, -6, 22, 10, -18, -5, 0, -1, 6, 4, 0, -8, 2, 0, 1],
    [0, 0, 0, 0, 0, 1, -8, 17, -21, -16, 62, -25, -21, 6, 18, -42, 20, 15, 9, -16, 9, -9, -2, 1, -1, 1, 3, -1, 0],
    [0, 0, -1, 14, -46, 149, -104, -41, 5, -42, 66, 10, 7, 20, -25, -21, -9, 11, 5, -3, 1, -8, 12, -9, 1, 4, -1, 4, 1],
    [0, 0, 0, -1, 8, -95, 168, -33, -97, 55, -16, 14, -10, 37, -17, -13, -15, 3, 6, 15, -18, 2, 3, -3, 6, 1, 2, -2, 0],
    [0, 0, 0, 1, -7, 48, -18, -87, 66, -7, 43, 10, -16, -55, -9, 3, 4, -12, 25, 19, 3, 9, -2, -2, -8, -1, -5, -2, 0],
    [0, -1, 24, -140, 241, -171, -18, -31, 44, 70, 50, 17, 5, -56, -34, -19, -37, 8, 11, 29, 1, -6, 1, 1, 7, 0, 1, 2, 1],
    [-1, 55, -572, 1848, -1824, -69, 247, 351, 304, 58, -39, -110, -191, -108, -49, -34, -6, 20, 2, 15, 25, 21, 17, 10, 9, 10, 6, 4, 1],
]


def xgcd(a,b):
    aa,bb=abs(a),abs(b)
    x0,x1,y0,y1=1,0,0,1
    while bb:
        t,r=divmod(aa,bb)
        aa,bb=bb,r
        x0,x1=x1,x0-t*x1
        y0,y1=y1,y0-t*y1
    return aa,x0*(1 if a>=0 else -1),y0*(1 if b>=0 else -1)
def saturation(K):
    rows=list(map(list,zip(*K))); pivots=[]
    for j in range(len(K)):
        first=min((i for i in range(j,len(rows)) if rows[i][j]),key=lambda i:abs(rows[i][j]))
        rows[j],rows[first]=rows[first],rows[j]
        for i in range(j+1,len(rows)):
            a,b=rows[j][j],rows[i][j]
            if not b:continue
            if b%a==0:
                rows[i]=[y-(b//a)*x for x,y in zip(rows[j],rows[i])]
            else:
                g,u,v=xgcd(a,b)
                rows[j],rows[i]=([u*x+v*y for x,y in zip(rows[j],rows[i])],
                                 [(-b//g)*x+(a//g)*y for x,y in zip(rows[j],rows[i])])
        pivots.append(abs(rows[j][j]))
        assert pivots[-1]==1
    return pivots

def gram_schmidt(basis):
    directions, coefficients, lengths = [], [], []
    for vector in basis:
        orthogonal = list(map(Fraction, vector))
        row = []
        for u, length in zip(directions, lengths):
            coefficient = sum(x*y for x,y in zip(vector,u)) / length
            row.append(coefficient)
            orthogonal = [x-coefficient*y for x,y in zip(orthogonal,u)]
        length = sum(x*x for x in orthogonal)
        assert length > 0
        lengths.append(length)
        directions.append(orthogonal)
        coefficients.append(row)
    return coefficients, lengths


def certificate():
    ds, kernel = DENOMINATORS, BASIS
    assert len(ds)==29 and len(kernel)==22
    assert all(sum(c*(720//d)**j for c,d in zip(row,ds))==0
               for row in kernel for j in range(7))
    pivots = saturation(kernel)
    weighted = [[c*(d-1) for c,d in zip(row,ds)] for row in kernel]
    mu, lengths = gram_schmidt(weighted)
    n = len(kernel)
    digits = [0]*n
    visited = [0]*(n+1)
    extrema, minimum = [], None

    def search(i, remaining):
        nonlocal minimum
        visited[i+1] += 1
        if i < 0:
            if not any(digits):
                return
            signed = [sum(c*x for c,x in zip(digits,column)) for column in zip(*kernel)]
            plus = sum(max(0,c)*(d-1) for c,d in zip(signed,ds))
            minus = sum(max(0,-c)*(d-1) for c,d in zip(signed,ds))
            cost = max(plus,minus)
            if minimum is None or cost<minimum:
                minimum = cost
                extrema.clear()
            if cost==minimum:
                extrema.append(dict(positive=plus,negative=minus,
                                    signed={str(d):c for c,d in zip(signed,ds) if c}))
            return
        shift = sum((digits[j]*mu[j][i] for j in range(i+1,n)), Fraction(0))
        den, num = shift.denominator, shift.numerator
        square = remaining * den**2 / lengths[i]
        bound = isqrt(square.numerator // square.denominator)
        for c in range(-((bound+num)//den), (bound-num)//den+1):
            digits[i] = c
            search(i-1, remaining-lengths[i]*(c+shift)**2)
        digits[i] = 0

    search(n-1, Fraction(2*2332**2))
    assert minimum==2332 and len(extrema)==2 and visited[0]==3337
    assert {v['positive'] for v in extrema}=={2276,2332}
    return dict(grid=720, denominator_count=len(ds), full_kernel_rank=len(kernel),
                primitive_pivots=pivots, squared_radius=2*2332**2,
                nodes_by_remaining_dimension=visited, nonzero_vectors=visited[0]-1,
                minimum_max_side=minimum, oriented_minimizers=extrema)


if __name__=='__main__':
    print(json.dumps(certificate(), indent=2, sort_keys=True))
