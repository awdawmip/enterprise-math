#!/usr/bin/env python3
"""PREFIX-1012: exact one-Green reconstruction for frozen X6 BRC signed Link loop.
Scientific model: P000 V5 and Stage46 *candidate* w(h,d)=1-6[h=d].
Only signed terminal-port-summed rooted return is projected; the path/port BRC DP below
serves as an independent finite semantic cross-check. No physical-time claims.
"""
import json
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
from collections import defaultdict

K=40
M=K+1

def convolution(a,b,n):
    out=[Q(0)]*(n+1)
    for i,x in enumerate(a[:n+1]):
        if x:
            for j,y in enumerate(b[:n+1-i]):
                if y: out[i+j]+=x*y
    return out

# Exact six-axis Laurent word coefficients W_{2m,0}, via finite native
# signed-word enumeration by axis multiplicities.
g=[Q(1,factorial(i)**2) for i in range(M+2)]
pow6=[Q(1)]+[Q(0)]*(M+1)
for _ in range(6): pow6=convolution(pow6,g,M+1)
W=[int(factorial(2*m)*pow6[m]) for m in range(M+2)]
assert all(Q(factorial(2*m))*pow6[m]==W[m] for m in range(M+2))

# F(z)=G0(z)= (1+36z^2)^(-1) sum_m W_{2m,0}(z/(1+36z^2))^(2m).
# Use y=z^2, storing y^m coefficients f[m].
f=[sum(W[r]*(-36)**(m-r)*comb(m+r,m-r) for r in range(m+1)) for m in range(M+1)]
assert f[0]==1 and f[1]==-24

# NEW theorem (same y-coordinates): K(z)=G0(z)-G2(z), k[0]=1;
# for m>=1: 12(2m+1)k[m]= f[m+1]-1296 f[m-1].
k=[Q(1)]+[Q(f[m+1]-1296*f[m-1],12*(2*m+1)) for m in range(1,K+1)]
assert all(x.denominator==1 for x in k)

# Independent combinatorial G2: W_{2r,2e1}= W_{2r,0}-W_{2r+2,0}/[12(2r+1)].
# This is a coefficient-level identity derived from the native six-axis Laurent words.
w2=[Q(W[r])-Q(W[r+1],12*(2*r+1)) for r in range(K+1)]
assert w2[0]==0 and w2[1]==1 and all(v.denominator==1 and v>=0 for v in w2)
j_direct=[sum(w2[r]*(-36)**(m-r)*comb(m+r,m-r) for r in range(m+1)) for m in range(K+1)]
assert [Q(f[m])-k[m] for m in range(K+1)]==j_direct

# All remaining algebra is a formal series rewrite of the existing rank-two
# BRC resolvent, not a generic untyped numerical propagation model.
def add(a,b,n=K):
    return [(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0)) for i in range(n+1)]
def mul(a,b,n=K):return convolution(a,b,n)
def inv(a,n=K):
    assert a[0] != 0
    res=[1/a[0]]+[Q(0)]*n
    for m in range(1,n+1):res[m]=-sum((a[r] if r<len(a) else 0)*res[m-r] for r in range(1,m+1))/a[0]
    return res

def z_shift(a,j,n=2*K):return [Q(0)]*j+list(a[:n+1-j])

def zmul(a,b,n=2*K):return convolution(a,b,n)
def zadd(a,b,n=2*K):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n+1)]

def zscale(a,s):return [x*s for x in a]

