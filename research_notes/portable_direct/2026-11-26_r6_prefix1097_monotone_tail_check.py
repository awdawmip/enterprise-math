# Exact rational certificate of PREFIX-1097: inherited BRC observer sign tests.
# No new propagation or external reference calculation.
from fractions import Fraction as F
from math import comb

bl=F(6800006737,5368709120)**2/36
bu=F(3400003369,2684354560)**2/36
v,w=F(469,10000),F(169,3600)
C=[F(114025897,629856),F(118208,2187),F(1637,324),F(4,27)]
Cp=[C[j]+(j+1)*C[j+1] for j in range(3)]+[C[3]]
R=[1,7,42,420]
assert F(25,576)<bl<bu<v<w

def J(C,s,z):
    assert 0<s<z<1
    return sum(C[j]*sum(comb(j,i)*R[i]/(z-s)**i for i in range(j+1)) for j in range(4))

def gmin(a,z):
    assert F(25,576)<=a<z<=w
    d=max(a-bu,bl-z)
    assert d>0
    return F(36,4*36**8)*(36*a)**3/(16**3*4**3)*8*10**9*F(180,13)*d

def consts(C,s,z,x,a,b,k,h=False):
    gm=gmin(a,b)
    if h: gm*=max(a-bu,bl-b)
    K=J(C,s,z)/((1-x)**3*gm*(b-a))
    q=(1-x)/(1-b)
    p=(x/a)*q**k
    return K,q,p

def floor_mode_right(m,k,x):
    # For every m+j, k=k0+shift this bound is checked via slopes below.
    return F(m+6,m+6+k-3)<=x

# Broad monotonic cone, all m>=280000 and k>=21m.
a,b=F(4545,100000),F(45451,1000000)
assert bu<a<b<v
K,q,p=consts(Cp,v,w,v,a,b,21,True)
assert K<2*10**32 and p<F(999503,10**6)
assert F(999503,10**6)**10000<F(1,100)
M=280000; N=1+22*M
assert floor_mode_right(M,21*M,v) and F(1,22)<v
assert p*F(N+22,N)**3<1 and q*F(N+1,N)**3<1
Umon=F(2*10**32*N**3,100**28)
assert Umon<F(1,100)

# Narrower earlier-activation cone: m>=100000, k>=ceil(107m/5).
a0,b0=F(447,10000),F(44701,1000000)
assert bu<a0<b0<v
Kn,qn,_=consts(Cp,v,w,v,a0,b0,0,True)
P=(v/a0)**5*qn**107
assert Kn<8*10**33 and P<F(99366,100000)
assert F(99366,100000)**1000<F(1,570)
assert v/a0<F(21,20)
M=100000; N=1+M+107*M//5
assert floor_mode_right(M,107*M//5,v) and F(5,112)<v
assert P*F(N+112,N)**3<1 and qn*F(N+1,N)**3<1
assert 1+(M+4)+(107*(M+4)+4)//5<2240100
Un=F(8*10**33*2240100**3,570**20)*F(21,20)**4
assert Un<F(1,100)

# Explicit negative sign at k=21m and positive at k=22m, all m>=1000000.
sL,bL=F(446,10000),F(447,10000)
assert bu<sL<bL<a<b<v<w
KL,qL,pL=consts(C,sL,bL,bL,a,b,21)
KR,qR,pR=consts(C,v,w,v,a,b,21)
assert KL<14*10**27 and pL<F(999877,10**6)
assert F(999877,10**6)**10000<F(3,10)
assert KR<2*10**29 and pR<F(999503,10**6)
M=1000000; N=1+22*M
assert F(1,22)>bL and floor_mode_right(M,21*M,v)
assert pL*F(N+22,N)**3<1 and pR*F(N+22,N)**3<1
UL=14*10**27*N**3*F(3,10)**100
UR=F(2*10**29*N**3,100**100)
assert UL+UR<F(1,100)
sP,bP=F(444,10000),F(445,10000)
aP,bP0=F(4347,100000),F(43471,1000000)
assert F(25,576)<aP<bP0<sP<bP<bl
KP,qP,pP=consts(C,sP,bP,sP,aP,bP0,22)
assert KP<13*10**27 and pP<F(999792,10**6)
assert F(999792,10**6)**10000<F(1,7)
N=1+23*M
assert floor_mode_right(M,22*M,sP) and F(1,23)<sP
assert pP*F(N+23,N)**3<1
UP=F(13*10**27*N**3,7**100)
assert UP<F(1,100)
print('PREFIX1097_EXACT_RATIONAL_INEQUALITIES_PASSED')
for label,u in [('broad_monotone',Umon),('narrow_monotone',Un),('negative_left_plus_right',UL+UR),('positive_complement',UP)]:
    print(label,format(float(u),'.12e')) # display only
