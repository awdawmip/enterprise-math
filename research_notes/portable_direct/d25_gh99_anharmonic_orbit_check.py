#!/usr/bin/env python3
"""GH-99 weighted S3 orbit projection for the GH-98 finite-log trace."""
from collections import Counter
from d25_gh98_finite_log_trace_check import (reflected_h, direct_tail,
    finite_log_fermat, poly_h_value)

def transforms(t,p):
    assert t not in (0,1)
    ir = pow(t,-1,p)
    i1 = pow(1-t,-1,p)
    im1 = pow(t-1,-1,p)
    return ((t,1), ((1-t)%p,1), (ir,(-ir)%p),
        ((1-ir)%p,(-ir)%p), (i1,(-i1)%p),
        ((t*im1)%p,im1))

def orbit_trace(h,p,a):
    d=len(h)-1
    visited=set()
    total=0
    orbit_sizes=Counter()
    active=0
    nonzero_terms=0
    certificates=[]
    for t in range(2,p):
        if t in visited:
            continue
        orb={}
        ell=finite_log_fermat(t,p)
        for x,w in transforms(t,p):
            assert (finite_log_fermat(x,p)-w*ell)%p==0,(p,t,x,w)
            if x in orb:
                assert (orb[x]-w)*ell%p==0
            else:
                orb[x]=w
        visited.update(orb)
        orbit_sizes[len(orb)]+=1
        if ell:
            active+=1
        weighted=0
        for x,w in orb.items():
            z=a*x%p
            weighted=(weighted+w*pow(z,d,p)*poly_h_value(h,z,p))%p
        contribution=a*ell*weighted%p
        nonzero_terms+=bool(contribution)
        total=(total+contribution)%p
        certificates.append((t,len(orb),ell,weighted,contribution))
    assert visited==set(range(2,p))
    return total,orbit_sizes,active,nonzero_terms,certificates

def main():
    pairs=[(p,a) for p in (7,11,19,23,31,43,47,59,67,71,83)
           for a in range(1,p)]
    pairs += [(103,9),(167,9),(3347,9)]
    for p,a in pairs:
        h=reflected_h(p)
        value,counts,active,nonzero,cert=orbit_trace(h,p,a)
        assert value==direct_tail(h,p,a),(p,a,value,direct_tail(h,p,a))
        if a==9:
            print('p',p,'orbit_sizes',dict(sorted(counts.items())),
                  'active_log_orbits',active,'nonzero_contributions',nonzero,
                  'R(9)',value)
            if p==3347:
                print('p3347_first_five_orbit_contributions',cert[:5])
    print('PASS_GH99_S3_ORBIT_SOURCE_PROJECTION;',len(pairs),'parameter_specializations')

if __name__=='__main__':
    main()
