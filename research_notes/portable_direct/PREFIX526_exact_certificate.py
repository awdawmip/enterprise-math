#!/usr/bin/env python3
"""PREFIX-526 exact symbolic and integer certificate; requires Python 3 and SymPy."""
import itertools, json
from collections import defaultdict
import sympy as sp

STARS = [(0,2,5),(0,3,4),(1,2,4),(1,3,5)]
EDGES = [(0,1),(2,3),(0,2),(1,3),(1,2),(0,3)]
def nearby(j,c):
    return [-(1 if c>0 else -1)*(a+1) for a in STARS[j] if a!=abs(c)-1]
def successor(s):
    j,p,c=s
    k=next(i for i,v in enumerate(STARS) if i!=j and abs(c)-1 in v)
    return [(j,c,v) for v in nearby(j,c) if v!=p]+[(k,c,v) for v in nearby(k,c)]
S=[(j,p,sign*(a+1)) for j in range(4) for a in STARS[j]
   for sign in (-1,1) for p in nearby(j,sign*(a+1))]
I={s:i for i,s in enumerate(S)}
NEXT=[[I[v] for v in successor(s)] for s in S]
T=I[(0,1,-3)]
assert len(S)==48 and all(len(v)==3 for v in NEXT) and T not in NEXT[T]
FIX=[p for p in itertools.permutations(range(4)) if {p[0],p[1]}=={0,1}]
assert len(FIX)==4
def move(st,p):
    j,prev,cur=st
    def axis(a):return EDGES.index(tuple(sorted(p[k] for k in EDGES[a])))
    def signed(c):return (1 if c>0 else -1)*(axis(abs(c)-1)+1)
    return STARS.index(tuple(sorted(axis(a) for a in STARS[j]))),signed(prev),signed(cur)
orbits=[]
seen=set()
for i,s0 in enumerate(S):
    if i in seen:continue
    orbit=sorted({I[move(s0,p)] for p in FIX})
    assert len(orbit)==4
    orbits.append(orbit);seen.update(orbit)
assert len(orbits)==12 and len(seen)==48
cls={v:i for i,o in enumerate(orbits) for v in o}
x,t,q,u=sp.symbols('x t q u')
W=sp.zeros(48)
for a,s0 in enumerate(S):
    for b in NEXT[a]:
        W[b,a]=x**(int(abs(s0[2])==1)+int(abs(S[b][2])==1))
Q=sp.zeros(12)
for a in range(12):
    y=W*sp.Matrix([int(cls[k]==a) for k in range(48)])
    for b,orb in enumerate(orbits):
        vals={sp.expand(y[z]) for z in orb}
        assert len(vals)==1
        Q[b,a]=vals.pop()
sgn=lambda v:1 if v==1 else (-1 if v==-1 else 0)
cats=(-1,0,1)
vec={c:sp.Matrix([int(sgn(S[o[0]][2])==c) for o in orbits]) for c in cats}
assert all(sum(vec[c][i] for c in cats)==1 for i in range(12))
F={c:(sp.eye(12)-2*t*Q).inv()*vec[c] for c in cats}
G={c:(sp.eye(12)-2*t*Q.T).inv()*vec[c] for c in cats}
qt=cls[T]
for c in cats:
    assert sp.cancel((Q**2*F[c])[qt]-9*x**2*G[c][qt])==0
J=t**2*sum(x**(-abs(a-b))*G[a][qt]*(Q**2*F[b])[qt]
           for a in cats for b in cats)
A=1-2*t-48*(1+q)*t**3-144*q*t**4-864*q*t**5
B=1+2*t+48*(1+q)*t**3-144*q*t**4+864*q*t**5
U=(1+2*t)*(1+2*t+12*t**2)*B
Vm=8*t**2*(1+12*t**2)**2
Vp=8*t**3*(15552*q*t**6+1296*q*t**4+864*t**4+48*q*t**2+84*t**2+5)
N=sp.expand((U+Vm+Vp)**2+(q-1)*(Vm**2+Vp**2))
Jc=9*q*t**2*N/(A*B)**2
assert sp.cancel(J.subs(x,sp.sqrt(q))-Jc)==0
assert sp.cancel(Jc.subs(q,1)-9*t**2/(1-6*t)**2)==0
assert sp.gcd(N,A*B)==1
E=1-4*u-(192+480*q)*u**2-(2304+8064*q+2304*q**2)*u**3 \
  -(82944*q+62208*q**2)*u**4-746496*q**2*u**5
assert sp.expand(A*B-E.subs(u,t**2))==0
numer=sp.Poly(sp.expand(9*q*t**2*N),t)
even=sum(c*u**(k[0]//2) for k,c in numer.terms() if k[0]%2==0)
odd=sum(c*u**(k[0]//2) for k,c in numer.terms() if k[0]%2==1)
assert sp.gcd(even,E)==1 and sp.gcd(odd,E)==1
# Direct independent integer DP over native branch-labeled paths.
states={(i,i,2,0):(1,0) for i in range(48)}
den=sp.Poly(sp.expand(E.subs(u,t**2)**2),t)
num=sp.Poly(sp.expand(9*q*t**2*N),t)
coeff={}; observed={}
for d in range(10):
    hist=defaultdict(int)
    for (start,end,prev,visits),(count,moment) in states.items():
        z0=sgn(S[start][2]);z1=sgn(S[end][2])
        p2=visits-abs(z1-z0)
        assert p2>=0 and p2%2==0
        if moment:hist[p2//2]+=moment
    observed[d]=dict(sorted(hist.items()))
    value=sp.expand(num.nth(d)-sum(den.nth(j)*coeff[d-j]
          for j in range(1,d+1) if d-j in coeff))
    coeff[d]=value
    assert sp.expand(value-sum(n*q**p for p,n in hist.items()))==0
    if d==9:break
    update=defaultdict(lambda:(0,0))
    for (start,end,prev,visits),(cnt,moment) in states.items():
        for dest in NEXT[end]:
            k=visits+int(abs(S[end][2])==1)+int(abs(S[dest][2])==1)
            for branch in (0,1):
                hit=int(prev==0 and branch==0 and dest==T)
                key=(start,dest,branch,k)
                a,h=update[key]
                update[key]=(a+cnt,h+moment+hit*cnt)
    states=update
out={'verdict':'ALL_CHECKS_PASS','model':'PREFIX-518/525 four-STAR signed-X6',
     'phase_states':48,'axis1_stabilizer':4,'orbit_classes':12,'gate_target':S[T],
     'denominator':'E(t^2,q)^2','generic_order':20,'even_odd_order_each':10,
     'finite_dp_depth':9,'hist_by_depth':{str(d):{str(k):str(v) for k,v in h.items()}
                                              for d,h in observed.items()},
     'specialization':'J(t,1)=9t^2/(1-6t)^2'}
print(json.dumps(out,indent=2))
