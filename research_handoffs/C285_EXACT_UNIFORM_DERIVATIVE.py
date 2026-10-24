#!/usr/bin/env python3
"""C285 exact uniform derivative theorem for the 187 C284 dyadic brackets.

Inputs beside this file: immutable C275_STANDALONE_EXACT_REPLAY.py and
C284_187_EXACT_DYADIC_BRACKETS.json. Only stdlib Fraction is used to decide
all inequalities; no float participates in the proof. No Source admission.
"""
from fractions import Fraction as R
import hashlib, json
import C275_STANDALONE_EXACT_REPLAY as s


def bounds(coef, x, y):
    assert x*y > 0                 # denominator cannot vanish on interval
    a,b=coef/x,coef/y
    return min(a,b),max(a,b)


def slope_range(j, v0, v1, d):
    """Bounds for (d/dt)log(M_j(v(t))) on the closed parameter interval."""
    lo=hi=R(0)
    def add(coef,x,y):
        nonlocal lo,hi
        if coef:
            a,b=bounds(coef,x,y)
            lo+=a; hi+=b
    if j in s.J:
        for k in range(4):
            add(-d[k],s.Z-v0[k],s.Z-v1[k])
            add(d[k],s.U[j]-v0[k],s.U[j]-v1[k])
    else:
        i=s.I.index(j)
        def kernel(p):
            return 6*d[i]*p*(1/(2-p*p)+1/(3-p*p))
        # p > 0; p/(a-p^2) is increasing for a=2,3, so endpoints bound kernel
        a,b=kernel(v0[i]),kernel(v1[i])
        lo+=min(a,b);hi+=max(a,b)
        for u in s.J:
            add(-d[i],v0[i]-s.U[u],v1[i]-s.U[u])
        for k in range(4):
            if i!=k:
                add(-d[k],s.Z-v0[k],s.Z-v1[k])
                add(d[k]-d[i],v0[i]-v0[k],v1[i]-v1[k])
    return lo,hi


def branch_mass(j, mid, weights):
    return (R(weights[j])*s.fixed_multiplier(j,mid) if j in s.J
            else s.moving_mass(j,mid))


def derivative_lower(w, h, a, b, weights):
    d=tuple(y-x for x,y in zip(w,h))
    v0=tuple(x+a*z for x,z in zip(w,d))
    v1=tuple(x+b*z for x,z in zip(w,d))
    vm=tuple((x+y)/2 for x,y in zip(v0,v1))
    assert s.valid(v0) and s.valid(v1) and s.valid(vm)
    half=(b-a)/2
    total=R(0)
    for j in range(79):
        ll,uu=slope_range(j,v0,v1,d)
        rho=max(abs(ll),abs(uu))*half
        assert rho<1
        mass=branch_mass(j,vm,weights)
        # log M has derivative in [-B,B]; exp(rho)<=1/(1-rho)
        # and exp(-rho)>=1-rho, hence exact rational lower envelope.
        total+= mass*ll*(1-rho) if ll>=0 else mass*ll/(1-rho)
    return total


def check():
    report=json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json',encoding='utf-8'))
    records=report['records']
    raw=json.dumps(records,ensure_ascii=False,separators=(',',':')).encode()
    assert hashlib.sha256(raw).hexdigest()==report['certificate_sha256']
    assert report['certificate_sha256']=='fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576'
    assert len(records)==187 and len({(r[0],r[1]) for r in records})==187
    weights,_=s.floor_fixed_masses(); hulls=s.hulls()
    expected={(i,j) for (i,j),(lo,hi,kind) in hulls.items()
              if kind!='safe' and any(s.inside(w,lo,hi) for w in s.WITNESSES)}
    assert len(expected)==187
    for i,j,wid,k in records:
        assert (i,j) in expected and wid in (1,2) and 0<=k<4096
        lo,hi,_=hulls[(i,j)];w=s.WITNESSES[wid-1];h=s.high_point(lo,hi)
        assert s.inside(w,lo,hi) and s.inside(h,lo,hi)
        a,b=R(k,4096),R(k+1,4096)
        v0=tuple(x+a*(y-x) for x,y in zip(w,h))
        v1=tuple(x+b*(y-x) for x,y in zip(w,h))
        assert s.original_F(v0,weights)<s.Q<s.original_F(v1,weights)
        # Main new theorem: along every one of the 187 *whole* dyadic brackets.
        assert 56*derivative_lower(w,h,a,b,weights)>s.Q,(i,j,k)
    assert {(r[0],r[1]) for r in records}==expected
    print('C285_187_UNIQUE_SIMPLE_ROOTS_EXACT_PASS Q_over_56_derivative_bound')

if __name__=='__main__':check()
