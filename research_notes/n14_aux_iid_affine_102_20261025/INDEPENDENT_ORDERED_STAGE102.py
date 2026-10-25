#!/usr/bin/env python3
"""Independent Stage102 author checker: recurse over every ordered prefix, no
forward count-state coalescing. Exact rationals; finite iid N=14 only."""
from fractions import Fraction as R
from functools import lru_cache

p=[R(1,8),R(1,24),R(5,6)]
q=[R(1,12),R(1,12),R(5,6)]
kk=R(96424629120,78169393)
ll=R(91338977736,78169393)
alpha=R(152150366213667431,438244169232678912)
v101=R(44227501292577155,3423782572130304)
s101=R(1033425075169483,1228800000000000)
h=R(1437504293,26112000000)
A=(5,0,2); B=(12,0,1)
@lru_cache(None)
def price(n,a,b):
 scores={'P':kk*R(2**(a+b),3**a),'Q':ll}
 if n<14:
  scores['C']=1+sum((p[j]*price(n+1,a+(j==0),b+(j==1))[0] for j in range(3)),R(0))
 smallest=min(scores.values())
 return smallest,tuple(k for k in ('P','Q','C') if k in scores and scores[k]==smallest)
assert price(0,0,0)[0]==v101+(kk+ll)*alpha

def check_ordered(u,s):
 errors=[R(0)]*2;times=[R(0)]*2;visits=[0];leaves=[0]
 hits={A:[0,R(0),R(0)],B:[0,R(0),R(0)]}
 def visit(n,a,b,wp,wq):
  visits[0]+=1
  v=(n,a,b)
  if v in hits:
   row=hits[v];row[0]+=1;row[1]+=wp;row[2]+=wq
  if v==A: opt=[('Q',u),('C',1-u)]
  elif v==B: opt=[('Q',s),('C',1-s)]
  else:
   c=price(n,a,b)[1]
   assert len(c)==1
   opt=[(c[0],R(1))]
  for act,w in opt:
   if not w:continue
   px=wp*w;qx=wq*w
   if act=='C':
    assert n<14
    for j in range(3):visit(n+1,a+(j==0),b+(j==1),px*p[j],qx*q[j])
   else:
    leaves[0]+=1
    if act=='Q':errors[0]+=px
    else:errors[1]+=qx
    times[0]+=n*px;times[1]+=n*qx
 visit(0,0,0,R(1),R(1))
 assert hits[A]==[10,R(625,62208),R(625,15552)]
 assert hits[B]==[12,R(48828125,725594112),R(48828125,362797056)]
 assert times[0]>times[1]
 return errors+times,visits[0],leaves[0]
z0,n0,l0=check_ordered(R(0),s101)
z1,n1,l1=check_ordered(R(1),s101-h)
assert z0==[alpha,alpha,v101,R(449462455858132795,36520347436056576)]
assert z1==[R(2586593746940986327,7450150876955541504),
            R(2586593746940986327,7450150876955541504),
            R(751163408448101635,58204303726215168),
            R(22836431111877252545,1862537719238885376)]
assert (n0,l0,n1,l1)==(1039336,692903,1029076,686063)
print('PASS independent full ordered history (start/end)')
print('counts:',(n0,l0,n1,l1))
print('start=',list(map(str,z0)),'end=',list(map(str,z1)))
