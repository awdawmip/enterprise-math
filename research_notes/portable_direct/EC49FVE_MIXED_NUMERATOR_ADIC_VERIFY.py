"""EC49FVE: exact rational proofs crosscheck; standard library only."""
from fractions import Fraction as F
from math import gcd

BETA=F(3,637)
GAMMA=F(141024,1653649)
U=F(4822040484,8132285009)

def vp(z,p):
    z=F(z)
    assert z!=0
    n,d=abs(z.numerator),z.denominator
    s=0
    while n%p==0: n//=p; s+=1
    while d%p==0: d//=p; s-=1
    return s

def state(x):
    t0=(1-x)*(1-BETA*x)
    te=(1-x)*(1+GAMMA*x)
    a=x*(640-3*x)/637
    b=1-U*te
    R=t0/(U*te)
    S=b*R/a
    assert 0<a<b<1 and 1<R<S
    return a,R,S

def pair(x,p):
    _,R,S=state(x)
    return vp(R,p),vp(S,p)

def obstructs(z):
    vr,vs=z
    return (vr==0)!=(vs==0) or vr*vs<0 or (vr*vs>0 and abs(vr)>=abs(vs))

assert vp(BETA,7)==-2 and vp(U-1,7)==1
assert vp(BETA,13)==-1 and vp(U-1,13)==0
assert vp(U,2)==2 and vp(U,3)==6 and vp(1+BETA,2)==7

counts={"two_three_both":0,"two_three_mismatch":0,"seven_numerator":0,"seven_certified":0,"thirteen_numerator":0,"thirteen_certified":0}
for d in range(2,401):
    for m in range(1,d):
        if gcd(m,d)!=1: continue
        x=F(m,d)
        if m%6==0:
            A=vp(state(x)[0],2);q=vp(m,3)
            assert pair(x,2)==(-2,-2-A)
            assert pair(x,3)==(-6,-6-q)
            if q!=3*A:
                assert (-2)*(-6-q)!=(-6)*(-2-A)
                counts['two_three_mismatch']+=1
            counts['two_three_both']+=1
        if m%7==0:
            j=vp(m,7);z=pair(x,7)
            r=vp(1-BETA*x,7)
            if j==1: assert z[0]==-1 and z[1]>=1
            elif j==2: assert z==(r,r+1)
            else: assert z==(0,3-j)
            cert=(j==1 or j>=4 or (j==2 and ((m//49)*pow(d,-1,7))%7!=2))
            if cert: assert obstructs(z);counts['seven_certified']+=1
            counts['seven_numerator']+=1
        if m%13==0:
            j=vp(m,13);z=pair(x,13)
            if j==1:
                r=vp(1-BETA*x,13)
                assert z==(r,r)
            else: assert z==(0,1-j)
            cert=(j>=2 or (j==1 and ((m//13)*pow(d,-1,13))%13==12))
            if cert: assert obstructs(z);counts['thirteen_certified']+=1
            counts['thirteen_numerator']+=1
print('FINITE_FRACTION_CROSSCHECK_PASS', counts)

def crt(rs,ms):
    z,N=0,1
    for r,m in zip(rs,ms):
        k=((r-z)*pow(N,-1,m))%m
        z+=N*k;N*=m
    return z,N

num,mod=crt([4,729,1814,157],[8,3**7,7**5,13**3])
den=mod+1
assert (num,mod,den)==(481394062332,646039432584,646039432585)
assert gcd(num,den)==1 and 0<num<den
x=F(num,den);a,R,S=state(x)
assert (vp(a,2),vp(a,7),vp(a,13),vp(num,3))==(4,2,1,6)
ps={p:pair(x,p) for p in (2,3,7,13)}
assert ps=={2:(-2,-6),3:(-6,-12),7:(-2,-4),13:(-1,-2)}
assert all(2*vr==vs for p,(vr,vs) in ps.items() if p in (3,7,13))
assert 3*ps[2][0]==ps[2][1]
print('FOUR_PRIME_JOINT_EXCEPTION_WITNESS_PASS', str(x),ps)
print('ALL PASS')
