#!/usr/bin/env python3
"""Exact R5 17-edge support, full 4D coupling polytope and atlas-gap verifier."""
from fractions import Fraction as F
def Q(s):return tuple(map(F,s.split()))
R=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y=Q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
K=Q('-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1')
P={
 (0,0):F('33553/432000'), (0,1):F('3997/368000'),
 (4,1):F('3997/690000'), (0,2):F('13091471/3762128400'),
 (2,2):F('8901809/21809440'), (4,2):F('170189123/37621284000'),
 (0,3):F('8294919533/677183112000'), (3,3):F('4095218743/29442744000'),
 (4,3):F('8294919533/188106420000'), (4,5):F('172449787/1363090000'),
 (5,5):F('219439/545236000'), (6,5):F('172449787/2180944000'),
 (6,6):F('38053/432000')
}
NEW=((2,1),(3,1),(3,2),(2,3))
BASIS=(
 {(0,1):-F(10,23),(4,1):-F(13,23),(0,2):F(10,23),(2,2):-F(1),(4,2):F(13,23)},
 {(0,1):-F(5,23),(4,1):-F(18,23),(0,3):F(5,23),(3,3):-F(1),(4,3):F(18,23)},
 {(0,2):-F(5,23),(4,2):-F(18,23),(0,3):F(5,23),(3,3):-F(1),(4,3):F(18,23)},
 {(0,2):F(10,23),(2,2):-F(1),(4,2):F(13,23),(0,3):-F(10,23),(4,3):-F(13,23)}
)
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
SB=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5))
ATLAS=set(SA)|set(SB)
ALLOWED=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
DUAL=[F(0)]*21
for k,v in {0:'-28/5',1:'-84/23',2:'-3',3:'-51/23',7:'28/5',8:'6',9:'6',10:'163/23',15:'-4',16:'-4',17:'-112/23'}.items():DUAL[k]=F(v)
PHI={0:F(23,5),1:F(3),2:F(2),3:F(1),7:-F(23,5),8:-F(5),9:-F(5),10:-F(5),15:F(4),16:F(4),17:F(4)}
def mass(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
 g,a,b,u,v,w,z=f
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)
def slack(f):
 g,a,b,u,v,w,z=f
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
         w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def eq_col(e):
 i,j=e; v=[F(0)]*21;v[i]=F(1);v[7+j]=F(1);v[14+j]=R[i];return v
def rank(rows):
 m=[list(map(F,r)) for r in rows]; p=0
 for col in range(len(m[0])):
  idx=next((i for i in range(p,len(m)) if m[i][col]),None)
  if idx is None:continue
  m[p],m[idx]=m[idx],m[p];scale=m[p][col];m[p]=[x/scale for x in m[p]]
  for i in range(p+1,len(m)):
   if m[i][col]:
    coef=m[i][col];m[i]=[a-coef*b for a,b in zip(m[i],m[p])]
  p+=1
  if p==len(m):break
 return p
def phi_price(e):
 i,j=e;return PHI.get(i,F(0))+PHI.get(7+j,F(0))+R[i]*PHI.get(14+j,F(0))
def gap_price(e):
 i,j=e;return F(int(e not in ATLAS))-DUAL[i]-DUAL[7+j]-R[i]*DUAL[14+j]
def edges(q):
 E=dict(P)
 for e,t,basis in zip(NEW,q,BASIS):
  E[e]=t
  for edge,c in basis.items():E[edge]+=t*c
 return E
def check(E,mu,nu):
 assert all(w>=0 for w in E.values()) and set(E)<=set(ALLOWED)
 for i in range(7):
  assert sum((v for (a,b),v in E.items() if a==i),F(0))==mu[i]
 for j in range(7):
  assert sum((v for (a,b),v in E.items() if b==j),F(0))==nu[j]
  assert sum((R[a]*v for (a,b),v in E.items() if b==j),F(0))==R[j]*nu[j]
nu=mass(X);mu=mass(Y)
assert sum(nu)==sum(mu)==1 and all(w>=0 for w in slack(X)+slack(Y))
assert times(X)==times(Y)==(F('17609/6000'),F('33857/12000'))
assert mu[1]==nu[4]==0 and len(ALLOWED)==30
assert all(phi_price(e)>=0 for e in ALLOWED)
b=mu+nu+tuple(R[j]*nu[j] for j in range(7))
assert sum(PHI.get(i,F(0))*v for i,v in enumerate(b))==0
Z=tuple(e for e in ALLOWED if phi_price(e)==0 and mu[e[0]]>0)
assert len(Z)==17 and set(Z)==set(P)|set(NEW)
assert all(gap_price(e)>=0 for e in ALLOWED)
assert [gap_price(e) for e in NEW]==[F(0),F(28,23),F(5,23),F(13,23)]
assert rank([[eq_col(e)[k] for e in P] for k in range(21)])==13
assert rank([[eq_col(e)[k] for e in Z] for k in range(21)])==13
for e,B in zip(NEW,BASIS):
 assert all(eq_col(e)[k]+sum((v*eq_col(x)[k] for x,v in B.items()),F(0))==0 for k in range(21))
check(P,mu,nu)
c=F('225713944957/3385915560000')
assert sum((DUAL[k]*b[k] for k in range(21)),F(0))==c
assert sum((v for e,v in P.items() if e not in ATLAS),F(0))==c
ep=F(1,1000000);E=edges((ep,)*4);check(E,mu,nu)
assert len(E)==17 and min(E.values())==ep
assert sum((v for e,v in E.items() if e not in ATLAS),F(0))==c+F(1,500000)
end=F('3997/390000')
for q,n in [((F(0),)*4,13),((end/2,F(0),F(0),F(0)),14),((end,F(0),F(0),F(0)),13)]:
 E=edges(q);check(E,mu,nu)
 assert sum(v>0 for v in E.values())==n
 assert sum((v for e,v in E.items() if e not in ATLAS),F(0))==c
for h in (F('-295513/49400000'),F(0),F('295513/36054360')):
 xx=tuple(x+h*k for x,k in zip(X,K))
 assert all(v>=0 for v in slack(xx)) and mass(xx)==nu and times(xx)==times(Y)
print('PASS_30_EDGE_PHI_NONNEGATIVE_AND_EXACT_SATURATION')
print('PASS_ALL_FEASIBLE_SUPPORT_IS_17_EDGE_SET',len(Z))
print('PASS_FULL_TRANSPORT_POLYTOPE_RANK_13_NULLITY_4')
print('PASS_FOUR_INDEPENDENT_EXPLICIT_KERNEL_BASIS')
print('PASS_STRICT_17_EDGE_EXACT_INTERIOR_WITNESS',ep)
print('EXACT_ALL_FEASIBLE_ATLAS_GAP_FORMULA',c,'+ 28/23*q2 + 5/23*q3 + 13/23*q4')
print('PASS_OPTIMAL_SEGMENT_Q1_IN',0,end,'Q2_Q3_Q4_ZERO')
print('PASS_FULL_PHYSICAL_FIBER_TIMES_FOUR_DIM_COUPLING_POLYTOPE')
