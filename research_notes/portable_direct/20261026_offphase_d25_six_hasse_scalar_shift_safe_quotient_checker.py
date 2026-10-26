#!/usr/bin/env python3
"""Author-side exact finite-ring falsifier for six-to-three Hasse jet shift quotient.
No external libraries, no CM/native experiment, no proof or Source admission claim.
"""
from __future__ import annotations
import json
from math import isqrt
from pathlib import Path

LABELS = ((0, 2), (1, 2), (0, 3), (2, 2), (1, 3), (0, 4))


def prime(p):
    if p < 2: return False
    for d in range(2, isqrt(p) + 1):
        if p % d == 0: return False
    return True


def mul(a, b, mod, degree=4):
    out = [0] * (degree + 1)
    for i, x in enumerate(a[:degree+1]):
        for j, y in enumerate(b[:degree+1-i]):
            out[i+j] = (out[i+j] + x*y) % mod
    return out


def coeff_ratio(j, p, mod, degree=4):
    # F_(j+1)/F_j = ((j-m-t)(j-2m-2t))/((j+1)(j+1-p/2-3t))
    m = (p - 1) // 6
    a, b = j-m, j-2*m
    c = (j + 1 - p*pow(2, -1, mod)) % mod
    assert (j+1) % p and c % p
    t = (3 * pow(c, -1, mod)) % mod
    factor = pow(j+1, -1, mod) * pow(c, -1, mod) % mod
    numer = [a*b, -(2*a+b), 2]
    geom = [pow(t, i, mod) for i in range(degree+1)]
    return [(x * factor) % mod for x in mul(numer, geom, mod, degree)]


def inverse_series(f, mod, degree=2):
    inv0 = pow(f[0], -1, mod)
    out = [inv0]
    for k in range(1,degree+1):
        out.append(-inv0 * sum(f[i]*out[k-i] for i in range(1,k+1)) % mod)
    return out


def projection(c, mod):
    return [c[0] % mod, (c[1]+c[2]) % mod, (c[3]+c[4]+c[5]) % mod]


def low_shift(c, f, mod):
    a,b,d,e,g,h = c
    f0,f1,f2=f[:3]
    return [(f0*a)%mod,(f0*b+f1*a)%mod,(f0*d)%mod,
            (f0*e+f1*b+f2*a)%mod,(f0*g+f1*d)%mod,(f0*h)%mod]


def high_shift(c, f, mod):
    a,b,d,e,g,h = c
    f0,f1,f2=f[:3]
    return [(f0*a)%mod,(f0*b)%mod,(f0*d+f1*a)%mod,
            (f0*e)%mod,(f0*g+f1*b)%mod,(f0*h+f1*d+f2*a)%mod]


def small_shift(z, f, mod):
    return mul(z, f[:3], mod, 2)


def run(p, r=3):
    assert prime(p) and p % 6 == 1 and p >= 13
    m = (p-1)//6
    mod = p**r
    jet = [[1,0,0,0,0]]
    ratios=[]
    for j in range(p-1):
        rr=coeff_ratio(j,p,mod)
        ratios.append(rr)
        jet.append(mul(jet[-1],rr,mod))
    # Original high-source F_(p-l) divisible by t^2 exactly, not just mod p.
    L=min(7,2*m)
    for ell in range(1,L+1):
        assert jet[p-ell][0:2] == [0,0]
    q={ell:inverse_series(ratios[p-ell-1],mod,2) for ell in range(1,L)}
    data={}
    for j in range(1,L+1):
        for ell in range(1,L+1):
            u,v=jet[j],jet[p-ell]
            c=tuple(u[a]*v[b] % mod for a,b in LABELS)
            z=projection(c,mod)
            direct=[sum(u[i]*v[k+2-i] for i in range(k+1))%mod for k in range(3)]
            assert z==direct
            data[(j,ell)]=c
    nlow=nhigh=nflat=0
    for j in range(1,L+1):
        for ell in range(1,L+1):
            c=data[(j,ell)]
            if j<L:
                b=low_shift(c,ratios[j],mod)
                assert tuple(b)==data[(j+1,ell)]
                assert projection(b,mod)==small_shift(projection(c,mod),ratios[j],mod)
                nlow+=1
            if ell<L:
                b=high_shift(c,q[ell],mod)
                assert tuple(b)==data[(j,ell+1)]
                assert projection(b,mod)==small_shift(projection(c,mod),q[ell],mod)
                nhigh+=1
            if j<L and ell<L:
                left=high_shift(low_shift(c,ratios[j],mod),q[ell],mod)
                right=low_shift(high_shift(c,q[ell],mod),ratios[j],mod)
                assert left==right==list(data[(j+1,ell+1)])
                nflat+=1
    # Explicit abstract free-source kernel witnesses, stable in both directions.
    vectors=((0,1,-1,0,0,0),(0,0,0,1,-1,0),(0,0,0,1,0,-1))
    nkernel=0
    for vec in vectors:
        assert projection(vec,mod)==[0,0,0]
        for j in range(1,L):
            assert projection(low_shift(vec,ratios[j],mod),mod)==[0,0,0]
            nkernel+=1
        for ell in range(1,L):
            assert projection(high_shift(vec,q[ell],mod),mod)==[0,0,0]
            nkernel+=1
    turns=[]
    for j in (m,2*m):
        rr=ratios[j]
        assert rr[0] == 0 and rr[1]%p!=0
        # T(rr) loses the highest scalar jet component, but retains rank two.
        assert small_shift([0,0,1],rr,mod)==[0,0,0]
        assert small_shift([1,0,0],rr,mod)[1]%p!=0
        assert small_shift([0,1,0],rr,mod)[2]%p!=0
        turns.append({'j':j,'r0':rr[0], 'r1_mod_p':rr[1]%p, 'r2_mod_p':rr[2]%p})
    return {'p':p,'precision_power':r,'window_L':L,'cells_checked':len(data),
            'low_edge_checks':nlow,'high_edge_checks':nhigh,'flat_square_checks':nflat,
            'kernel_stability_checks':nkernel,'turning_ranks':turns,'status':'PASS'}


if __name__=='__main__':
    ps=(13,19,31,37,223,733,8221)
    records=[run(p) for p in ps]
    totals={k:sum(z[k] for z in records) for k in ('cells_checked','low_edge_checks','high_edge_checks','flat_square_checks','kernel_stability_checks')}
    result={'schema':'D25_SIX_HASSE_SCALAR_SHIFT_SAFE_QUOTIENT_AUTHOR_CHECK_V1',
            'status':'AUTHOR_SIDE_EXACT_PASS','primes':list(ps),'records':records,'totals':totals,
            'mathematical_scope':'All-prime algebraic identity, p-local scalar rank shifts, declared original six Hasse labels',
            'not_native_cm_dp_or_source_checkpoint':True}
    target=Path(__file__).with_name('d25_six_hasse_shift_quotient_author_check_20261026.json')
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'totals':totals,'primes':list(ps)},ensure_ascii=False))
