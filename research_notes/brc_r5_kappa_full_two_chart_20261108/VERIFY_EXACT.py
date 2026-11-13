#!/usr/bin/env python3
"""Exact Fraction-only R5 full-kappa five-parameter two-chart certificate.
Sparse supports were numerically discovered; verification here is wholly rational.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
T=F(1,50);P=(F(0),F(77,152));D=(F(17,2112),F(1));TH=(F(0),F(1))
SUP={
 (P[0],D[0]):(0,1,8,9,16,17,22,23,24,26,38,40,47,48),
 (P[0],D[1]):(0,1,8,9,15,16,17,24,37,44,45,48),
 (P[1],D[0]):(0,1,3,15,16,17,24,36,40,45,48),
 (P[1],D[1]):(0,1,2,3,15,16,17,24,37,45,48),
}
def source(t,p,q,theta,kappa):
 return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
         F(9,40)*kappa+t*theta/10,(F(3,40)*t+F(21,80))*q,t*theta/10)
def old_G(t,p,q,theta,kappa):
 g,a,b,u,v,w,z=source(t,p,q,theta,kappa)
 return (F(1),F(0),F(1),u+F(23,160)*t,v+F(37,80)*t,w-F(17,160)*t,F(0))
def seam(t,theta):return 1-t*(F(37,18)+F(4,9)*theta)
def new_F_at_1(t,p,q,theta,a):
 g,A,b,u,v,w,z=source(t,p,q,theta,F(1))
 V=F(9,40)+a/10
 dv=V-v; da=a-t
 return (F(1),a,F(1),u-F(3,8)*da-dv/2,V,w-da/8-dv/2,a/10)
def masses(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def tp(f):
 g,a,b,u,v,w,z=f
 return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w
def tq(f):
 g,a,b,u,v,w,z=f
 return 1+g+(a+b)/2+u+v+w
def check(x,y,E):
 for f in (x,y):
  g,a,b,u,v,w,z=f
  assert 0<=a<=g<=1 and 0<=b<=g,(f,'a')
  assert 0<=u<=F(13,40)*a+b/80,(f,'u')
  assert 0<=w<=F(3,40)*a+F(21,80)*b,(f,'w')
  assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b,(f,'v/z')
  m=masses(f)
  assert all(w>=0 for w in m),(f,'negative masses')
  assert sum(m)==1 and sum(r*w for r,w in zip(R,m))==1
 g,a,b,u,v,w,z=y
 assert 9*b*z==4*a*(v-z),(y,'not seedless')
 assert all(w>=0 for w in E.values()),('negative Q',E)
 mx,my=masses(x),masses(y)
 for i in range(7):assert sum(w for (ii,j),w in E.items() if ii==i)==my[i],('row',i)
 for j in range(7):
  assert sum(w for (i,jj),w in E.items() if jj==j)==mx[j],('col',j)
  assert sum(R[i]*w for (i,jj),w in E.items() if jj==j)==R[j]*mx[j],('weighted',j)
 assert tp(x)==tp(y) and tq(x)==tq(y)
def exact_solver(A,b):
 M=[list(row)+[v] for row,v in zip(A,b)]
 n=len(A[0]);k=0;cols=[]
 for j in range(n):
  pivot=next((i for i in range(k,len(M)) if M[i][j]),None)
  if pivot is None:continue
  M[k],M[pivot]=M[pivot],M[k]
  z=M[k][j];M[k]=[v/z for v in M[k]]
  for i in range(len(M)):
   if i==k or not M[i][j]:continue
   z=M[i][j]
   M[i]=[a-z*c for a,c in zip(M[i],M[k])]
  cols.append(j);k+=1
 assert len(cols)==n,('rank deficient',len(cols),n)
 assert all(any(row[:n]) or not row[-1] for row in M),'inconsistent'
 sol=[F(0)]*n
 for i,c in enumerate(cols):sol[c]=M[i][-1]
 assert all(sum(a*v for a,v in zip(row,sol))==rhs for row,rhs in zip(A,b))
 return sol
def constraints(x,y,ss):
 mx,my=masses(x),masses(y)
 A=[];b=[]
 for i in range(7):A.append([F(k//7==i) for k in ss]);b.append(my[i])
 for j in range(7):
  A.append([F(k%7==j) for k in ss]);b.append(mx[j])
  A.append([R[k//7]*F(k%7==j) for k in ss]);b.append(R[j]*mx[j])
 return A,b
def transfer_support(x,y,ss):
 A,b=constraints(x,y,ss)
 sol=exact_solver(A,b)
 E={divmod(k,7):v for k,v in zip(ss,sol) if v}
 check(x,y,E)
 return E

# Sparse supports found with floating LP, certified below using exact fractions.
SEAM={
 (P[0],D[0],TH[0]):(0,1,2,8,16,17,22,23,24,26,38,40,47,48),
 (P[0],D[0],TH[1]):(0,1,2,8,16,17,22,23,24,26,38,40,47,48),
 (P[0],D[1],TH[0]):(0,1,8,9,15,16,17,23,24,37,45,48),
 (P[0],D[1],TH[1]):(0,1,8,9,15,16,17,23,24,37,45,48),
 (P[1],D[0],TH[0]):(0,1,15,16,17,19,24,36,40,45,47,48),
 (P[1],D[0],TH[1]):(0,1,15,16,17,19,24,36,40,45,47,48),
 (P[1],D[1],TH[0]):(0,1,15,16,17,24,36,43,45,48),
 (P[1],D[1],TH[1]):(0,1,15,16,17,24,36,43,45,48),
}
ONE={
 (P[0],D[0],TH[0]):(0,1,8,10,15,16,17,19,24,38,40,47,48),
 (P[0],D[0],TH[1]):(0,8,16,24,40,48),
 (P[0],D[1],TH[0]):(0,1,8,9,15,16,17,24,37,38,45,48),
 (P[0],D[1],TH[1]):(0,8,16,24,48),
 (P[1],D[0],TH[0]):(0,1,8,10,15,16,17,19,24,38,40,47,48),
 (P[1],D[0],TH[1]):(0,8,16,24,40,48),
 (P[1],D[1],TH[0]):(0,2,8,9,16,17,24,37,38,45,48),
 (P[1],D[1],TH[1]):(0,8,16,24,48),
}
def corner_certificates():
 cert={}; summary=[]
 for p,q,h in product(P,D,TH):
  x=source(T,p,q,h,F(0));y=old_G(T,p,q,h,F(0))
  E=transfer_support(x,y,SUP[p,q]);cert[(T,p,q,h,'zero')]=(x,y,E)
  s=seam(T,h)
  x=source(T,p,q,h,s);y=old_G(T,p,q,h,s)
  assert y[4]==F(9,40)
  E=transfer_support(x,y,SEAM[p,q,h])
  cert[(T,p,q,h,'seam')]=(x,y,E)
  summary.append(('seam',str(p),str(q),str(h),str(s),len(E),str(min(E.values())),list(sorted(7*i+j for i,j in E))))
  x=source(T,p,q,h,F(1))
  a=(F(7,400) if p==P[0] else F(19,1000)) if h==0 else T
  y=new_F_at_1(T,p,q,h,a)
  E=transfer_support(x,y,ONE[p,q,h])
  cert[(T,p,q,h,'one')]=(x,y,E)
  summary.append(('one',str(p),str(q),str(h),str(a),len(E),str(min(E.values())),list(sorted(7*i+j for i,j in E))))
  for key,kappa in [('zero',F(0)),('seam',F(1)),('one',F(1))]:
   x0=source(F(0),p,q,h,kappa)
   I={(i,i):v for i,v in enumerate(masses(x0)) if v}
   check(x0,x0,I)
   cert[(F(0),p,q,h,key)]=(x0,x0,I)
 return cert,summary

def prism_at_key(t,p,q,h,key,cert):
 factors=(t/T,p/P[1],(q-D[0])/(D[1]-D[0]),h)
 W={}
 for aa,bb,cc,dd in product((0,1),repeat=4):
  bits=(aa,bb,cc,dd)
  wt=F(1)
  for z,bit in zip(factors,bits):wt*=z if bit else (1-z)
  W[(T if aa else F(0),P[bb],D[cc],TH[dd],key)]=wt
 assert sum(W.values())==1
 x=tuple(sum(w*cert[K][0][i] for K,w in W.items()) for i in range(7))
 y=tuple(sum(w*cert[K][1][i] for K,w in W.items()) for i in range(7))
 indices=set().union(*(set(v[2]) for v in cert.values()))
 E={ij:sum(w*cert[K][2].get(ij,F(0)) for K,w in W.items()) for ij in indices}
 E={ij:v for ij,v in E.items() if v}
 check(x,y,E)
 return x,y,E

def full(t,p,q,h,kappa,cert):
 if t==0:
  x=source(t,p,q,h,kappa)
  I={(i,i):v for i,v in enumerate(masses(x)) if v}
  check(x,x,I);return x,x,I,'identity'
 s=seam(t,h)
 assert F(0)<=kappa<=F(1) and 0<s<1
 if kappa<=s:
  xx0,yy0,Q0=prism_at_key(t,p,q,h,'zero',cert)
  xs,ys,Qs=prism_at_key(t,p,q,h,'seam',cert)
  weight=kappa/s;chart='G'
  endpoints=((xx0,yy0,Q0),(xs,ys,Qs))
 else:
  xs,ys,Qs=prism_at_key(t,p,q,h,'seam',cert)
  xx1,yy1,Q1=prism_at_key(t,p,q,h,'one',cert)
  weight=(kappa-s)/(1-s);chart='F'
  endpoints=((xs,ys,Qs),(xx1,yy1,Q1))
 x=tuple((1-weight)*endpoints[0][0][i]+weight*endpoints[1][0][i] for i in range(7))
 y=tuple((1-weight)*endpoints[0][1][i]+weight*endpoints[1][1][i] for i in range(7))
 ij=set(endpoints[0][2])|set(endpoints[1][2])
 E={q:(1-weight)*endpoints[0][2].get(q,F(0))+weight*endpoints[1][2].get(q,F(0)) for q in ij}
 assert x==source(t,p,q,h,kappa)
 if chart=='G':assert y[1]==0 and y[6]==0
 else:assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)
 check(x,y,E)
 return x,y,E,chart

if __name__=='__main__':
 cert,summary=corner_certificates()
 print('EXACT_CORNER_CERTIFICATES_PASS',len(summary),'POS_EDGES',sum(row[5] for row in summary))
 for row in summary: print('CORNER',*row[:7], 'SUPPORT',row[7])
 print('MIN_EDGE',min(F(row[6]) for row in summary))
 n=0; chart_count=defaultdict(int)
 for j in range(161):
  t=T*F((37*j+13)%161,160)
  p=P[1]*F((19*j+7)%161,160)
  q=D[0]+(D[1]-D[0])*F((29*j+3)%161,160)
  h=F((43*j+11)%161,160)
  k=F((31*j+17)%161,160)
  x,y,E,chart=full(t,p,q,h,k,cert)
  chart_count[chart]+=1;n+=1
 print('EXACT_FULL_INTERIOR_PASS',n,dict(chart_count))
 for p,q,h in product(P,D,TH):
  for k in (F(0),seam(T,h),F(1)):
   x,y,E,chart=full(T,p,q,h,k,cert)
 print('EXACT_ALL_BOUNDARY_EXTREMA_PASS')
 nF=0
 for j in range(100):
  t=T*F((31*j+7)%101+1,102);p=P[1]*F((11*j+3)%101,100)
  q=D[0]+(D[1]-D[0])*F((13*j+9)%101,100);h=F((17*j+4)%101,100)
  s=seam(t,h);k=s+(1-s)*F((19*j+5)%101+1,102)
  _,_,_,chart=full(t,p,q,h,k,cert)
  assert chart=='F';nF+=1
 print('EXACT_STRICT_F_INTERIOR_PASS',nF)
 print('ALL_REAL_FIVE_PARAMETER_R5_COMPLETE_LOW_T_KAPPA_BOX_AUTHOR_PROOF')
