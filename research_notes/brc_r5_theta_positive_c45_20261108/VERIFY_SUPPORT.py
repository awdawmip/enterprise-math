#!/usr/bin/env python3
"""R5 exact rational 16-corner Blackwell certificates on seedless C_(4/5).
Sparse supports and free variables are in EXACT_SUPPORT_CERTS.json. Standard library only.
"""
import json
from fractions import Fraction as F
from itertools import product
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
C=F(4,5)
def source(t,p,q,theta):
 return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
         t*theta/10+F(27,160),(F(3,40)*t+F(21,80))*q,t*theta/10)
def target(y):
 g,a,b,u,w=y;z=C*a/10
 return (g,a,b,u,z+C*F(9,40)*b,w,z)
def mass(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
 F(13,40)*a+b/80-u,(g-a)/2,
 1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
 (g-b)/2,F(3,40)*a+F(21,80)*b-w,
 u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def tp(f):
 g,a,b,u,v,w,z=f;return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(f):
 g,a,b,u,v,w,z=f;return 1+g+(a+b)/2+u+v+w
def construct_equations(x,support):
 z=target((F(0),)*5)
 basis=[target(tuple(F(k==i) for k in range(5))) for i in range(5)]
 dm=[[mass(basis[j])[i]-mass(z)[i] for j in range(5)] for i in range(7)]
 n=5+len(support);A=[];b=[]
 def put(row,val):assert len(row)==n;A.append(row);b.append(val)
 for i in range(7):
  put([-dm[i][j] for j in range(5)]+[F(s//7==i) for s in support],mass(z)[i])
 for j in range(7):
  put([F(0)]*5+[F(s%7==j) for s in support],mass(x)[j])
  put([F(0)]*5+[R[s//7]*F(s%7==j) for s in support],R[j]*mass(x)[j])
 for fun in (tp,tq):
  put([fun(basis[j])-fun(z) for j in range(5)]+[F(0)]*len(support),fun(x)-fun(z))
 return A,b
def solve_exact(A,b,free_values):
 n=len(A[0]);T=[list(row)+[v] for row,v in zip(A,b)];piv=[];k=0
 for j in range(n):
  idx=next((i for i in range(k,len(T)) if T[i][j]),None)
  if idx is None:continue
  T[idx],T[k]=T[k],T[idx]
  v=T[k][j];T[k]=[t/v for t in T[k]]
  for i in range(len(T)):
   if i==k or not T[i][j]:continue
   v=T[i][j];T[i]=[a-v*c for a,c in zip(T[i],T[k])]
  piv.append(j);k+=1
 assert all(any(row[:n]) or row[n]==0 for row in T)
 free=[j for j in range(n) if j not in piv]
 assert len(free)==len(free_values)
 sol=[F(0)]*n
 for j,v in zip(free,free_values):sol[j]=F(v)
 for row,j in enumerate(piv):sol[j]=T[row][-1]-sum(T[row][i]*sol[i] for i in free)
 assert all(sum(a*v for a,v in zip(row,sol))==b0 for row,b0 in zip(A,b))
 return sol
def check(x,y,E):
 g,a,b,u,w=y;t=target(y);mx,my=mass(x),mass(t)
 assert 0<=a<=g<=1 and 0<=b<=g<=1
 assert 0<=u<=F(13,40)*a+b/80 and 0<=w<=F(3,40)*a+F(21,80)*b
 assert 0<=t[6]<=a/10 and 0<=t[4]-t[6]<=F(9,40)*b
 assert 9*b*t[6]==4*a*(t[4]-t[6])
 assert all(v>=0 for v in list(mx)+list(my)+list(E.values()))
 assert sum(mx)==sum(my)==1
 assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==1
 for i in range(7):assert sum(v for (ii,j),v in E.items() if ii==i)==my[i]
 for j in range(7):
  assert sum(v for (i,jj),v in E.items() if jj==j)==mx[j]
  assert sum(R[i]*v for (i,jj),v in E.items() if jj==j)==R[j]*mx[j]
 assert tp(x)==tp(t) and tq(x)==tq(t)
if __name__=='__main__':
 data=json.load(open('EXACT_SUPPORT_CERTS.json',encoding='utf-8'))
 assert len(data)==16
 corners={};edges=0
 for ts,p,q,th in product((F(1,100),F(1,5)),(F(0),F(1)),(F(0),F(1)),(F(3,4),F(1))):
  key=','.join(map(str,(ts,p,q,th)));D=data[key];S=D['s']
  assert len(S)==len(set(S)) and all(isinstance(j,int) and 0<=j<49 for j in S)
  A,B=construct_equations(source(ts,p,q,th),S)
  sol=solve_exact(A,B,list(map(F,D['f'])))
  y=tuple(sol[:5]);E={divmod(s,7):sol[5+i] for i,s in enumerate(S)}
  check(source(ts,p,q,th),y,E)
  corners[ts,p,q,th]=(y,E)
  edges+=sum(v>0 for v in E.values())
 print('EXACT_16_CORNER_CERTIFICATES_PASS',edges)
 for j in range(257):
  t=F(1,100)+(F(1,5)-F(1,100))*F((17*j+3)%257,256)
  p=F((7*j+19)%257,256);q=F((11*j+23)%257,256)
  theta=F(3,4)+F(1,4)*F((13*j+29)%257,256)
  s=(t-F(1,100))/(F(1,5)-F(1,100));z=4*(theta-F(3,4));W={}
  for a,b,c,d in product((0,1),repeat=4):
   key=(F(1,5) if a else F(1,100),F(b),F(c),F(1) if d else F(3,4))
   W[key]=(s if a else 1-s)*(p if b else 1-p)*(q if c else 1-q)*(z if d else 1-z)
  assert sum(W.values())==1 and all(v>=0 for v in W.values())
  x=source(t,p,q,theta)
  assert all(x[k]==sum(W[v]*source(*v)[k] for v in W) for k in range(7))
  y=tuple(sum(W[v]*corners[v][0][k] for v in W) for k in range(5))
  S=set().union(*(set(cert[1]) for cert in corners.values()))
  E={ij:sum(W[v]*corners[v][1].get(ij,F(0)) for v in W) for ij in S}
  check(x,y,E)
 print('EXACT_257_INTERIOR_REGRESSION_PASS')
 print('PROVED_ALL_REAL_T_1_100_TO_1_5_P_Q_0_TO_1_THETA_3_4_TO_1_KAPPA_3_4_SEEDLESS_C_4_5')
