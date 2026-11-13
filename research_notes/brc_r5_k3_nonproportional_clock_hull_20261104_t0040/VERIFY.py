"""Exact nonproportional K3 clock-hull certificate; standard-library fractions."""
from fractions import Fraction as F
from itertools import product

C=(F(1,8),F(1,6),F(1,16),F(3,32))
UP_FULL=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
UP_LR=((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
CHECKS=0
def check(expr):
    global CHECKS
    CHECKS+=1
    assert expr, f'assertion {CHECKS} failed'
def obs(up,js,r,v,p,q):
    x,y,i=up
    w=(C[0],F(1-x,6),F(y,16),F(3*i,32))
    d=F(y,16)+F(3*i,32)
    M=[w[s]*STAGES[js[s]][0] for s in range(4)]
    S=[F(2,3)*M[s]*STAGES[js[s]][1] for s in range(4)]
    U=[S[s]*STAGES[js[s]][2] for s in range(4)]
    return (F(107,128)-F(21*x,128)+d/4-sum(S)/2+sum((p[s]*S[s]/8 for s in range(4)),F(0)),
            F(13,64)+F(3*x,64)-d/2+sum(S)/8+sum((q[s]*S[s]/32 for s in range(4)),F(0)),
            F(3)+sum(M)+F(3,2)*sum(S)+sum((r[s]*U[s] for s in range(4)),F(0)),
            F(3)+sum(M)/2+F(3,8)*sum(S)+sum((v[s]*U[s]/4 for s in range(4)),F(0)))
def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull2(points):
    p=sorted(set(points));lo=[];hi=[]
    for x in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],x)<=0:lo.pop()
        lo.append(x)
    for x in p[::-1]:
        while len(hi)>=2 and cross(hi[-2],hi[-1],x)<=0:hi.pop()
        hi.append(x)
    return lo[:-1]+hi[:-1]
def inside(poly,x):
    return all(cross(poly[j],poly[(j+1)%len(poly)],x)>=0 for j in range(len(poly)))
def dot(a,b):
    return sum((u*v for u,v in zip(a,b)),F(0))
R,L,lam=F(3,5),F(1,4),F(36,35)
V,W=(lam*(3+2*R)-3)/2,(lam*(3+2*L)-3)/2
r=(R,R,L,L);v=(V,V,W,W);p=q=(F(1,2),)*4
check((V,W)==(F(33,50),F(3,10)))
check(R>L>0 and R<1 and 1<lam<2)
check(all(0<r[s]<v[s]<min(F(1),F(3,2)*r[s]) for s in range(4)))
check((3+2*V)/(3+2*R)==(3+2*W)/(3+2*L)==lam)
Fv=[obs(up,st,r,v,p,q) for up in UP_FULL for st in product(range(4),repeat=4)]
Lv=[obs(up,(j,)*4,r,v,p,q) for up in UP_LR for j in range(4)]
check((len(Fv),len(Lv))==(1536,16))
fh,lh=hull2([z[2:] for z in Fv]),hull2([z[2:] for z in Lv])
check(len(fh)==4 and fh==lh)
for z in Fv:check(inside(lh,z[2:]))
for z in Lv:check(inside(fh,z[2:]))
muR=(F(9)+2*V)/(8*(3+R));muL=(F(9)+2*W)/(8*(3+L));m=F(11,30)
check(muR==F(43,120) and muL==F(24,65))
check(muR<m<muL<F(3,8))
A=(2*m-F(3,4)+(4*m*R-V)/6,)*2+(2*m-F(3,4)+(4*m*L-W)/6,)*2
check(A==(F(1,50),F(1,50),-F(1,180),-F(1,180)))
g=min(C[1]*A[1],-C[2]*A[2]-C[3]*A[3]);eps=g/2
check((g,eps)==(F(1,1152),F(1,2304)))
fullW=obs((0,1,1),(3,3,0,0),r,v,p,q)
lrH=obs((0,0,0),(3,)*4,r,v,p,q)
check(fullW==(F(455,576),F(39,256),F(37,10),F(3901,1200)))
check(lrH==(F(865,1152),F(59,256),F(37,10),F(3901,1200)))
check(tuple(a-b for a,b in zip(fullW,lrH))==(F(5,128),-F(5,64),F(0),F(0)))
n0=(F(0),F(0),m,-F(1))
check(max(dot(n0,z) for z in Fv)==dot(n0,fullW))
check(max(dot(n0,z) for z in Lv)==dot(n0,lrH))
check(sum(dot(n0,z)==dot(n0,lrH) for z in Lv)==1)
check(min(dot(n0,lrH)-dot(n0,z) for z in Lv if z!=lrH)==g)
n=(eps,F(0),m,-F(1))
check(max(dot(n,z) for z in Fv)==dot(n,fullW))
check(max(dot(n,z) for z in Lv)==dot(n,lrH))
gap=dot(n,fullW)-dot(n,lrH)
bound=gap/sum(abs(t) for t in n)
check(gap==F(5,294912))
check(bound==F(25,2015872))
print('PARAMETERS R L lambda V W',R,L,lam,V,W)
print('FULL_LR_CLOCK_HULL_EQUAL',fh)
print('EXHAUSTIVE_CLOCK_POINT_TESTS',len(Fv)+len(Lv))
print('MU_R MU_L',muR,muL,'m',m,'A',A,'g',g,'epsilon',eps)
print('W_FULL',fullW,'H_LR',lrH,'n',n)
print('SUPPORT_FULL',max(dot(n,z) for z in Fv),'SUPPORT_LR',max(dot(n,z) for z in Lv))
print('FOUR_DIMENSIONAL_GAP',gap,'L_INFTY_DISTANCE_LOWER',bound)
print('ASSERTIONS',CHECKS)
print('PASS_EXACT_R5_K3_NONPROPORTIONAL_CLOCK_HULL_TRIANGULAR_FAN')
