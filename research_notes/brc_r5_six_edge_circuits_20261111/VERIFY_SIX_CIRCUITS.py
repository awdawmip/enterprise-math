#!/usr/bin/env python3
"""Exact 21x30 P/Q-Blackwell observer kernel circuit checker; no physical-feasibility claim."""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational

r=tuple(F(v) for v in ('1/10','1/2','3/4','1','5/4','3/2','19/10'))
J=(0,1,2,3,5,6)
D=tuple((i,j) for j in J for i in range(7) if j not in (0,6) or i==j)
assert len(D)==30 and len(set(D))==30

def col(i,j):
    c=[F(0) for _ in range(21)]
    c[i]=1
    c[7+j]=1
    c[14+j]=r[i]-r[j]
    return c

C=Matrix.hstack(*(Matrix([Rational(x.numerator,x.denominator) for x in col(*e)]) for e in D))
assert C.shape==(21,30)
assert C.rank()==15

circuits=[]
for ja,jb in combinations((1,2,3,5),2):
    for it in combinations(range(7),3):
        a,b,c=it
        h=(r[b]-r[c],r[c]-r[a],r[a]-r[b])
        assert sum(h)==0 and sum(h[k]*r[it[k]] for k in range(3))==0
        assert all(v for v in h)
        z=[F(0) for _ in D]
        for k,i in enumerate(it):
            z[D.index((i,ja))]=h[k]
            z[D.index((i,jb))]=-h[k]
        assert sum(bool(v) for v in z)==6
        residuals=[sum(F(C[row,n])*z[n] for n in range(30)) for row in range(21)]
        assert residuals==[F(0)]*21
        cols=[D.index((i,j)) for j in (ja,jb) for i in it]
        assert C[:,cols].rank()==5
        circuits.append((ja,jb,it))
assert len(circuits)==210
print('MODEL_RATIOS', ', '.join(map(str,r)))
print('ALLOWED_ARCS',len(D))
print('OBSERVER_ROWS',C.rows)
print('OBSERVER_RANK',C.rank())
print('OBSERVER_NULLITY',C.cols-C.rank())
print('SIX_EDGE_MINIMAL_CIRCUITS',len(circuits))
print('CIRCUIT_TYPE','K_2_3: two unrestricted sources and three distinct targets')
print('ONE_EXAMPLE_SOURCES',(1,3),'TARGETS',(0,3,6),'h',(-F(9,10),F(9,5),-F(9,10)))
print('PASS_EXACT_210_CIRCUIT_CONSTRUCTIONS_AND_RANKS')

# Exact nonnegative observer-level ambiguity (not a frozen-physical feasibility claim).
e0={(0,1):F(11,36),(3,1):F(1,6),(6,1):F(1,36),
    (0,3):F(1,8),(3,3):F(1,4),(6,3):F(1,8)}
h={(0,1):F(-1),(3,1):F(2),(6,1):F(-1),
   (0,3):F(1),(3,3):F(-2),(6,3):F(1)}
def readout(e):
    return tuple(sum(col(*k)[row]*val for k,val in e.items()) for row in range(21))
assert readout(h)==(F(0),)*21
assert sum(e0.values())==1
assert all(v>0 for v in e0.values())
assert all(readout(e0)[14+j]==0 for j in J)
e_plus={k:e0[k]+F(1,144)*h[k] for k in e0}
e_minus={k:e0[k]-F(1,144)*h[k] for k in e0}
assert all(x>0 for x in e_plus.values())
assert all(x>0 for x in e_minus.values())
assert e_plus!=e_minus and readout(e_plus)==readout(e_minus)
print('NONNEGATIVE_OBSERVER_WITNESS_SOURCES',(1,3),'TARGETS',(0,3,6))
print('WITNESS_BASE_WEIGHTS',[(f'{i},{j}',str(v)) for (i,j),v in e0.items()])
print('WITNESS_EPSILON', F(1,144))
print('WITNESS_TARGET_MARGINALS',[(i,str(readout(e_plus)[i])) for i in (0,3,6)])
print('PASS_EXACT_POSITIVE_PAIR_SAME_OBSERVER_READOUT')
