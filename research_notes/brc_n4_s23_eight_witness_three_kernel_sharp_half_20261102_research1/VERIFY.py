"""Exact Fraction certificate, BRC N=4 S23, source pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34."""
from fractions import Fraction as F
from itertools import product
import json
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
AA=(0,0,0,1,1,1);BB=(2,2,3,2,2,4);CC=(5,6,7,8,9,10);G=(0,0,1,2,2,3)
def p(z):
 z=list(map(F,z)); rows=[]
 for a,b,c in zip(AA,BB,CC):
  x,y,t=z[a],z[b],z[c];q=(1-x)*(1-y)
  rows.append((x,(1-x)*y,q*t,q*(1-t)))
 return tuple(tuple(sum(F(M[i][s],20)*rows[s][j] for s in range(6)) for j in range(4)) for i in range(6))
def q(d):
 return tuple(tuple(sum(F(M[i][s],20)*d[G[s]][j] for s in range(6)) for j in range(4)) for i in range(6))
def d(rows):return tuple(tuple(map(F,row.split())) for row in rows.split(';'))
def tv(x,y):return sum(abs(a-b) for a,b in zip(x,y))/2
def L(x,y):return max(tv(a,b) for a,b in zip(x,y))
def O(s,t):return (s,t,0,0,0,0,1,1,1,0,1)
def N(s,t):return (s,t,0,0,0,1,0,0,0,0,0)
raw={'W':(1,0,0,0,1,0,0,0,0,0,0),
     'J':(1,F(1,3),0,0,0,0,0,0,0,1,0),
     'A':O(F(1,7),1),'B':O(1,F(1,7)),
     'C':N(F(1,7),1),'X':O(1,F(1,15)),
     'Y':(1,0,0,0,0,0,0,0,1,1,1),
     'Z':(0,1,0,1,0,1,1,0,0,0,0)}
P={name:p(z) for name,z in raw.items()}
K={
 'WA':d('9/14 0 5/14 0;9/14 0 5/14 0;1/2 0 0 1/2;1/2 1/2 0 0'),
 'JBXY':d('1 0 0 0;1 0 0 0;0 0 1/2 1/2;0 0 1/2 1/2'),
 'CZ':d('1/2 0 1/2 0;0 1/2 0 1/2;1 0 0 0;1 0 0 0')}
for z in raw.values():assert len(z)==11 and all(0<=F(x)<=1 for x in z)
for x in P.values():assert all(sum(row)==1 and min(row)>=0 for row in x)
for k in K.values():assert len(k)==4 and all(sum(row)==1 and min(row)>=0 for row in k)
Q={name:q(k) for name,k in K.items()}
risks={name:{j:str(L(P[name],Q[j])) for j in Q} for name in P}
chosen={name:min(risks[name],key=lambda j:F(risks[name][j])) for name in P}
assert all(F(risks[name][chosen[name]])==F(1,2) for name in P)
pairs=(('W','J',5),('W','A',3),('W','C',3),('W','Y',3),
       ('Y','J',5),('Y','A',3),('Y','C',3))
assert all(tv(P[a][i],P[b][i])==1 for a,b,i in pairs)
mass=sum(P['J'][2][i] for i in (0,1))+P['A'][2][2]+P['C'][2][3]
assert mass==F(19,7) and (mass-1)/3==F(4,7)
five='WJACY'
for colors in product(range(3),repeat=5):
 c=dict(zip(five,colors))
 assert any(c[a]==c[b] for a,b,_ in pairs) or c['J']==c['A']==c['C']
base=('34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12',
      '12 12 24 34','12 13 23 24','23 34 12 13','24 34 12 14')
def pair(s):return tuple(tuple(F(row.count(str(t)),2) for t in range(1,5)) for row in s.split())
D=[q(pair(s)) for s in base]+list(Q.values())
off=('00000000000','00000001000','00000000001','00101000000',
     '00110000000','00101001000','00100000001','00100000000')
off_rows=[];cert_count=0
for h,bits in enumerate(off):
 target=p(bits); v=[L(target,dec) for dec in D]
 assert v[h]==F(1,2) and all(v[j]==1 for j in range(11) if j!=h)
 for j,dec in enumerate(D):
  if j==h:continue
  found=False
  for i in range(6):
   E=[t for t in range(4) if target[i][t]>0]
   if sum(target[i][t] for t in E)==1 and sum(dec[i][t] for t in E)==0:
    found=True;break
  assert found,(h,j)
  cert_count+=1
 off_rows.append({'released':h+1,'policy':bits,'remaining_ten_risks':'1 x 10'})
assert cert_count==80
print(json.dumps({'result':'PASS_BRC_N4_S23_EIGHT_WITNESS_SHARP_HALF_AND_EIGHT_OFF_COUNTEREXAMPLES_20261102',
 'pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
 'eight_witness_risks':risks,'chosen_decoders':chosen,
 'radius':'1/2','singular_pair_certificates':len(pairs),'label_assignments':243,
 'triple_event_mass':str(mass),'exact_full_domain_counterexamples':off_rows,
 'exact_disjoint_support_certificates':cert_count,
 'arithmetic':'Python stdlib Fraction','status':'AUTHOR_EXACT_PROOF_UNREVIEWED_NOT_ADMITTED'},indent=2))
