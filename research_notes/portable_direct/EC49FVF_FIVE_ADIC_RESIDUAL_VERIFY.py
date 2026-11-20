"""EC49FVF exact five-adic theorem and seven-prime-compatible CRT witness."""
from fractions import Fraction as F
from math import gcd

BETA=F(3,637)
GAMMA=F(141024,1653649)
U=F(4822040484,8132285009)

def vp(z,p):
    z=F(z)
    assert z!=0
    n,d=abs(z.numerator),z.denominator
    v=0
    while n%p==0: n//=p;v+=1
    while d%p==0: d//=p;v-=1
    return v

def data(x):
    t0=(1-x)*(1-BETA*x)
    te=(1-x)*(1+GAMMA*x)
    a=1-t0
    b=1-U*te
    r=t0/(U*te)
    s=b*r/a
    assert 0<a<b<1 and 1<r<s
    return a,b,r,s

def pair(x,p):
    _,_,r,s=data(x)
    return vp(r,p),vp(s,p)

def crt(residues,moduli):
    x,N=0,1
    for residue,mod in zip(residues,moduli):
        x+=N*((residue-x)*pow(N,-1,mod)%mod)
        N*=mod
    return x,N

assert vp(1-U,5)==2 and vp(GAMMA-1,5)==3
assert vp(1+BETA,5)==1
assert vp(U,5)==vp(BETA,5)==vp(GAMMA,5)==0

counts={'v5_num_ge_2':0,'v5_num_eq_1_unit_minus_1':0}
for d in range(2,401):
    for m in range(1,d):
        if gcd(m,d)!=1 or d%5==0: continue
        x=F(m,d)
        if m%25==0:
            j=vp(m,5)
            a,b,r,s=data(x)
            assert vp(a,5)==j+1 and vp(b,5)==2
            assert (vp(r,5),vp(s,5))==(0,1-j)
            counts['v5_num_ge_2']+=1
        elif m%5==0 and (m//5)*pow(d,-1,5)%5==4:
            a,b,r,s=data(x)
            assert vp(a,5)==2 and vp(b,5)>=3
            assert vp(r,5)==0 and vp(s,5)>=1
            counts['v5_num_eq_1_unit_minus_1']+=1
assert all(counts.values())
print('FINITE_FRACTION_THEOREM_CROSSCHECK_PASS',counts)

moduli=[4,3**7,7**5,13**3,25,29**2,673**2,416677**2]
residues=[2,3**6,1814,157,20,23,295,168371]
m,N=crt(residues,moduli)
d=N+1
assert m==471955466252550476437545415817070
assert d==534065128161609717579116674491301
assert gcd(m,d)==1 and 0<m<d
x=F(m,d)
expected={2:(-2,-4),3:(-6,-12),7:(-2,-4),13:(-1,-2),
          29:(0,0),673:(0,0),416677:(0,0),5:(0,1)}
actual={p:pair(x,p) for p in expected}
assert actual==expected
for p in [2,3,7,13,29,673,416677]:
    vr,vs=actual[p]
    assert 2*vr==vs
assert actual[5]==(0,1) and 2*actual[5][0]!=actual[5][1]
assert (m*pow(d,-1,25))%25==20
print('EIGHT_COORDINATE_STRICT_WITNESS_PASS',str(x),actual)
print('ALL PASS')
