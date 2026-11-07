#!/usr/bin/env python3
"""PREFIX-564 exact standalone zero-root native X6-BRC certificate (stdlib only).
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d; six axes and gate stay independent.
"""
from collections import Counter
from itertools import product
from math import comb
import json

S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in S[a] if k!=abs(c))
P=tuple((a,p,e*k) for a in range(4) for k in S[a] for e in (-1,1) for p in near(a,e*k))
I={x:i for i,x in enumerate(P)}
def successors(i):
 a,p,c=P[i]; b=next(b for b in range(4) if b!=a and abs(c) in S[b])
 return tuple(I[x] for x in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(successors(i) for i in range(48))
T=I[(0,1,-3)]
ACTIONS=tuple(product(range(3),(0,1)))
ZERO=(0,)*7

def edge(i,action):
 p,b=divmod(i,2);slot,c=action;j=N[p][slot]
 w=tuple(int(abs(P[p][2])==k) for k in range(1,7))+(int(b==c==1 and j==T),)
 return 2*j+c,w

def sigma_signed(v):return (1 if v>0 else -1)*({5:6,6:5}.get(abs(v),abs(v)))
SIGINDEX={(p,c):i for i,(_,p,c) in enumerate(P)}
F=tuple(2*SIGINDEX[(sigma_signed(P[i//2][1]),sigma_signed(P[i//2][2]))]+i%2 for i in range(96))
ORBS=sorted({tuple(sorted({i,F[i]})) for i in range(96)})
REP=[o[0] for o in ORBS]
IDX={i:k for k,o in enumerate(ORBS) for i in o}
MIR={i:i!=REP[IDX[i]] for i in range(96)}
FIXED={k for k,o in enumerate(ORBS) if len(o)==1}
def tau(m):return m[:4]+(m[5],m[4])+m[6:]

def rows():
 return [Counter((IDX[j],MIR[j],w) for a in ACTIONS for j,w in [edge(i,a)]) for i in REP]

def clean(x):return Counter({k:v for k,v in x.items() if v})
def add(x,y,sgn=1):
 o=Counter(x)
 for k,v in y.items():o[k]+=sgn*v
 return clean(o)
def sh(x,k,mul=1):
 return Counter({t[:k]+(t[k]+1,)+t[k+1:]:mul*v for t,v in x.items()})
def calc(A,B,flip,w):
 if flip:A,B=add(A,sh(B,4)),clean(Counter({k:-v for k,v in B.items()}))
 if w[4]:A,B=sh(B,5,-1),add(A,sh(B,4))
 if w[5]:A,B=add(sh(A,4),sh(B,5)),clean(Counter({k:-v for k,v in A.items()}))
 def move(x):return Counter({tuple(t[k]+w[k] if k in (0,1,2,3,6) else t[k] for k in range(7)):v for t,v in x.items()})
 return move(A),move(B)
def step_uv(q,old):
 new=[]
 for row in q:
  A=Counter();B=Counter()
  for (j,f,w),n in row.items():
   C,D=calc(*old[j],f,w)
   for t,v in C.items():A[t]+=n*v
   for t,v in D.items():B[t]+=n*v
  new.append((clean(A),clean(B)))
 return new

def expand_half(old,k,flip):
 for t,v in old[k].items():
  yield (tau(t) if flip else t),v
  if k in FIXED and t[4]!=t[5]:yield tau(t),v

def step_half(q,old):
 new=[]
 for k,row in enumerate(q):
  v=Counter()
  for (j,flip,w),n in row.items():
   for t,c in expand_half(old,j,flip):
    mm=tuple(t[i]+w[i] for i in range(7))
    if k in FIXED and mm[4]>mm[5]:continue
    v[mm]+=c*n
  new.append(v)
 return new

def full_half(old,k):
 o=Counter()
 for t,v in expand_half(old,k,False):o[t]+=v
 return o

def decode(A,B):
 out=Counter()
 for poly,extra in ((A,0),(B,1)):
  for t,c in poly.items():
   u,v=t[4:6]
   for j in range(u+1):out[t[:4]+(v+j+extra,v+u-j)+t[6:]]+=c*comb(u,j)
 return clean(out)

def main(depth=16):
 assert len(P)==48 and len(F)==96 and len(ORBS)==64 and len(FIXED)==32
 assert all(F[F[i]]==i for i in range(96))
 q=rows();old=[Counter({ZERO:1}) for _ in range(64)];uv=[(Counter({ZERO:1}),Counter()) for _ in range(64)]
 checks=0;coeffs=0;fixed_checks=0
 for d in range(depth+1):
  assert all(not uv[k][1] for k in FIXED)
  fixed_checks+=len(FIXED)
  if d in (0,8,12,16):
   for k in range(64):
    expected=full_half(old,k)
    assert decode(*uv[k])==expected,(d,k)
    checks+=1;coeffs+=len(expected)
  if d<depth:old=step_half(q,old);uv=step_uv(q,uv)
 result={'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'depths_checked':[0,8,12,16],'exact_polynomial_comparisons':checks,
         'nonzero_coefficient_positions_checked':coeffs,'fixed_zero_B_checks':fixed_checks,
         'depth16_half_support_positions':sum(map(len,old)),
         'depth16_uv_module_positions':sum(len(A)+len(B) for A,B in uv)}
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
