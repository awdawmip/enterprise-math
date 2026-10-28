#!/usr/bin/env python3
"""GH-60 exact finite-field exhaustive verification: all F_{p^2}-points killed by p-1."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
prior=Path(__file__).with_name('20261028_hourly_d25_gh58_gh59_signed_cm_isogeny_check.py')
spec=spec_from_file_location('gh58_existing_verified',prior)
f=module_from_spec(spec);spec.loader.exec_module(f)

def ec_add(P,Q,C,p):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u and f.add(y,v,p)==(0,0): return None
    if x==u:
        lam=f.div(f.add(f.sub(f.scale(f.mul(x,x,p),3,p),f.scale(x,12,p),p),C,p),f.scale(y,2,p),p)
    else: lam=f.div(f.sub(v,y,p),f.sub(u,x,p),p)
    xr=f.add(f.sub(f.sub(f.mul(lam,lam,p),x,p),u,p),f.const(6,p),p)
    return (xr,f.sub(f.mul(lam,f.sub(x,xr,p),p),y,p))

def ec_mult(n,P,C,p):
    R=None
    while n:
        if n&1: R=ec_add(R,P,C,p)
        P=ec_add(P,P,C,p)
        n>>=1
    return R

def certify(p):
    C=f.Ct(p)
    roots={}
    for a in range(p):
        for b in range(p):
            z=(a,b)
            roots.setdefault(f.mul(z,z,p),z)
    number=1
    for a in range(p):
        for b in range(p):
            xx=(a,b)
            z=f.f(xx,C,p)
            yy=roots.get(z)
            if yy is None:continue
            pts=[(xx,yy)] if yy==(0,0) else [(xx,yy),(xx,f.neg(yy,p))]
            for pt in pts:
                assert ec_mult(p-1,pt,C,p) is None,(p,pt)
            number+=len(pts)
    assert number==(p-1)**2,(p,number)
    return number

if __name__=='__main__':
    ps=[19,43,67,139,163]
    for p in ps:print('CERTIFIED_FULL_RATIONAL_TORSION',p,certify(p))
    print('PASS_GH60_ALL_INERT_PRIMES_UNDER_200',len(ps))
