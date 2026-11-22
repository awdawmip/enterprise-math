#!/usr/bin/env python3
"""Independent exact rational verification of p17 q12 (6,6) witness indices."""
import json
from fractions import Fraction
P=(2,3,5,7,11,13,17)
def smooth(n):
 for p in P:
  while n%p==0:n//=p
 return n==1
A=[(q,r,17*q+r,17*(17*q+r)-1) for q in range(1,8) for r in range(1,17) if smooth(17*q+r)]
J=list(range(1,17))
V=[]
def vwalk(at,rem,mass,indices):
 if rem==0:
  V.append((mass,indices));return
 for i in range(at,len(A)):
  q,r,a,w=A[i]
  if q<=rem and mass+w<=2331:vwalk(i,rem-q,mass+w,indices+(i,))
vwalk(0,6,0,())
Q=[]
def qwalk(at,cost,counts):
 if at==len(J):
  Q.append((cost,counts));return
 j=J[at];w=17*j-1
 for k in range((565-cost)//w+1):qwalk(at+1,cost+k*w,counts+(k,))
qwalk(0,0,())
Q.sort(key=lambda z:z[0])
assert len(V)==11105 and len(Q)==54000
import sys
data=json.load(open(sys.argv[1]))  # the JSON emitted by the C++ checker
out=[]
for row in data['sample_H012']:
 pair=[]
 for side in ('A','B'):
  item=row[side];vm=V[item['vindex']];q=Q[item['qindex']]
  vind=vm[1];qs=[j for j,k in zip(J,q[1]) for z in range(k)]
  assert sum(1<<i for i in set(vind))==item['vmask']
  assert sum(1<<(j-1) for j in set(qs))==item['qmask']
  cofs=[A[i][2] for i in vind]+qs
  mass=sum(17*a-1 for a in cofs)
  assert mass<=2331
  H=[sum((Fraction(17*a-1,17*a)**k for a in cofs),Fraction()) for k in range(4)]
  pair.append((cofs,mass,H))
 assert all(pair[0][2][k]==pair[1][2][k] for k in range(3))
 delta=pair[0][2][3]-pair[1][2][3]
 assert delta
 out.append({'A':pair[0][0],'B':pair[1][0],'mass_A':pair[0][1],'mass_B':pair[1][1],'delta_H3':str(delta)})
assert len(out)==4
assert min(abs(Fraction(x['delta_H3'])) for x in out)==Fraction(1,647101056)
print(json.dumps({'aliases':out,'sharp_H3_gap':'1/647101056'},indent=2))