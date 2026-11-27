from fractions import Fraction as F
from math import gcd, floor, ceil, isqrt
from itertools import product
from collections import Counter

E=400000; L=10**90; Q=2*10**59
q0=544447235321021556325566186117974922693
R=tuple(F(v,10**95) for v in (2144003672040464398327479053201895915383511059209519307682385914713370011963832308188034970238138,2144003672040464398327479053201895915383511059209519307682385914713370011963832308188034997970814))
C=tuple(F(v,10**95) for v in (9914101043768065462450064423603705069195427225553607117376972848962694844883675852942227093660291,9914101043768065462450064423603705069195427225553607117376972848962694844883675852942227226766253))
T=tuple(F(v,10**95) for v in (126659995644219604163996478285389021613125848769777025941085307762759121792259973708930351798842,126659995644219604163996478285389021613125848769777025941085307762759121792259973708930352581511))
d=tuple(F(v,10**85) for v in (96908626596415488199625924806903600960651737707918479478269855625061455284941067578033,96908626596415488199625924806903600960651737707918479478269855625061455285040066368357))
x=F(1266599956442196041639964782853890216131258487697770259410853077627591217922599737089303521901765,10**96)
c0=sum(C)/2; assert T[0]<=x<=T[1]
# Outward-quantized BRC observer certificate from batch_joint.py.
s=F(-11634884889781635619562764508733,500000000000000000000000000000)
B=tuple(F(v,10**110) for v in (-29563782680394916876739371429,29518261340403151337066718651))
D=tuple(F(v,10**30) for v in (1627485539561293395435538730916079508360030,1627485539561293395435538730916079508360031))
F1=tuple(F(v,10**30) for v in (-9569233600936582651958077026760045106905,-9569233600936582651958077026760045106904))
assert F1[1]<0 and q0>16*E/d[0]
K=d[1]+F(2*E,q0);H=2*d[1]+F(4*E,q0)
V=((-224326691387726790803476148069,-88143501759569569282032804965,21324440778287960813735441752),(-23812108652948012001441004278322,10986580739434895869593113952,237808308129791510604566865691),(15791433389430059226754366936087,-141352059143984074653323213130,-128714040683492997026356269828))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
det=dot(V[0],cross(V[1],V[2]));assert abs(det)==1
W=tuple(tuple(v*det for v in row) for row in zip(cross(V[1],V[2]),cross(V[2],V[0]),cross(V[0],V[1])))
assert tuple(tuple(dot(v,w) for w in zip(*W)) for v in V)==((1,0,0),(0,1,0),(0,0,1))
r=(R[0]-K/L**2,R[1]);c=(C[0],C[1]+H/L)
ranges=[]
for a,b,cc in V:
    z=[q*(a+b*rr+cc*cs) for q,rr,cs in product((q0,Q),r,c)]
    ranges.append((ceil(min(z)),floor(max(z))))
# Complete integer enumeration (27,950 box points; filter exact inequalities).
ans=[]
for n in product(*(range(a,b+1) for a,b in ranges)):
    q,p,h=(dot(row,n) for row in W)
    if q0<=q<=Q and gcd(p,q)==1 and r[0]*q<=p<=r[1]*q and c[0]*q<=h<=c[1]*q:ans.append((q,p,h))
assert len(ans)==len(set(ans));ans.sort()
def mul(a,b):
    v=[u*w for u,w in product(a,b)];return min(v),max(v)
G=10**130
counts=Counter();remaining=[];margins=[]
for q,p,h in ans:
    rr=(max(R[0],F(p,q)),min(R[1],F(p,q)+K/L**2));cc=(max(C[0],F(h,q)-H/L),min(C[1],F(h,q)))
    assert rr[0]<=rr[1] and cc[0]<=cc[1]
    z=(36/(1+rr[1]),36/(1+rr[0]))
    t=(max(T[0],F(isqrt(floor(z[0]*G*G)),G)),min(T[1],F(isqrt(floor(z[1]*G*G))+1,G)))
    assert t[0]<=t[1]
    delta=(t[0]-x,t[1]-x);p0,p1=mul(delta,D);v=(B[0]+p0,B[1]+p1)
    target=mul((cc[0]-c0,cc[1]-c0),F1)
    if v[1]<target[0]:counts['below']+=1;margins.append(target[0]-v[1])
    elif v[0]>target[1]:counts['above']+=1;margins.append(v[0]-target[1])
    else:counts['remaining']+=1;remaining.append((q,p,h))
assert len(ans)==595 and counts=={'below':295,'above':293,'remaining':7}
q=remaining[0][0];assert q==103227297686501849015849101643201302351892157120286900838987
assert min(margins)>F(4652,10**84)
first=10**8
while first<=d[0]*q*q/(4*E):first*=2
firstp=10**8
while firstp<q*q:firstp*=2
print('ranges',ranges,'det',det,'count',len(ans),dict(counts))
print('min margin',float(min(margins)),'q lower',q,'first triple',first,'first sqrt pair',firstp)
print('remaining',remaining)
