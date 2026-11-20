"""EC49FVG: exact 5-adic lift and two strict CRT witnesses.

Scientific scope: frozen BRC16943 derived Bernoulli rational observer.
All arithmetic exact; no external dependencies or numerical logarithms.
"""
from fractions import Fraction as F
from math import gcd

BETA=F(3,637)
GAMMA=F(141024,1653649)
U=F(4822040484,8132285009)

def vp(z,p):
    z=F(z)
    assert z!=0
    a,b=abs(z.numerator),z.denominator
    e=0
    while a%p==0: a//=p; e+=1
    while b%p==0: b//=p; e-=1
    return e

def modq(q,mod):
    q=F(q)
    assert gcd(q.denominator,mod)==1
    return (q.numerator*pow(q.denominator,-1,mod))%mod

def values(x):
    T0=(1-x)*(1-BETA*x)
    TE=(1-x)*(1+GAMMA*x)
    a=1-T0
    b=1-U*TE
    R=T0/(U*TE)
    S=R*b/a
    assert 0<a<b<1 and 1<R<S
    return a,b,R,S

def crt(remainders,moduli):
    n,M=0,1
    for r,q in zip(remainders,moduli):
        n+=M*((r-n)*pow(M,-1,q)%q)
        M*=q
    return n,M

# Rational identities and congruences in Z_5
delta=(1-U)/25
kappa=U*(GAMMA-1)/5
assert vp(1-U,5)==2 and vp(GAMMA-1,5)==3
assert modq(delta,25)==9 and modq(kappa,25)==0
assert modq(U*GAMMA,25)==1

counts={5:0,30:0,55:0,80:0,105:0}
for d in range(2,401):
    if d%5==0: continue
    for m in range(1,d):
        if gcd(m,d)>1 or m%5 or m%25==0: continue
        x=F(m,d)
        residue=modq(x,125)
        if residue not in counts: continue
        y=x/5
        a,b,R,S=values(x)
        assert modq(y,5)==1
        assert vp(R,5)==0
        assert vp(a,5)==2+vp(128-3*y,5)
        assert vp(b,5)==2+vp(delta-kappa*y+U*GAMMA*y*y,5)
        va,vb,vs=vp(a,5),vp(b,5),vp(S,5)
        if residue==5:
            assert va>=4 and vb==3 and vs<=-1
        elif residue==105:
            assert va==3 and vb>=4 and vs>=1
        else:
            assert va==vb==3 and vs==0
        counts[residue]+=1
assert counts[5] and counts[105]
print('5_ADIC_LIFT_FINITE_EXACT_PASS',counts)

moduli=[4,3**7,7**5,13**3,125,29**2,673**2,416677**2]
old=[2,3**6,1814,157,None,23,295,168371]
expected_legacy={2:(-2,-4),3:(-6,-12),7:(-2,-4),
                 13:(-1,-2),29:(0,0),673:(0,0),416677:(0,0)}
for newres,expected5 in [(5,(0,-1)),(105,(0,1))]:
    remainders=[newres if r is None else r for r in old]
    m,N=crt(remainders,moduli)
    d=N+1
    assert gcd(m,d)==1 and 0<m<d
    x=F(m,d)
    a,b,R,S=values(x)
    valuations={p:(vp(R,p),vp(S,p))
                for p in [2,3,7,13,5,29,673,416677]}
    assert {p:valuations[p] for p in expected_legacy}==expected_legacy
    assert valuations[5]==expected5
    assert modq(x,125)==newres
    assert all(2*vr==vs for p,(vr,vs) in valuations.items() if p!=5)
    assert 2*valuations[5][0]!=valuations[5][1]
    print('STRICT_CRT_WITNESS_PASS',newres,'m',m,'d',d,'valuation',valuations)
print('ALL PASS')
