from fractions import Fraction as F
from math import floor,ceil,gcd
from itertools import product
from pathlib import Path
# Immutable PREFIX-1127 verifier; use its constants only, without rerunning its scan.
exec(Path('prefix1127_verify.py').read_text().split('r=(R[0]')[0])
def mul(a,b):
    v=[u*w for u,w in product(a,b)];return min(v),max(v)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def div(a,b):
    assert b[0]*b[1]>0
    return mul(a,(1/b[1],1/b[0]))
rho_x=36/x**2-1
J=div(mul((-x*x/36,-x*x/36),mul(T,T)),add(T,(x,x)))
S=div(mul(D,J),F1);kappa=sum(S)/2;intercept=c0-kappa*rho_x
P=add(div(B,F1),mul(sub(S,(kappa,kappa)),sub(R,(rho_x,rho_x))))
assert kappa>0 and P[0]>-F(3085,10**95) and P[1]<F(3090,10**95)
V0=((224326691387726790803476148069,88143501759569569282032804965,-21324440778287960813735441752),(-1515201213273875841385829048234,2425796072622968330395221244807,-509314515124052350020117214945),(27129891768577462196953562901254,-25897752315286350056400093345605,5326946603787925837008318389406))
V1=((-1739527904661602632189305196303,2337652570863398761113188439842,-487990074345764389206381773193),(1963854596049329422992781344372,-2249509069103829191831155634877,466665633567476428392646331441),(193392520729861042806628469118813,-241536571370391043454285962151611,50283534702378254816927114461315))
V2=((-1739527904661602632189305196303,2337652570863398761113188439842,-487990074345764389206381773193),(7182438310034137319560696933281,-9262466781694025475170720954403,1930635856604769596011791651020),(591063462451951105177870010237847,-752957322927387565072660671863758,156871199126873195143527095273600))
def scan(L,Q,V):
    r=(R[0]-K/L**2,R[1]);c=(C[0],C[1]+H/L)
    z=add(add(P,mul((kappa,kappa),(F(0),K/L**2))),(F(0),H/L))
    det=dot(V[0],cross(V[1],V[2]));assert abs(det)==1
    W=tuple(tuple(v*det for v in row) for row in zip(cross(V[1],V[2]),cross(V[2],V[0]),cross(V[0],V[1])))
    assert tuple(tuple(dot(v,w) for w in zip(*W)) for v in V)==((1,0,0),(0,1,0),(0,0,1))
    ranges=[]
    for a,b,cc in V:
        vals=[q*(a+cc*intercept+(b+cc*kappa)*rr+cc*zz) for q,rr,zz in product((q0,Q),r,z)]
        ranges.append((ceil(min(vals)),floor(max(vals))))
    ans=[];npoints=0
    for n in product(*(range(a,b+1) for a,b in ranges)):
        npoints+=1;q,p,h=(dot(w,n) for w in W)
        if q0<=q<=Q and gcd(p,q)==1 and r[0]*q<=p<=r[1]*q and c[0]*q<=h<=c[1]*q and z[0]*q<=h-kappa*p-intercept*q<=z[1]*q:ans.append((q,p,h))
    return sorted(ans),ranges,npoints
L0=10**90
old,rs,n=scan(L0,2*10**59,V0);assert len(old)==7 and n==117
print('original seven',rs,n)
lo=[];hi=[];g=d[0]-F(4*E,q0);assert g>0
for q,p,h in old:
    z=F(h,q)-kappa*F(p,q)-intercept;assert z>P[1]
    lower=g/(z-P[0]);upper=(H+kappa*K/L0)/(z-P[1]);lo.append(lower);hi.append(upper)
    print('scale localization',q,float(lower),float(upper))
assert max(hi)<F(2043,1000)*L0
empty,rs,n=scan(10**91,2*10**59,V1);assert not empty and n==0
print('no lines at L>=1e91',rs,n)
new,rs,n=scan(10**100,3*10**60,V2);assert len(new)==115 and n==620
q=new[0][0];assert q==704830121671781357562188570181003663463817577529892083528277
L3=L2=10**8
while L3<=d[0]*q*q/(4*E):L3*=2
while L2<q*q:L2*=2
assert L3>10**100 and L2>10**100
print('new minimum',new[0],rs,n,'count',len(new))
print('first triple',L3,'first sqrt pair',L2)
first=10**8
while first<L0:first*=2
assert 2*first>max(hi)
fixed=[line for line,l,u in zip(old,lo,hi) if l<=first<=u]
assert len(fixed)==4 and fixed[0][0]==157915136333228082417423528698944751801766005910505403078499
print('fixed dyadic survivors',first,len(fixed),fixed[0][0])
