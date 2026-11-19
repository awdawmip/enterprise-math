"""Exact finite checks of the a>1/4 direction-event identity.

These finite examples support the implementation; the general counting
argument is proved in HAAR_FINITE_INTERVAL.md.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd,ceil
from pathlib import Path
import json


def add(u,v):
    return tuple(x+y for x,y in zip(u,v))


def marks(v):
    x,y=v
    return x,y,2*y-x


def determinant(u,v):
    return u[0]*v[1]-u[1]*v[0]


def canonical(label):
    n,m=label
    return label if n>0 or (n==0 and m>0) else (-n,-m)


total=0
hist={k:0 for k in range(4)}
for a in [F(3,10),F(1,3),F(2,5),F(49,100),F(1,2)]:
    for v in [(F(1,3),F(1,5)),(F(1),F(0)),
              (F(1,7),F(1,9)),(F(2,3),F(-1,3)),
              (F(4,5),F(2,5))]:
        vv=sum(x*x for x in v)
        for shear in [F(0),F(1,4),F(1,2),F(3,4),a*v[1]/(vv*v[0])]:
            w=(-a*v[1]/vv+shear*v[0],a*v[0]/vv+shear*v[1])
            assert determinant(v,w)==a
            bound_n=ceil((abs(w[0])+abs(w[1]))/a)
            bound_m=ceil((abs(v[0])+abs(v[1]))/a)
            candidates={}
            for n in range(-bound_n,bound_n+1):
                for m in range(-bound_m,bound_m+1):
                    if gcd(n,m)!=1:
                        continue
                    z=tuple(n*x+m*y for x,y in zip(v,w))
                    l=marks(z)
                    if all(abs(x)<1 for x in l):
                        candidates[n,m]=l
            for phase in product([F(0),F(1,4),F(1,2),F(3,4)],repeat=3):
                present={k for k,l in candidates.items()
                         if all(0<=p+x<1 for p,x in zip(phase,l))}
                directions={canonical(k) for k in present}
                n=len(directions)
                assert n<=3
                hist[n]+=1
                if n>=2:
                    assert len(present)==n
                pairs=[(u,w) for u in present for w in present
                       if determinant(u,w)>0]
                assert all(determinant(u,w)==1 for u,w in pairs)
                triangles=sum(add(u,w) in present for u,w in pairs)
                assert len(pairs)==n*(n-1)//2
                assert triangles==(1 if n==3 else 0)
                assert int(n==0)==1-n+len(pairs)-triangles
                total+=1

assert hist[3]>0
result={'checks':'exact finite direction-event identity',
        'lattice_phase_cases':total,'direction_histogram':hist,
        'arithmetic':'fractions.Fraction',
        'statement_scope':'Finite examples; analytic proof is in HAAR_FINITE_INTERVAL.md.'}
Path(__file__).with_name('direction_event_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