N=2*K
F=[Q(0)]*(N+1)
Ke=[Q(0)]*(N+1)
for i in range(K+1):F[2*i]=Q(f[i]);Ke[2*i]=k[i]
U=zadd(F,zscale(z_shift(F,2),36));U[0]-=1
R=zscale(zadd(F,zscale(z_shift(F,2),-36)),Q(1,2));R[0]+=Q(1,2)
# P+=1+(1-6z)(zF+U/12)
# P-=1-(1+6z)(zF-U/12)
x=zadd(z_shift(F,1),zscale(U,Q(1,12)))
y=zadd(z_shift(F,1),zscale(U,Q(-1,12)))
Pp=zadd(x,zscale(z_shift(x,1),-6)); Pp[0]+=1
Pm=zscale(zadd(y,zscale(z_shift(y,1),6)),-1);Pm[0]+=1
numer=zmul(R,zadd([Q(1)],[Q(0),Q(0)]+zscale(Ke,-6)))
den=zmul(Pp,Pm)
Lseries=zmul(numer,inv(den,N),N)
assert all(Lseries[2*i+1]==0 for i in range(K))
L=[Lseries[2*i] for i in range(K+1)]
assert all(v.denominator==1 for v in L)
L=[int(x) for x in L]
prior=[1,-25,390,-2365,-49550,1645010,-22026080,78710035,4076647030,-215329002630,7724818416180,-146088496994110,-815898004254020]
assert L[:len(prior)] == prior, (L[:len(prior)],prior)

# Actual signed BRC named-port integer DP for six native axes, independent of
# the Green-series formal calculation. No renormalization, no squaring.
dirs=[tuple(s if j==axis else 0 for j in range(6)) for axis in range(6) for s in (-1,1)]
origin=(0,)*6; e1=(1,0,0,0,0,0)
check={0:1}
for target in range(1,8):
    state={(origin,tuple(-x for x in e1)):1}
    for step in range(1,2*target+1):
        nxt=defaultdict(int)
        remaining=2*target-step
        for (cell,h),val in state.items():
            for d in dirs:
                dest=tuple(x+y for x,y in zip(cell,d))
                if sum(abs(x) for x in dest)>remaining: continue
                if (cell==origin and dest==e1) or (cell==e1 and dest==origin):continue
                wt=1-6*(h==d)
                nxt[(dest,tuple(-x for x in d))]+=val*wt
        state={key:v for key,v in nxt.items() if v}
    measured=sum(v for (x,h),v in state.items() if x==origin)
    assert measured==L[target],(target,measured,L[target])
    check[target]=measured

out={
  "schema":"PREFIX1012_R6_EXACT_ONE_GREEN_CERT_V1",
  "hypothesis":"P000 V5, Stage46 candidate signed BRC, initial incoming h=-e1, chart-root 0, blocked both directions 0<->e1",
  "observer":"signed integer sum over all terminal ports, paths of 2k steps ending at root; NOT squared probability",
  "theorem":"(d/dz)[z(G0-G2)]=(1-36z^2)((1+36z^2)G0-1)/(12z^2)",
  "series_coefficients":"k_0=1; k_m=(f_{m+1}-1296*f_{m-1})/[12*(2m+1)] for m>=1, f_m=[z^(2m)]G0",
  "range":{"scalar_k":[0,K],"independent_BRC_k":[0,7],"G2_combinatorial_k":[0,K]},
  "f0_to_f12":f[:13],"k0_to_k12":[str(x) for x in k[:13]],
  "exact_L_0_to_40":[str(x) for x in L],"independent_BRC_root_coefficients":{str(i):str(v) for i,v in check.items()},
  "validation":["exact six-axis named-word multinomial series","independent displaced-word enumeration relation",
      "one-series vs direct two-series equality for G2","previous PREFIX-1010 L0..L12 exact values",
      "native 12-direction BRC rooted and masked DP L0..L7","all odd coefficients vanish up to z^80"],
  "review_status":"AUTHOR_PROOF_AND_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED"
}
with Path(__file__).with_name('PREFIX1012_R6_EXACT_RESULTS.json').open('w') as h:json.dump(out,h,ensure_ascii=False,indent=2)
print('PASS L0..12',L[:13]);print('NEW L33..40',list(enumerate(L[33:41],33)));print('BRC',check)
