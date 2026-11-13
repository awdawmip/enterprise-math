#!/usr/bin/env python3
"""Pure Fraction proof checker: R5 escape mass from a fixed 16-edge atlas."""
from fractions import Fraction as F
def q(s): return tuple(F(v) for v in s.split())
R=q('1/10 1/2 3/4 1 5/4 3/2 19/10')
x=q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
y=q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
SB=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),(0,5),(1,5),(3,5),(4,5),(5,5),(6,5))
S=set(SA)|set(SB)
assert len(S)==16
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
def slacks(f):
 g,a,b,u,v,w,z=f
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
 w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
P={
 (0,0):F('33553/432000'),(0,1):F('3997/368000'),
 (4,1):F('3997/690000'),(0,2):F('13091471/3762128400'),
 (2,2):F('8901809/21809440'),(4,2):F('170189123/37621284000'),
 (0,3):F('8294919533/677183112000'),
 (3,3):F('4095218743/29442744000'),
 (4,3):F('8294919533/188106420000'),
 (4,5):F('172449787/1363090000'),(5,5):F('219439/545236000'),
 (6,5):F('172449787/2180944000'),(6,6):F('38053/432000')}
nu=mass(x);mu=mass(y)
assert len(P)==13 and all(w>0 for w in P.values())
assert all(v>=0 for v in slacks(x)+slacks(y))
assert x[0]==x[2] and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
assert times(x)==times(y)==(F('17609/6000'),F('33857/12000'))
assert sum(nu)==sum(mu)==sum(P.values())==1
assert sum(R[i]*nu[i] for i in range(7))==sum(R[i]*mu[i] for i in range(7))==1
for i in range(7):assert sum(P.get((i,j),F(0)) for j in range(7))==mu[i]
for j in range(7):
 assert sum(P.get((i,j),F(0)) for i in range(7))==nu[j]
 assert sum(R[i]*P.get((i,j),F(0)) for i in range(7))==R[j]*nu[j]
z=[F(0)]*21
for i,v in {0:'-28/5',1:'-84/23',2:'-3',3:'-51/23',
             7:'28/5',8:'6',9:'6',10:'163/23',
             15:'-4',16:'-4',17:'-112/23'}.items():z[i]=F(v)
allowed=[(i,j) for j in (0,1,2,3,5,6) for i in range(7)
         if j not in (0,6) or i==j]
assert len(allowed)==30
for i,j in allowed:
 edge_price=z[i]+z[7+j]+R[i]*z[14+j]
 assert edge_price<=int((i,j) not in S),((i,j),edge_price)
for i,j in P:
 assert z[i]+z[7+j]+R[i]*z[14+j]==int((i,j) not in S)
primal=sum(w for e,w in P.items() if e not in S)
dual=sum(z[i]*mu[i]+z[7+i]*nu[i]+z[14+i]*R[i]*nu[i] for i in range(7))
assert primal==dual==F('225713944957/3385915560000')
delta=nu[3]-mu[3]
assert delta==F('8294919533/147213720000')
assert primal-delta==F('646866587/62702140000')>0
print('PASS_PHYSICAL_SEEDLESS_STOPPING_TIMES_AND_ALL_21_BLACKWELL_EQUATIONS')
print('PASS_30_EXACT_DUAL_EDGE_INEQUALITIES_AND_13_COMPLEMENTARY_EQUALITIES')
print('OPTIMUM_UNION_ESCAPE_COST',primal)
print('ROW3_BASIC_LOWER_BOUND',delta)
print('STRICT_IMPROVEMENT',primal-delta)
print('SHARP_PRIMAL_SUPPORT',len(P),'UNION_SUPPORT',len(S))
