#!/usr/bin/env python3
"""Finite exact closed native X6 BRC trace-polynomial symmetry test, depth<=12."""
from collections import defaultdict
from itertools import product
import json
from pathlib import Path
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in STARS[a] if k!=abs(c))
PHASE=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in(-1,1) for p in near(a,s*k))
IX={x:i for i,x in enumerate(PHASE)}
def succ(i):
 a,p,c=PHASE[i];b=next(b for b in range(4) if b!=a and abs(c) in STARS[b]);return tuple(IX[x] for x in [(a,c,d) for d in near(a,c) if d!=p]+[(b,c,d) for d in near(b,c)])
NEXT=[succ(i) for i in range(48)];TARGET=IX[(0,1,-3)]
E=[[] for _ in range(96)]
for i in range(96):
 phase,bit=divmod(i,2);axis=abs(PHASE[phase][2])-1
 for slot,nb in product(range(3),(0,1)):
  j=NEXT[phase][slot]
  E[i].append((2*j+nb,axis,int(bit==nb==1 and j==TARGET)))
MAX=12
traces=[defaultdict(int) for _ in range(MAX+1)]
for initial in range(96):
 D={(initial,(0,)*7):1}
 for depth in range(1,MAX+1):
  U=defaultdict(int)
  for (node,counts),multiplicity in D.items():
   for dest,axis,gate in E[node]:
    v=list(counts);v[axis]+=1;v[6]+=gate
    U[(dest,tuple(v))]+=multiplicity
  D=U
  for (end,counts),multiplicity in D.items():
   if end==initial:traces[depth][counts]+=multiplicity
p=(2,3,0,1,4,5)
res=[]
for d in range(1,MAX+1):
 C=traces[d]
 assert all(C[vec]==C.get(tuple(vec[p[i]] for i in range(6))+(vec[6],),0) for vec in C)
 res.append({'depth':d,'distinct_closed_observer_monomials':len(C),'closed_labelled_paths':sum(C.values()),'permutation_exact_equal':True})
result={'schema':'PREFIX583_R2_FINITE_CLOSED_TRACE_SYMMETRY_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'scope':'Original 96 native start/end ports; 576 labelled actions; all closed paths length 1..12',
 'axis_permutation':'(1 3)(2 4) with gate fixed','observed':res,
 'inference':'Exact equality of multivariate closed-path trace polynomials for each d=1..12 only',
 'status':'ALL_ASSERTIONS_PASS_FINITE_EXHAUSTIVE_AUTHOR_SIDE'}
Path(__file__).with_name('PREFIX583_R2_finite_trace_scan_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result['observed'],indent=2))
