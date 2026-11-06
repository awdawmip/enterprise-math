#!/usr/bin/env python3
"""PREFIX-537: exact polynomial 3-seed X6 BRC-gate joint histograms.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
All 48 roots, depths 0..24; independent labeled-path comparison.
"""
from collections import Counter,defaultdict
from json import dump

S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*x for x in S[a] if x!=abs(c))
PH=tuple((a,p,e*x) for a in range(4) for x in S[a] for e in (-1,1) for p in near(a,e*x))
IDX={x:i for i,x in enumerate(PH)}
def succ(x):
 a,p,c=x;b=next(b for b in range(4) if b!=a and abs(c) in S[b])
 return tuple(IDX[y] for y in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
NX=tuple(succ(x) for x in PH)
T=IDX[(0,1,-3)]
sig=lambda i: (1 if PH[i][2]>0 else -1) if abs(PH[i][2])==1 else 0
eps=lambda i:int(abs(PH[i][2])==1)
BACK=tuple(Counter(eps(i)+2*eps(m)+eps(T) for m in NX[i] if T in NX[m]) for i in range(48))
assert len(PH)==48 and all(len(a)==3 for a in NX) and sum(sum(a.values()) for a in BACK)==9

def add(out,src,de=0,dh=0,c=1):
 for (e,h),v in src.items():out[(e+de,h+dh)]+=c*v

def lift(n):
 allroots=[[None]*(n+1) for _ in range(48)]
 peaks={}
 for r in (-1,0,1):
  roots=[i for i in range(48) if sig(i)==r]
  f=[{(2-abs(sig(i)-r),0):1} for i in range(48)];g={};pk=0
  for d in range(n+1):
   for i in roots:
    a={}
    for (e,h),v in f[i].items():
     assert e>=2 and e%2==0 and v>0
     a[((e-2)//2,h)]=v
    assert sum(a.values())==6**d
    allroots[i][d]=a
   pk=max(pk,sum(len(a) for a in f)+len(g))
   if d==n:break
   nxt=[]
   for i in range(48):
    p=defaultdict(int)
    for j in NX[i]:add(p,f[j],eps(i)+eps(j),0,2)
    for k,c in BACK[i].items():add(p,g,k,0,c)
    nxt.append({k:v for k,v in p.items() if v})
   gp=defaultdict(int);add(gp,f[T],0,1);add(gp,f[T],0,0,-1)
   f,g=nxt,{k:v for k,v in gp.items() if v}
  peaks[str(r)]={'roots':len(roots),'max_polynomial_monomial_storage':pk}
 return allroots,peaks

def raw(root,n):
 states={(root,0,0,0):1};seq=[]
 for d in range(n+1):
  p=defaultdict(int)
  for (i,b,k,h),c in states.items():
   delta=abs(sig(i)-sig(root))
   assert k>=delta and (k-delta)%2==0
   p[((k-delta)//2,h)]+=c
  seq.append(dict(p))
  assert sum(p.values())==6**d
  if d==n:break
  nxt=defaultdict(int)
  for (i,b,k,h),c in states.items():
   for j in NX[i]:
    for inner in (0,1):nxt[(j,inner,k+eps(i)+eps(j),h+int(b and inner and j==T))]+=c
  states=nxt
 return seq

N=24
allroots,peak=lift(N)
for root in range(48):assert raw(root,N)==allroots[root]
by_depth=[]
for d in range(N+1):
 p=[allroots[root][d] for root in range(48)]
 assert all(all(0<=h<=((d+2)//4) and h<=k<=d and c>0 for (k,h),c in f.items()) for f in p)
 bound=((d+2)//4+1)*(d+1)-((d+2)//4)*(((d+2)//4)+1)//2
 assert all(len(f)<=bound for f in p)
 by_depth.append({'depth':d,'min_terms':min(map(len,p)),'max_terms':max(map(len,p)),
  'total_nonzero_coefficients':sum(map(len,p)),
  'distinct_rooted_polynomials':len({tuple(sorted(f.items())) for f in p}),
  'max_gate_degree':max(max(h for k,h in f) for f in p),
  'max_coefficient_bits':max(max(c.bit_length() for c in f.values()) for f in p)})
result={'status':'ALL_CHECKS_PASS','science_pin':'enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'roots':48,'depths':'0..24','independent_polynomial_equalities':48*(N+1),
 'three_shared_lift':peak,'by_depth':by_depth,
 'example_root_0_depth_6':[[k,h,str(c)] for (k,h),c in sorted(allroots[0][6].items())],
 'scope':'Four STAR directed native X6, 6 labeled histories per macro step, exact Z[q,z] coefficients',
 'review_status':'AUTHOR_EXACT_CHECKED_UNREVIEWED'}
with open('PREFIX537_EXACT_EXECUTION.json','w',encoding='utf-8') as f:dump(result,f,indent=2)
print('ALL_CHECKS_PASS: 1200 root-depth checks; d24 terms',by_depth[-1]['total_nonzero_coefficients'])
