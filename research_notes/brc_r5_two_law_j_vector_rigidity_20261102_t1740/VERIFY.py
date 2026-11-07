"""Standalone exact R5 J-vector support certificate, 2026-11-02."""
from fractions import Fraction as F
from itertools import product

def obs(t,p):
    a,b,c,d,U,V=t; x,j,h,*k=map(F,p)
    D1=(1-j)/8; D2=(1-x)*(1-h)/8
    w=(F(1,4),(1-x)/4,D1,D2)
    C=[w[i]*(1-k[i]) for i in range(4)]
    S=sum(C);D=D1+D2
    return (1-a*D1-b*D2-sum(U[i]*C[i] for i in range(4)),
            c*D1+d*D2+sum(V[i]*C[i] for i in range(4)),
            F(5,2)-3*x/4+2*D+3*S/2,
            F(5,2)-3*x/4+2*D+4*S/3)

def lr(x,y,z):return(x,y,y,z,z,z,z)
def dot(n,o):return sum(x*y for x,y in zip(n,o))
def direction(s,L):return ((1,0) if L==0 else (0,-1))+(-2*s,9*s/4)

S=[F(3,5),F(7,20),F(2,5),F(3,4)]
U=(F(1,4),F(2,3),F(5,8),F(3,7))
V=(F(1,3),F(4,5),F(2,7),F(9,20))
cases=[(*S,U,V),(F(1,2),F(1,2),F(1,4),F(3,4),U,V),
       (F(1,4),F(3,4),F(1,2),F(1,2),U,V),
       (F(1,3),F(2,3),F(3,5),F(2,5),(F(2,5),)*4,(F(7,10),)*4),
       (F(2,3),F(1,3),F(2,5),F(3,5),U,V),
       (F(1,2),F(1,2),F(1,2),F(1,2),U,V)]
checks=0
for m,t in enumerate(cases):
    Fv=[obs(t,p) for p in product((0,1),repeat=7)]
    Lv=[obs(t,lr(*p)) for p in product((0,1),repeat=3)]
    for L in (0,1):
        z1,z2=t[:2] if L==0 else t[2:4]
        s=z1+z2;n=direction(s,L);base=n[0]+5*s/8
        g=abs(z1-z2)/16
        witness=obs(t,(0,0,1,1,1,1,1) if z1<=z2 else (0,1,0,1,1,1,1))
        assert max(dot(n,o) for o in Lv)==base;checks+=1
        assert max(dot(n,o) for o in Fv)==base+g;checks+=1
        assert dot(n,witness)==base+g;checks+=1
        assert sum(abs(i) for i in n)==1+17*s/4;checks+=1
        print('CASE',m,'LAW','P' if L==0 else 'Q','SUPPORT_GAP',g,'WITNESS',witness,'DIST_LINF_LOWER',g/(1+17*s/4))
    # Exact nonbinary time-only Markovization, regardless of answer kernels.
    for q in range(18):
        p=[F(((7*q+11*i*i+5*i)%23)+1,25) for i in range(7)]
        x,j,h,*k=p;d1=(1-j)/8;d2=(1-x)*(1-h)/8
        w=(F(1,4),(1-x)/4,d1,d2)
        y=(j+(1-x)*h)/(2-x);z=sum(w[i]*k[i] for i in range(4))/sum(w)
        assert 0<=y<=1 and 0<=z<=1;checks+=1
        assert obs(t,p)[2:]==obs(t,lr(x,y,z))[2:];checks+=1
print('PASS_EXACT_R5_TWO_LAW_J_VECTOR_PORTABLE',checks,'exact assertions')
