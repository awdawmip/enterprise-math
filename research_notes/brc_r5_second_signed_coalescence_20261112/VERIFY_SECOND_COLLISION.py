#!/usr/bin/env python3
"""Exact R5 second signed-resonance collision; frozen 28 masses/15 moves."""
from fractions import Fraction as F
from collections import Counter
from math import factorial
R=(2,10,15,20,25,30,38)
PORTS=(1,2,3,5); J=(1,2,5)
V=tuple((i,j) for j in PORTS for i in range(7)); IX={v:k for k,v in enumerate(V)}
X=tuple(map(F,('250555781039/3397584400000,854053219229681/5470110884000000,'
 '155682221/156288882400000,1/800000,1/800000,19487331497/781444412000000,'
 '1001314300627/47566181600000,1/800000,6101786845061/95132363200000,'
 '19640941861/6795168800000,1/800000,1/800000,1/800000,1326387507069/95132363200000,'
 '155682221/25142124560000000,155682221/25142124560000000,'
 '969901373288483/5782688648800000,1627075388860003/11721666180000000,'
 '14139282599219/169879220000000,165067666637733/7814444120000000,'
 '1696529496568917/144567216220000000,31271973479/25142124560000000,'
 '12993863727852929/4047882054160000000,7517305745629/5782688648800000,'
 '36686587724849/3907222060000000,1308842702731/169879220000000,'
 '331925821992147/7814444120000000,54684907960963337/2023941027080000000').split(',')))
x=X[IX[(0,3)]]
assert X[IX[(1,3)]]==x
coeff={1:(12,8,1,13,8), 2:(3,13,7,4,2), 5:(-15,-21,-8,-17,-10)}
# integer numerator of atom mass transfer; the actual M is M36/36
M36=[]; labels=[]
for j in J:
 for i in range(1,6):
  v=[0]*28;h=[0]*7;h[0]=R[i]-R[6];h[i]=R[6]-R[0];h[6]=R[0]-R[i]
  for k,a in enumerate(h):
   v[IX[(k,j)]]+=coeff[j][i-1]*a
   v[IX[(k,3)]]-=coeff[j][i-1]*a
  M36.append(tuple(v));labels.append((j,i))
H=[0]*28
for i,v in ((1,-23),(2,28),(6,-5)):
 H[IX[(i,3)]]=v;H[IX[(i,1)]]=-v
assert sum(H)==0
N=1<<15
# all prefix 36*P(S) integer vectors
P=[None]*N;P[0]=(0,)*28
for mask in range(1,N):
 bit=mask&-mask; ix=bit.bit_length()-1; prev=P[mask^bit]; P[mask]=tuple(prev[k]+M36[ix][k] for k in range(28))
max_eps=F(9,115400000)
T0={-36*x/p[IX[(0,3)]] for p in P if p[IX[(0,3)]]<0 and 0<-36*x/p[IX[(0,3)]]<max_eps}
assert len(T0)==1144
# assert observer kernel each move and H
for v in M36+[tuple(H)]:
 for i in range(7): assert sum(v[IX[(i,j)]] for j in PORTS)==0
 for j in PORTS:
  assert sum(v[IX[(i,j)]] for i in range(7))==0
  assert sum(R[i]*v[IX[(i,j)]] for i in range(7))==0

def spectrum(eta):
 newx=tuple(X[k]+eta*H[k] for k in range(28))
 assert min(newx)>0
 D36=P[-1]; assert min(newx[k]+max_eps*D36[k]/36 for k in range(28))>=0
 thresh={}
 for mask in range(1,N):
  ps=P[mask]
  candidates=[(-36*newx[k]/ps[k],k) for k in range(28) if ps[k]<0]
  if not candidates:continue
  t=min(z for z,k in candidates)
  if 0<t<=max_eps:thresh[mask]=(t,tuple(k for z,k in candidates if z==t))
 vals=set(t for t,_ in thresh.values())
 return vals,thresh

def count(eta,eps):
 newx=tuple(X[k]+eta*H[k] for k in range(28))
 # shared positive denominator integer exact endpoint, all subset coordinates
 from math import lcm
 scale=36
 for z in newx:scale=lcm(scale,z.denominator)
 for z in [eps]:scale=lcm(scale,z.denominator)
 scale*=36
 base=[int(z*scale) for z in newx]
 mv=[[int(eps*m*scale/36) for m in v] for v in M36]
 # counts using states built additively in ascending subset order
 states=[None]*N;states[0]=base;ways=[0]*N;ways[0]=1
 for mask in range(1,N):
  bit=mask&-mask; ix=bit.bit_length()-1
  states[mask]=[a+b for a,b in zip(states[mask^bit],mv[ix])]
  if min(states[mask])>=0:
   m=mask
   while m:
    b=m&-m;ways[mask]+=ways[mask^b];m^=b
 return ways[-1]

def order_threshold(eta):
 vals,ts=spectrum(eta)
 return sorted(v for v in vals if v<max_eps),ts

for sg in (+1,-1):
 # first and second collisions using q15 and q12, k=540+sg, 432+sg
 a1=F(sg)*x/(23*(540+sg))  # x/23 * (1 - 540/(540+sg))= sg*x/(23*(540+sg))
 a2=F(sg)*x/(23*(432+sg))
 assert abs(a1)<abs(a2)
 mid=(a1+a2)/2
 extra=(3*a2-a1)/2
 boundary=a2
 for title,eta in [("just-after-first",mid),("second-edge",boundary),("just-after-second",extra)]:
  vals,t=spectrum(eta);new={v for v in vals if 0<v<max_eps and v not in T0}
  print('SIGN',sg,'POINT',title,'ETA',eta,'INTERIOR',len([v for v in vals if v<max_eps]),'MOVING_NEW',len(new),'EXPECTED_SET_MATCH',set(v for v in vals if v<max_eps)==T0|set((x-23*eta)/q for q in (15,12,3)))
 # exact coalescence q12 at k432+sg
 t=(x-23*boundary)/12
 assert t==36*x/(432+sg)
 values,thresholds=spectrum(boundary)
 masks=[s for s,(z,_) in thresholds.items() if z==t]
 new_state={s for s,(z,_) in thresholds.items() if z==t}
 # neighbor values and counts with fixed eta on either side of eps=t
 order_vals=sorted(values)
 ind=order_vals.index(t)
 before=(order_vals[ind-1]+t)/2
 after=(t+order_vals[ind+1])/2
 nb=count(boundary,before);na=count(boundary,after)
 print('SECOND_EDGE_SIGN',sg,'ETA',boundary,'EPS',t,'NEWLY_ZERO_MASKS',len(masks),'ORDER_COUNT_BEFORE',nb,'AFTER',na,'DROP',nb-na)
 assert nb>na>0
print('PASS_R5_EXACT_SECOND_SIGNED_COLLISION')
