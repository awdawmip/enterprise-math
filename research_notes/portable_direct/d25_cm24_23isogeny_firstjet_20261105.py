#!/usr/bin/env python3
"""D25 CM(-24): exact 2/3-isogeny first-jet symbolic and finite certificate.
2026-11-05. Author-side auxiliary, not original native H0/B0 experiment.
Requires SymPy for rational quotient-ring identities; finite prime checks stdlib.
"""
from math import isqrt
import sympy as S

z,X,u0,A0,B0=S.symbols('z X u A B')
Q=z**4-140*z**3+294*z**2-140*z+1
def R(v):
    n,d=S.fraction(S.cancel(v))
    return S.rem(n*S.invert(d,Q,z),Q,z)
def prod(*xs):
    a=S.Integer(1)
    for x in xs:a=R(a*x)
    return a
def quot(a,b):return R(a*S.invert(b,Q,z))

def symbolic():
    g0=3*u0**2+A0;f0=u0**3+A0*u0+B0
    xx=X+2*g0/(X-u0)+4*f0/(X-u0)**2
    yy=1-2*g0/(X-u0)**2-8*f0/(X-u0)**3
    A3g=A0-10*g0;B3g=B0-14*(5*u0**3+3*A0*u0+2*B0)
    num=S.together((X**3+A0*X+B0)*yy**2-(xx**3+A3g*xx+B3g)).as_numer_denom()[0]
    psi=3*u0**4+6*A0*u0**2+12*B0*u0-A0**2
    assert S.rem(num,psi,u0)==0
    e=R((z**3-141*z**2+427*z-7)/192)
    a=R(z-(1+z)**2/S.Integer(3))
    b=R(-2*(1+z)**3/S.Integer(27)+(1+z)*z/S.Integer(3))
    ad=R(S.diff(z-(1+z)**2/S.Integer(3),z))
    bd=R(S.diff(-2*(1+z)**3/S.Integer(27)+(1+z)*z/S.Integer(3),z))
    assert R(3*e**4-4*(1+z)*e**3+6*z*e**2-z*z)==0
    pe=prod(12,e,e-1,e-z)
    ep=quot(R(4*e**3-6*e**2+2*z),pe)
    assert ep==R(-(z**3-133*z**2-677*z+673)/384)
    v=R(e-(1+z)/S.Integer(3));vd=R(ep-S.Rational(1,3))
    g=R(3*v*v+a);gd=R(6*v*vd+ad)
    w=R(5*v**3+3*a*v+2*b)
    wd=R(15*v*v*vd+3*ad*v+3*a*vd+2*bd)
    a3=R(a-10*g);b3=R(b-14*w)
    a3d=R(ad-10*gd);b3d=R(bd-14*wd)
    assert a3==R(-3*(z*z+14*z+1)/4)
    assert b3==R((z+1)*(z*z-34*z+1)/4)
    h=quot(1+2*z-7*z*z,16*z*(1-z*z))
    for cls,f in [('split',quot(7-5*z,5-7*z)),
                  ('inert',quot(5-7*z,7-5*z))]:
        s2=quot(-(1+f),2*(1+z))
        s3=prod(S.Rational(-2,3),s2)
        af=R(f-(1+f)**2/S.Integer(3))
        bf=R(-2*(1+f)**3/S.Integer(27)+(1+f)*f/S.Integer(3))
        afd=R((1-2*f)/3)
        bfd=R(-2*(1+f)**2/S.Integer(9)+(1+2*f)/3)
        assert R(af-prod(s3,s3,a3))==0
        assert R(bf-prod(s3,s3,s3,b3))==0
        det=R(3*bf*afd-2*af*bfd)
        f3d=quot(R(3*bf*prod(s3,s3,a3d)
                  -2*af*prod(s3,s3,s3,b3d)),det)
        alpha3=quot(R(afd*f3d-prod(s3,s3,a3d)),2*af)
        f2d=quot(-4*f*(1+f),(1-z*z)*(1-f))
        alpha2=R(quot(f2d,1+f)-quot(1,1+z))
        assert R(f3d+f2d)==0,cls
        assert R(alpha2+alpha3+4*h)==0,cls
    return True

def primes(limit):
    for p in range(5,limit+1):
        if p%8==5 and all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def finite(p):
    qr=(-1,140,-294,140)
    one=(1,0,0,0);zero=(0,0,0,0);t=(0,1,0,0)
    def k(v):return (v%p,0,0,0)
    def add(a,b):return tuple((a[i]+b[i])%p for i in range(4))
    def mul(a,b):
        v=[0]*7
        for i in range(4):
            for j in range(4):v[i+j]+=a[i]*b[j]
        for j in range(6,3,-1):
            w=v[j]
            for i in range(4):v[j-4+i]+=w*qr[i]
        return tuple(x%p for x in v[:4])
    def neg(a):return tuple(-x%p for x in a)
    def sub(a,b):return add(a,neg(b))
    m=(p-1)//2;H=Hp=zero;mon=old=one;bi=1
    for j in range(m+1):
        w=bi*bi%p
        H=add(H,mul(k(w),mon))
        if j:Hp=add(Hp,mul(k(j*w),old))
        old=mon;mon=mul(mon,t)
        if j<m:bi=bi*(m-j)*pow(j+1,-1,p)%p
    C=add(mul(k(16),mul(mul(t,sub(one,mul(t,t))),Hp)),
          mul(sub(add(one,mul(k(2),t)),
                  mul(k(7),mul(t,t))),H))
    chi=pow((-2*pow(3,-1,p))%p,m,p)
    if p%24==5:
        assert chi==1 and C==zero and H!=zero,(p,'split')
        return 'split'
    assert p%24==13 and chi==p-1 and H==zero and C!=zero,(p,'inert')
    return 'inert'

if __name__=='__main__':
    assert symbolic()
    print('SYMBOLIC_PASS: Velu degree 3, CM kernel and 2/3 first-jet identities')
    counts={'split':0,'inert':0}
    for p in primes(5000):counts[finite(p)]+=1
    assert counts=={'split':85,'inert':83},counts
    print('FINITE_EXACT_PASS',counts,'total',sum(counts.values()),'limit',5000)
