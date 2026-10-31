"""EC49BY exact compact verifier; native signed_brc.py must be in source/."""
from collections import defaultdict
from functools import lru_cache
from math import comb
from pathlib import Path
import importlib.util

s=importlib.util.spec_from_file_location('brc',Path(__file__).parent/'source/signed_brc.py')
brc=importlib.util.module_from_spec(s);s.loader.exec_module(brc)
Z=(0,)*6; A=tuple(range(1,7))+tuple(range(-1,-7,-1))
wp=(2,3,3,2,1,1); wm=(1,)*6

def w(a):return wp[a-1] if a>0 else wm[-a-1]
def sw(a):return (2 if a>0 else -2) if abs(a)==1 else ((1 if a>0 else -1) if abs(a)==2 else a)
def dfa(q,a):return 2 if q==2 or(q==1 and a==2) else (1 if a==1 else 0)
def move(x,a):
 y=list(x);i=abs(a)-1;y[i]+=1 if a>0 else -1;return tuple(y)
def dp(n):
 L={(Z,0,0):(1,1,1)};updates=0
 for t in range(n):
  T={}
  for (x,p,q),(u,v,c) in L.items():
   for a in A:
    k=(move(x,a),dfa(p,a),dfa(q,sw(a)))
    U,V,C=T.get(k,(0,0,0));T[k]=(U+u*w(a),V+v*w(sw(a)),C+c);updates+=1
  L=T
 R=defaultdict(lambda:[0,0,0])
 for (x,p,q),v in L.items():
  if x==Z:
   b=f'{int(p==2)}{int(q==2)}'
   for j in range(3):R[b][j]+=v[j]
 return dict(sorted(R.items())),len(L),updates

def direct(n):
 R=defaultdict(lambda:[0,0,0])
 def rec(t,x,p,q,u,v):
  if t==n:
   assert x==Z
   b=f'{int(p==2)}{int(q==2)}'
   R[b][0]+=u;R[b][1]+=v;R[b][2]+=1;return
  for a in A:
   y=move(x,a);r=n-t-1;dist=sum(abs(z) for z in y)
   if dist<=r and (r-dist)%2==0:rec(t+1,y,dfa(p,a),dfa(q,sw(a)),u*w(a),v*w(sw(a)))
 rec(0,Z,0,0,1,1)
 return dict(sorted(R.items()))

def recurrence(m,q):
 V=[1]+[0]*m
 for qi in q:
  P=[qi**k for k in range(m+1)];V=[sum(comb(2*j,2*k)*comb(2*k,k)*P[k]*V[j-k] for k in range(j+1)) for j in range(m+1)]
 return V

if __name__=='__main__':
 for n in (0,2,4,6,8):
  z,states,updates=dp(n);tot=[sum(v[j] for v in z.values()) for j in range(3)]
  assert tot==[brc.endpoint_weight(n,Z,wp,wm)]*2+[brc.endpoint_multiplicity(n,Z)]
  if n<=6:assert z==direct(n)
  print(n,tot,states,updates,z)
 W=recurrence(100,wp);U=recurrence(100,(1,)*6)
 for m in range(10):
  assert W[m]==brc.endpoint_weight(2*m,Z,wp,wm)
  assert U[m]==brc.endpoint_multiplicity(2*m,Z)
 assert (W[100].bit_length(),U[100].bit_length())==(789,695)
 print('n=200 exact numerator bits',W[100].bit_length(),U[100].bit_length())
