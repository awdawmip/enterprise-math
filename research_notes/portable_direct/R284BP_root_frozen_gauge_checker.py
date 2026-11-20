"""R284BP: exact finite certificate of the all-dimension frozen-root Port gauge.

No packages. Models auxiliary signed determinant algebra, not native X6/BRC dynamics.
"""
from itertools import product
from collections import defaultdict
import json


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def det(a):
    n=len(a)
    if n==1: return a[0][0]
    if n==2: return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if n==3: return det3(a)
    return sum((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(n))


def signature(C,t):
    n=len(C);m=n-1
    a=C[0][0]; b=C[0][1:]
    v=[C[i][0] for i in range(1,n)]
    A=[row[1:] for row in C[1:]]
    gvals=[]; fvals=[]
    for x in product((0,1),repeat=m):
        B=[[(x[i] if i==j else 0)-A[i][j] for j in range(m)]
           for i in range(m)]
        D=det(B)
        g=[det([[v[i] if j==k else B[i][j] for j in range(m)]
                for i in range(m)]) for k in range(m)]
        gvals.extend(g)
        fvals.append((t-a)*D-sum(bi*gi for bi,gi in zip(b,g)))
    return tuple(gvals+fvals)


def exhaustive(n,H,t):
    """Complete H^(n*n) census. Symbolic signatures via Boolean interpolation."""
    seen={}; collision=None
    for flat in product(range(1,H+1), repeat=n*n):
        C=tuple(flat[i*n:(i+1)*n] for i in range(n))
        key=signature(C,t)
        if key in seen:
            if collision is None: collision=(seen[key],C)
        else: seen[key]=C
    return {"n":n,"H":H,"t":t,"total":H**(n*n),
            "unique_signatures":len(seen),"collision_example":collision}


def witness(n,H,t):
    q,rem=divmod(t-1,H);a=rem+1
    assert -(H-1)<=q<=H-1
    C=[[1]*n for _ in range(n)]
    C[0][0]=a;C[0][1]=1+max(q,0)
    for k in range(1,n):C[k][0]=H
    Cp=[r[:] for r in C]
    for k in range(1,n):Cp[k][1]=2
    Cp[0][1]=1+max(-q,0)
    assert C!=Cp
    assert all(1<=value<=H for row in C+Cp for value in row)
    assert signature(C,t)==signature(Cp,t)
    return {"n":n,"H":H,"t":t,"identity":True}


def main():
    tests=[]
    for n,H,ts in ((3,2,(-2,-1,0,4,5)),(4,2,(-2,0,5))):
        for t in ts: tests.append(exhaustive(n,H,t))
    W=[witness(*args) for args in ((3,2,-1),(3,3,9),(4,2,0),
       (4,2,4),(5,4,-11),(5,4,16),(6,3,9))]
    out={"schema":"R284BP_ROOT_FROZEN_EXACT_V1",
         "arithmetic":"exact Python integers",
         "signature":"all Boolean-cube values of adj(B)v and F(x,0); determines all coefficient polynomials in x; z linear",
         "tests":tests,"witnesses":W,
         "unbounded_proof":"separate algebraic rank-one gauge theorem",
         "review":"NOT_REVIEWED"}
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
