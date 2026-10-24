#!/usr/bin/env python3
"""R250 author-side exact BRC histogram and faithful 2x2 Laurent-image cross-check.
This uses the declared BRC algebra from Source; it is NOT an enterprise_math package import.
"""
from collections import defaultdict
from itertools import product

# Effects act on signed X6 chart:
# (x1,x2,x3,...,x6) -> (sigma*x1+k,sigma*x2,x3,...,x6).
# Chronological composition is first f and then g (g o f).
EDGES = (
    ((2,(-1,-1)),(2,(+1,-1))),
    ((0,(-1,-1)),(0,(+1,-1))),
    ((1,(+1,+1)),(2,(+1,-1))),
)
ZERO={}
ONE={0:1}
def then(f,g): return f[0]*g[0],g[0]*f[1]+g[1]
def apply(f,x): return (f[0]*x[0]+f[1],f[0]*x[1],*x[2:])
def histogram(start,depth):
    states={(start,(1,0)):1}
    for _ in range(depth):
        out=defaultdict(int)
        for (q,f),count in states.items():
            for dst,g in EDGES[q]:
                out[dst,then(f,g)]+=count
        states=out
    obs=defaultdict(int)
    for (q,f),count in states.items():obs[f]+=count
    return dict(obs)
def add(a,b):
    out=defaultdict(int,a)
    for p,c in b.items():out[p]+=c
    return {p:c for p,c in out.items() if c}
def mul(a,b):
    out=defaultdict(int)
    for p,c in a.items():
        for q,d in b.items():out[p+q]+=c*d
    return {p:c for p,c in out.items() if c}
def total(items):
    x={}
    for a in items:x=add(x,a)
    return x
def image(f):
    # Psi(f)=rho(f^-1)=D_{-sigma*k} P_sigma; faithful Q[D_infty] monomial image.
    sigma,k=f
    m=-sigma*k
    return (({m:1},ZERO),(ZERO,{-m:1})) if sigma==1 else ((ZERO,{m:1}),({-m:1},ZERO))
def prod2(A,B):
    return tuple(tuple(add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j]))
                       for j in range(2)) for i in range(2))
def embed(hist):
    ans=[[ZERO,ZERO],[ZERO,ZERO]]
    for f,count in hist.items():
        M=image(f)
        for i in range(2):
            for j in range(2):
                ans[i][j]=add(ans[i][j],{p:c*count for p,c in M[i][j].items()})
    return tuple(tuple(row) for row in ans)
def transition():
    M=[[ZERO for _ in range(6)] for _ in range(6)]
    for source,edges in enumerate(EDGES):
        for target,effect in edges:
            block=image(effect)
            for i in range(2):
                for j in range(2):
                    M[2*source+i][2*target+j]=add(M[2*source+i][2*target+j],block[i][j])
    return M
def matmul(A,B):
    n=len(A)
    return [[total(mul(A[i][k],B[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]
def observation(M,start):
    return tuple(tuple(total(M[2*start+i][2*q+j] for q in range(3))
                       for j in range(2)) for i in range(2))
def main():
    # Group law, source Affine.then ordering, and faithful representation product.
    cases=list(product((-1,1),range(-2,3)))
    for f in cases:
        for g in cases:
            assert image(then(f,g))==prod2(image(f),image(g))
            for x in ((0,0,0,0,0,0),(2,3,-4,5,6,-7)):
                assert apply(then(f,g),x)==apply(g,apply(f,x))
    W=[[ONE if i==j else ZERO for j in range(6)] for i in range(6)]
    M=transition()
    same=[True,True,True,False]
    for depth in range(9):
        for initial in range(3):
            h=histogram(initial,depth)
            assert observation(W,initial)==embed(h),(depth,initial)
            assert sum(h.values())==2**depth
        if depth<4:
            assert (histogram(0,depth)==histogram(1,depth))==same[depth]
        W=matmul(W,M)
    x,y=histogram(0,3),histogram(1,3)
    assert x.get((1,1),0)==0 and y.get((1,1),0)==1
    print("PASS R250: shortest=3, 100 group pairs, 27 direct-vs-Laurent six-axis observations, depths=0..8")
if __name__=="__main__":
    main()
