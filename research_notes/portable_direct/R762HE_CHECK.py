#!/usr/bin/env python3
"""R762HE exact standard-library certificate: characteristic polynomials and independent parity DP."""
from itertools import combinations
from collections import defaultdict
from math import comb
import json

ports=list(combinations(range(6),2))
P0=ports.index((0,1))
edges=[]
for i,p in enumerate(ports):
    for j,q in enumerate(ports):
        common=set(p)&set(q)
        if len(common)==1:
            edges.append((i,j,next(iter(common)),sum(1<<a for a in set(p)|set(q))))
assert len(ports)==15 and len(edges)==120

def mul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def B(k):
    signs=[-1 if a<k else 1 for a in range(6)]
    A=[[0]*15 for _ in range(15)]
    for i,j,a,mask in edges:
        A[i][j]=signs[a]
    assert A==list(map(list,zip(*A)))
    return A

def charpoly(A):
    # Exact Newton traces: c[0]=1, c[k]=-sum(c[k-j]tr(A^j))/k.
    T=[0]; M=ident(15)
    for _ in range(15):
        M=mul(M,A); T.append(tr(M))
    c=[1]
    for k in range(1,16):
        numerator=-sum(c[k-j]*T[j] for j in range(1,k+1))
        assert numerator%k==0
        c.append(numerator//k)
    return c  # descending degree

def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def expected_factor_product(factors):
    p=[1]
    for f,m in factors:
        for _ in range(m):
            p=pmul(p,f)
    assert len(p)==16
    return list(reversed(p))

factors=[
    [([-8,1],1),([-2,1],5),([2,1],9)],
    [([2,1],5),([-32,-2,1],1),([-2,-2,1],4)],
    [([0,1],3),([2,1],2),([4,1],1),([-4,-2,1],3),([32,-28,-2,1],1)],
    [([0,1],5),([-28,0,1],1),([-6,-2,1],2),([-6,2,1],2)],
]
T=[]
for k in range(4):
    M=B(k)
    assert charpoly(M)==expected_factor_product(factors[k]), k
    P=ident(15); t=[tr(P)]
    for m in range(16):
        P=mul(P,M); t.append(tr(P))
    T.append(t)

# Independent unsigned Port × six-bit triple-incidence parity automaton.
d={(P0,0):1}
rows=[]
for m in range(17):
    unsigned=sum(n for (p,mask),n in d.items() if p==P0)
    parity_zero=d.get((P0,0),0)
    U=(8**m+5*2**m+9*(-2)**m)//15
    assert unsigned==U
    spectral=0
    if m%2==0:
        numerator=T[0][m]+6*T[1][m]+15*T[2][m]+10*T[3][m]
        assert numerator%480==0
        spectral=numerator//480
    assert spectral==parity_zero,(m,spectral,parity_zero)
    rows.append([m,unsigned,parity_zero])
    nxt=defaultdict(int)
    for (p,mask),n in d.items():
        for i,j,a,triple in edges:
            if i==p:
                nxt[j,mask^triple]+=n
    d=nxt

# Independently audit the telescoping retained-axis identity on all paths <=4.
def verify(p,m,triple_parity,retained):
    if m==0:
        endpoint=sum(1<<i for i in ports[p])
        initial=sum(1<<i for i in ports[P0])
        assert triple_parity==(initial^endpoint^retained)
        return
    for i,j,a,triple in edges:
        if i==p:
            verify(j,m-1,triple_parity^triple,retained^(1<<a))
for m in range(5):
    verify(P0,m,0,0)

print(json.dumps({
    "check":"PASS",
    "proof_certificate":"4 exact characteristic polynomials (15x15 integer Newton traces)",
    "independent_dynamic_program":"0..16",
    "telescoping_path_audit":"0..4",
    "rows":rows,
    "review":"NOT_REVIEWED",
    "native_primitive_admission":"UNRESOLVED"
},ensure_ascii=False))
