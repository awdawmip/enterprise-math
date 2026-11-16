#!/usr/bin/env python3
"""R749SRY: finite exact global N(M) via extreme-coordinate feasibility and polynomial tail.
No external libraries; all rational operations exact.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json
W=(1,1,2,3,6); J=(0,1,5); P=tuple(F(x,36) for x in (455,-295,-25,185,-25,-295))
S=tuple(tuple(P[(a+h)%6] for h in J) for a in range(6))
H=(F(1,6),F(1,2),-F(115,36),F(115,6),-F(16315,108))

def counts(N):
 c=[0]*N;t=[0]*N;c[0]=1
 for i,w in enumerate(W):
  for j in range(w,N):
   t[j]+=t[j-w]+(c[j-w] if i==0 else 0)
   c[j]+=c[j-w]
 C=[0];T=[0]
 for v in range(N):C.append(C[-1]+c[v]);T.append(T[-1]+t[v])
 return C,T

def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def scale(a,s):return [v*s for v in a]
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def power(a,k):
 out=[F(1)]
 for _ in range(k):out=mul(out,a)
 return out
def interpolate(y):
 d=list(map(F,y));out=[F(0)]
 for k in range(len(y)):
  p=[F(1)]
  for i in range(k):p=mul(p,[-F(i),F(1)])
  out=add(out,scale(p,d[0]/factorial(k)))
  d=[d[i+1]-d[i] for i in range(len(d)-1)]
 return out
def deg(a):
 i=len(a)-1
 while i>0 and a[i]==0:i-=1
 return i

def tail_certificate(C,T):
 """For each class r=516+a+6n, proves 0<R(r)-P[a]<1600/r, n>=0."""
 rows=[]
 for a in range(6):
  base=516+a
  cp=interpolate([C[base+6*i] for i in range(6)])
  tp=interpolate([T[base+6*i] for i in range(7)])
  for i in range(7,12):
   assert sum(cp[j]*i**j for j in range(len(cp)))==C[base+6*i]
   assert sum(tp[j]*i**j for j in range(len(tp)))==T[base+6*i]
  r=[F(base),F(6)]
  smooth=[P[a]]
  for i,v in enumerate(H):smooth=add(smooth,scale(power(r,4-i),v))
  q=add(mul(power(r,3),tp),scale(mul(cp,smooth),-1))
  upper=add(scale(cp,1600),scale(mul(r,q),-1))
  assert deg(cp)==5 and deg(tp)==6 and deg(q)==4 and deg(upper)==5
  assert all(v>0 for v in cp[:6]) and all(v>0 for v in q[:5]) and all(v>0 for v in upper[:6])
  rows.append({'phase':a,'base':base,'degrees':[deg(cp),deg(tp),deg(q),deg(upper)],
    'positive_coefficient_counts':[6,5,6], 'Q_leading':str(q[4]),'upper_leading':str(upper[5])})
 return rows

def ceilq(x):return -(-x.numerator//x.denominator)

def competitor(a,b,x,u,M):
 """Exact existence over full integer cube; at most 2k extreme coordinates."""
 k=len(x); delta=[S[b][i]-S[a][i] for i in range(k)]
 for j in range(k):
  for sign in (-1,1):
   t=sign*(x[j]+u[j]*sign*M)
   if t<0 or not (0<=sign*delta[j]<=2*t):continue
   e=[0]*k;e[j]=sign*M
   for i in range(k):
    if i==j:continue
    lo=max(-t,delta[i]-t);hi=min(t,delta[i]+t)
    L=max(-M,ceilq((lo-x[i])/u[i]));U=min(M,(hi-x[i])//u[i])
    if L>U:break
    e[i]=L
   else:return tuple(e)
 return None

def failure(r,R,U,M):
 a=r%6;x=tuple(R[r+h]-S[a][i] for i,h in enumerate(J));u=tuple(U[r+h] for h in J)
 for b in range(6):
  if b==a:continue
  e=competitor(a,b,x,u,M)
  if e is not None:return {'r':r,'phase':a,'competitor':b,'errors':list(e)}
 return None

def direct_failure(r,R,U,M):
 a=r%6
 for e in product(range(-M,M+1),repeat=3):
  y=[R[r+h]+U[r+h]*e[i] for i,h in enumerate(J)]
  da=max(abs(y[i]-S[a][i]) for i in range(3))
  for b in range(6):
   if b!=a and max(abs(y[i]-S[b][i]) for i in range(3))<=da:return True
 return False

def main():
 maxM=300; cutoff=900
 assert F(1600,cutoff)+F(4320*maxM,cutoff*cutoff)<F(15,4)
 C,T=counts(cutoff+max(J)+3)
 tail=tail_certificate(C,T)
 U=[F(0)];R=[F(0)]
 for r in range(1,len(C)):
  U.append(F(r**3,C[r]));R.append(U[r]*T[r]-sum(v*r**(4-i) for i,v in enumerate(H)))
 checked=0
 for r in range(1,100):
  for M in range(3):
   assert bool(failure(r,R,U,M))==direct_failure(r,R,U,M),(r,M)
   checked+=1
 critical=[]
 for r in range(1,cutoff):
  if failure(r,R,U,maxM) is None:continue
  low=0;high=maxM
  while low<high:
   mid=(low+high)//2
   if failure(r,R,U,mid):high=mid
   else:low=mid+1
  assert failure(r,R,U,low) is not None
  if low>0:assert failure(r,R,U,low-1) is None
  critical.append([r,low])
 rows=[]
 for M in range(maxM+1):
  candidates=[r for r,m in critical if m<=M]
  last=max(candidates,default=0)
  rows.append(last+1)
 assert rows[0:3]==[35,53,65]
 samples=[0,1,2,3,4,5,10,20,32,40,50,64,80,100,150,200,300]
 witnesses={str(M):failure(rows[M]-1,R,U,M) for M in samples}
 assert all(w is not None for w in witnesses.values())
 assert all(failure(rows[M],R,U,M) is None for M in range(maxM+1))
 return {'status':'PASS','unit':'R749SRY',
  'model':'W=(1,1,2,3,6), J=(0,1,5), exact denominator C, integer numerator errors',
  'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'theorem':'Extremal coordinate + independent lattice interval feasibility is necessary and sufficient for decoding failure for any M and any r.',
  'global_bound':'0 < R(r)-P[r mod 6] < 1600/r for all r>=516',
  'volume_bound':'C_r>=r^5/4320 for all r>=1',
  'tail_r_start':900,'M_all_integers_from':0,'M_all_integers_to':300,
  'tail_margin_at_900':str(F(15,4)-F(1600,900)-F(4320*300,900**2)),
  'tail_positive_coefficient_checks':tail,
  'bruteforce_r_M_pairs':checked,
  'exact_global_N_for_M_0_to_300':rows,
  'selected_failures_at_N_minus_1':witnesses,
  'future_question':'Asymptotic bounded fluctuation law; simultaneous errors in C and T; sharper complexity and joint provenance.'}
if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,indent=2))
