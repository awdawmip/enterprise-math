#!/usr/bin/env python3
"""Exact 16-leaf check; all-real optimality proof is in PROOF.md."""
from collections import defaultdict
from fractions import Fraction as F
from sympy import sqrt, simplify
q={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),)*2,
   'BU':(F(1,5),F(9,5)),'BV':(F(2),)*2}
leaf=[(s,j,k,q[s]*r[s][j]/4,q[s]/4) for s in q for j in (0,1) for k in (0,1)]
assert len(leaf)==16 and all(p>0 and v>0 for s,j,k,p,v in leaf)
assert sum(p for s,j,k,p,v in leaf)==sum(v for s,j,k,p,v in leaf)==1
print('PASS_16_POSITIVE_NORMALIZED_LEAVES')
def tv(a,b):return sum(abs(a.get(k,0)-b.get(k,0)) for k in set(a)|set(b))/2
def build(u,v):
 out={L:defaultdict(F) for L in ('P','Q')}
 for s,j,k,p,z in leaf:
  for L,w in [('P',p),('Q',z)]:
   if s in ('AV','BV'):out[L][(('E','-',0),'-','-')]+=w
   elif s=='AU':out[L][(('A','-',0),'-','-')]+=w
   else:
    c=u if j==0 else v
    out[L][(('B',j,0),'-','-')]+=w*(1-c)
    out[L][(('B',j,1),k,k)]+=w*c
 return out
def marginal(law):
 out=defaultdict(F)
 for (s,a,b),w in law.items():out[s]+=w
 return out
def decode(m,p,q,shared=False):
 d=defaultdict(F)
 for s,w in m.items():
  if s[2]:
   if shared:d[(s,0,0)]+=w/2;d[(s,1,1)]+=w/2
   else:
    for a,b,c in [(0,0,(1-p)*(1-q)),(0,1,(1-p)*q),
                  (1,0,p*(1-q)),(1,1,p*q)]:d[(s,a,b)]+=w*c
  else:d[(s,'-','-')]+=w
 return d
for u in (F(0),F(1,4),F(2,3),F(1)):
 for v in (F(0),F(1,4),F(2,3),F(1)):
  D=build(u,v)
  for L,W in [('P',(u+9*v)/40),('Q',(u+v)/8)]:
   m=marginal(D[L]); assert sum(D[L].values())==1
   assert sum(x for s,x in m.items() if s[2])==W
   assert D[L]==decode(m,0,0,True)
   assert tv(D[L],decode(m,F(1,2),F(1,2)))==W/2
  assert (u+9*v)/40-(u+v)/8==(v-u)/10
print('PASS_16_RATIONAL_RATE_PAIRS_PQ_PERSISTENCE_AND_T4_MASSES')
D=build(F(0),F(1));wp,wq=F(9,40),F(1,8)
for p in [F(i,6) for i in range(7)]:
 for q in [F(i,6) for i in range(7)]:
  f=1-min((1-p)*(1-q),F(1,2))-min(p*q,F(1,2))
  assert tv(D['P'],decode(marginal(D['P']),p,q))==wp*f
  assert tv(D['Q'],decode(marginal(D['Q']),p,q))==wq*f
print('PASS_49_NONSTATIONARY_FRESH_COIN_PAIRS_BOTH_LAWS')
a=1-1/sqrt(2)
assert simplify((1-a)**2-F(1,2))==0 and a*a < F(1,2)
assert simplify(1-F(1,2)-a*a-(sqrt(2)-1))==0
assert simplify(wp*(sqrt(2)-1)-9*(sqrt(2)-1)/40)==0
print('PASS_EXACT_RADICAL_SHARP_FRESH_9_TIMES_SQRT2_MINUS_1_OVER_40')
stop={L:defaultdict(F) for L in ('P','Q')}
for s,j,k,p,z in leaf:
 key=s if s in ('AV','BV') else (('AU',j) if s=='AU' else (('BU',0) if j==0 else ('BU',1,k)))
 stop['P'][key]+=p;stop['Q'][key]+=z
assert len(stop['P'])==7 and tv(stop['P'],stop['Q'])==F(43,120)
print('PASS_G4_SEVEN_STOP_ATOMS_TV_43_OVER_120')
print('PASS_BRC_N4_LAWFUL_T4_SEQUENTIAL_SHARP_20261030')
