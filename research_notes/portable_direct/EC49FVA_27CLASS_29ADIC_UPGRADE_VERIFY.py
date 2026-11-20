"""EC49FVA extension: certify 27 of 29 classes via signed valuations.
Fraction arithmetic only; finite sampling is not the global proof.
"""
from fractions import Fraction as Q
P=29
BETA=Q(3,637)
E=Q(31597745,1653649)
UE=Q(4822040484,8132285009)
U0=Q(21829245984,45529434409)
EXCLUDED={1,23}

def residue(z):
    assert z.denominator%P
    return (z.numerator*pow(z.denominator,-1,P))%P

def v(z):
    assert z!=0
    a,b,k=z.numerator,z.denominator,0
    while a%P==0:
        a//=P
        k+=1
    while b%P==0:
        b//=P
        k-=1
    return k

def verify(x):
    assert 0<x<1 and x.denominator%P
    r=residue(x)
    assert r not in EXCLUDED
    t0=(1-x)*(1-BETA*x)
    te=(1-x)*(1+BETA*(E-1)*x)
    a=1-t0
    b=1-UE*te
    pm=1-te
    q0=1-U0*t0
    assert 0<pm<a<b<q0<1
    R=t0/(UE*te)
    S=b*R/a
    vr,vs=v(R),v(S)
    if r in {0,20}:
        assert v(a)>0 and (v(t0),v(te))==(0,0)
        assert (vr,vs)==(1,-v(a))
    elif r==19:
        assert v(t0)>=1 and v(te)==0 and v(a)==0
        assert (vr,vs)==(v(t0)+1,v(t0))
    else:
        assert r not in {0,1,19,20,23}
        assert (vr,vs)==(1,0)
    # t=log(R)/log(S) is in (0,1): a rational h/k would
    # require k*vr=h*vs with 0<h<k, impossible in each case.
    assert not (vr>0 and vs>vr)
    return vr,vs

assert set(range(P))-EXCLUDED == (set(range(P))-{0,1,19,20,23})|{0,19,20}
for r in range(P):
    if r in EXCLUDED:
        continue
    x=Q(r,30) if r else Q(29,30)
    assert residue(x)==r
    verify(x)
    for m in (2,4,11):
        d=29*m+1
        for j in range(m+1):
            k=r+29*j
            if 0<k<d:
                x=Q(k,d)
                assert residue(x)==r
                verify(x)
for x in (Q(29,30),Q(20,59),Q(19,30),Q(7,20),Q(1,2),Q(3,4)):
    print('SIGNED_VALUATION_CERTIFICATE',x,residue(x),verify(x))
print('ALL PASS -- 27 residue classes; all finite sample valuations exact')
