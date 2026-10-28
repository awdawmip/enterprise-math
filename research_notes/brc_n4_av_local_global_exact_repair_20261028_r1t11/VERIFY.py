#!/usr/bin/env python3
"""Independent Fraction check: exact AV local minimax, external BRC N4 tree."""
from fractions import Fraction as F
from itertools import product
Z,O=F(0),F(1)
N={1:{'A':(F(1,2),F(1,2)),'B':(F(1,2),F(3,2))},
   2:{'AU':(F(1,6),O),'AV':(F(1,3),F(1,4)),
      'BU':(F(1,4),O),'BV':(F(1,4),F(2))}}
for t in (3,4):
 N[t]={}
 for h,(q,r) in N[t-1].items():
  e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[h] if t==3
     else Z if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
  for j,k in enumerate((-1,1)):N[t][h+str(j)]=(q/2,r*(1+k*e))
for t in N:
 assert all(q>0 and r>0 for q,r in N[t].values())
 assert sum((q for q,r in N[t].values()),Z)==O
 assert sum((q*r for q,r in N[t].values()),Z)==O
T2={'AU':(F(1,2),F(1,6),F(1,3)),'AV':(Z,Z,O),
    'BU':(Z,F(1,2),F(1,2)),'BV':(O,Z,Z)}
T3={'AU0':(Z,O,Z),'AU1':(O,Z,Z),'AV0':(Z,F(1,2),F(1,2)),
    'AV1':(Z,Z,O),'BU0':(Z,Z,O),'BU1':(Z,O,Z)}
def terminal(r):return (Z,O,Z) if r<F(2501,10000) else (O,Z,Z)
def law(s,a0,a1,common=None):
 P2=dict(T2);P2['AV']=(O-s,Z,s)
 P3={h:T3.get(h,(O,Z,Z)) for h in N[3]}
 P3['AV0']=a0;P3['AV1']=a1
 if common is not None:P3['AV0']=P3['AV1']=common
 y=[Z]*16
 for leaf,(q,r) in N[4].items():
  alive=O
  for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
   a=(Z,Z,O) if t==1 else P2[h] if t==2 else P3[h] if t==3 else terminal(N[t][h][1])
   assert all(v>=0 for v in a) and sum(a,Z)==O
   j=2*(t-1)
   y[j]+=q*alive*a[0];y[j+1]+=q*alive*a[1]
   y[8+j]+=q*r*alive*a[0];y[9+j]+=q*r*alive*a[1]
   alive*=a[2]
  assert alive==Z
 assert sum(y[:8],Z)==sum(y[8:],Z)==O
 return y
def tv(x,y):return (sum((abs(x[j]-y[j]) for j in range(8)),Z)/2,
                     sum((abs(x[j]-y[j]) for j in range(8,16)),Z)/2)
def score(y):return y[6]+(y[4]+y[5])/4
A=[(F(i,4),F(j,4),F(4-i-j,4)) for i in range(5) for j in range(5-i)]
assert len(A)==15
count=0
for s in (Z,F(1,7),F(1,2),O):
 for a,b in product(A,repeat=2):
  c=tuple((u+v)/2 for u,v in zip(a,b))
  y=law(s,a,b);z=law(s,a,b,c)
  d=abs(a[2]-b[2])
  assert tv(y,z)==(s*d/24,F(53,4800)*s*d)
  assert abs(score(y)-score(z))==s*d/24
  count+=1
assert count==900
for a,b in [((Z,F(1,2),F(1,2)),(Z,Z,O)),
            ((F(1,3),F(1,6),F(1,2)),(F(1,4),F(1,4),F(1,2)))]:
 for pi in [(O,Z,Z),(Z,O,Z),(Z,Z,O),(F(1,4),F(1,4),F(1,2))]:
  assert abs(score(law(O,a,b))-score(law(O,a,b,pi)))==abs(a[2]-b[2])/24
f0=law(O,(Z,F(1,2),F(1,2)),(Z,Z,O))
assert f0[:8]==list(map(F,['0','0','1/3','11/72','1/36','25/144','1/12','11/48']))
assert f0[8:]==list(map(F,['0','0','7/12','11/72','11/360','19/120','53/2400','127/2400']))
assert tv(f0,law(O,(Z,F(1,2),F(1,2)),(Z,Z,O),(Z,F(1,4),F(3,4))))==(F(1,48),F(53,9600))
print('PASS_EXACT_FRACTION_AV_LOCAL_900 / universal real-parameter proof in PROOF.md / local d=1/48 for F0')
