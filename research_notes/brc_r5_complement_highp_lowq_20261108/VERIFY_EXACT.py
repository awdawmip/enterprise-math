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

# NEW: complementary high-p/low-q prism, exact 32 corners on ONE linear F face.
# Generated supports below were discovered by floating LP, but the
# result is verified with stdlib Fraction and exact Gaussian elimination.
T=F(1,50); P=F(77,152); D=F(17,2112)
TABLE="""
0,1,2,8,16,17,19,22,23,38,40,47,48|1,8,13
0,8,16,24,40,48|1,8,12,13
0,1,2,8,16,17,19,22,23,38,40,47,48|1,8,13
0,8,16,24,40,48|1,8,12,13
0,1,2,8,16,17,19,22,23,38,40,47,48|1,8,13
0,8,16,24,40,48|1,8,13
0,1,2,8,16,17,19,22,23,38,40,47,48|1,8,13
0,8,16,24,40,48|1,8,13
0,2,16,17,19,23,31,33,47,48|2,3
0,16,24,40,48|1,2,8,12,13
0,2,16,17,19,23,31,33,47,48|2,3
0,16,24,40,48|1,2,8,12,13
0,2,16,17,19,23,31,33,47,48|2,3
0,16,24,40,48|1,2,8,13
0,2,16,17,19,23,31,33,47,48|2,3
0,16,24,40,48|1,2,8,13
0,1,2,16,17,19,22,23,37,38,40,47,48|1,2,8,13
0,1,8,15,16,24,26,40,47,48|1
0,1,2,16,17,19,22,23,37,38,40,47,48|1,2,8,13
0,8,16,24,40,48|1,12
0,1,2,16,17,19,22,23,37,38,40,47,48|1,2,8,13
0,1,8,15,16,24,26,40,47,48|1
0,1,2,16,17,19,22,23,37,38,40,47,48|1,2,8,13
0,8,16,24,40,48|1
0,2,16,17,19,23,31,33,47,48|2,3
0,3,16,24,31,33,40,47,48|2
0,2,16,17,19,23,31,33,47,48|2,3
0,16,24,40,48|1,2,12
0,2,16,17,19,23,31,33,47,48|2,3
0,3,16,24,31,33,40,47,48|2
0,2,16,17,19,23,31,33,47,48|2,3
0,16,24,40,48|1,2
"""
SPECS=[(tuple(map(int,line.split('|')[0].split(','))),
        tuple(map(int,line.split('|')[1].split(','))))
       for line in TABLE.strip().splitlines()]
assert len(SPECS)==32
Z0=(F(0),)*7
M0=masses(Z0)
MC=tuple(tuple(masses(tuple(F(i==j) for i in range(7)))[k]-M0[k]
               for j in range(7)) for k in range(7))
TP0=tp(Z0);TQ0=tq(Z0)
TPC=tuple(tp(tuple(F(i==j) for i in range(7)))-TP0 for j in range(7))
TQC=tuple(tq(tuple(F(i==j) for i in range(7)))-TQ0 for j in range(7))

def vertex(x,support,active):
    n=7+len(support);A=[];rhs=[]
    def row(d,b):
        z=[F(0)]*n
        for i,v in d.items(): z[i]+=v
        A.append(z);rhs.append(b)
    for i in range(7):
        d={7+k:F(1) for k,idx in enumerate(support) if idx//7==i}
        for j in range(7): d[j]=d.get(j,F(0))-MC[i][j]
        row(d,M0[i])
    mx=masses(x)
    for j in range(7):
        row({7+k:F(1) for k,idx in enumerate(support) if idx%7==j},mx[j])
        row({7+k:R[idx//7] for k,idx in enumerate(support) if idx%7==j},R[j]*mx[j])
    row(dict(enumerate(TPC)),tp(x)-TP0)
    row(dict(enumerate(TQC)),tq(x)-TQ0)
    # The common F face: z'=a'/10, v'-z'=9b'/40.
    row({6:F(1),1:-F(1,10)},F(0))
    row({4:F(1),6:-F(1),2:-F(9,40)},F(0))
    for idx in active:
        if idx==0: row({1:F(1),0:-F(1)},F(0))
        elif idx==1: row({2:F(1),0:-F(1)},F(0))
        elif idx==2: row({3:F(1),1:-F(13,40),2:-F(1,80)},F(0))
        elif idx==3: row({5:F(1),1:-F(3,40),2:-F(21,80)},F(0))
        elif idx>=7: row({idx-7:F(1)},F(0))
        else: raise ValueError(idx)
    ans=exact_solver(A,rhs)
    y=tuple(ans[:7])
    E={divmod(k,7):w for k,w in zip(support,ans[7:]) if w}
    assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    check(x,y,E)
    return y,E

def corners():
    V={};num_edges=0;minimum=None
    box=((F(0),T),(P,F(1)),(F(0),D),(F(0),F(1)),(F(0),F(1)))
    for index,bits in enumerate(product((0,1),repeat=5)):
        x=source(*(box[i][b] for i,b in enumerate(bits)))
        y,E=vertex(x,*SPECS[index])
        V[bits]=(y,E)
        positive=[v for v in E.values() if v>0]
        num_edges+=len(positive)
        if positive:
            minimum=min(positive) if minimum is None else min(minimum,*positive)
    print('EXACT_32_F_FACE_CORNERS_PASS', 'EDGES', num_edges, 'MIN_POSITIVE', minimum)
    return V

def exact_mix(V,t,p,q,theta,kappa):
    xx=(t,p,q,theta,kappa)
    low=(F(0),P,F(0),F(0),F(0))
    high=(T,F(1),D,F(1),F(1))
    z=[(v-a)/(b-a) for v,a,b in zip(xx,low,high)]
    y=[F(0)]*7;E={}
    for bits,(target,trans) in V.items():
        weight=F(1)
        for bit,r in zip(bits,z):weight*=r if bit else 1-r
        for i in range(7):y[i]+=weight*target[i]
        for ij,v in trans.items():E[ij]=E.get(ij,F(0))+weight*v
    check(source(*xx),tuple(y),E)
    return tuple(y),E

if __name__ == '__main__':
    V=corners()
    for j in range(101):
        exact_mix(
            V,
            T*F((31*j+11)%101,100),
            P+(1-P)*F((13*j+3)%101,100),
            D*F((19*j+7)%101,100),
            F((23*j+5)%101,100),
            F((29*j+9)%101,100))
    print('EXACT_INTERIOR_REGRESSION_PASS 101')
    print('THEOREM_ALL_REAL_FIVE_PARAMETER_COMPLEMENTARY_F_FACE_PRISM')
