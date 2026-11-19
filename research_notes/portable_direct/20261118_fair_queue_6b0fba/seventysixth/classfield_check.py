"""Certified small-discriminant level-two marked CM comparison, python-flint."""
import argparse
import json
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path

import flint
from flint import acb, arb, ctx, fmpz_poly, fmpz_mod_poly_ctx


def forms(D):
    for a in range(1, isqrt(abs(D)//3)+1):
        for b in range(-a,a+1):
            disc=b*b-D
            if disc%(4*a):
                continue
            c=disc//(4*a)
            if a>c or ((abs(b)==a or a==c) and b<0):
                continue
            if gcd(gcd(a,b),c)==1:
                yield a,b,c


def theta_data(tau):
    theta=acb(0).modular_theta(tau)
    x=tau.modular_lambda()
    assert x.overlaps((theta[1]/theta[2])**4)
    q2=(2*arb.pi()*acb(0,1)*tau).exp()
    h=80
    total=sum(n*q2**n/(1-q2**n) for n in range(1,h+1))
    radius=abs(q2).upper()
    tail=24*radius**(h+1)*(h+1)/(1-radius)**3
    error=arb(0,tail.upper())
    E=1-24*total+acb(error,error)-3/(arb.pi()*tau.imag)
    return x,E/theta[2]**4


def markings(x,e):
    for word in ['', 'S','T','ST','TS','STS']:
        a,b=x,e
        for h in word:
            if h=='S': a,b=1-a,-b
            else: a,b=a/(a-1),b/(1-a)
        yield word,a,b


def ratios(x,e):
    return ((e**2+(4*x-2)*e+7*x*x-7*x+1)/(3*(1-x)**2), (1-3*x-e)/(1-x))


def finite_places():
    X=fmpz_poly([0,1])
    num=256*(1-X+X**2)**3
    den=X**2*(1-X)**2
    H=fmpz_poly.hilbert_class_poly(-20)
    assert list(H)==[-681472000,-1264000,1]
    relation=num**2+H[1]*num*den+H[0]*den**2
    point=acb(0,arb(5).sqrt()).modular_lambda()
    factors=[factor for factor,power in relation.factor()[1]]
    def ball_eval(poly):
        val=acb(0)
        for c in reversed(poly.coeffs()):
            val=val*point+int(c)
        return val
    candidates=[factor for factor in factors if 0 in ball_eval(factor)]
    assert len(candidates)==1
    poly=candidates[0]
    assert list(poly)==[1,-72,88,-32,16]
    modular={}
    for p,expect in [(11,[1,1,2]),(13,[2,2])]:
        assert pow(-5,(p-1)//2,p)==p-1
        _,parts=fmpz_mod_poly_ctx(p)(poly).factor()
        assert all(k==1 for g,k in parts)
        degrees=sorted(g.degree() for g,k in parts)
        assert degrees==expect
        modular[str(p)]={"degrees":degrees,"monic_factors":[[int(c) for c in g.coeffs()] for g,k in parts]}
    return {"H_minus_20":[int(a) for a in H],"lambda_i_sqrt5":[int(a) for a in poly],
            "all_quartic_factors":[[int(a) for a in f] for f in factors],
            "primitive_reduced_minus80":list(forms(-80)),"inert_primes":modular}


def certificate():
    ctx.prec=192
    records=[]
    by_D={}
    for D in range(-40,-2):
        if D%4 not in (0,1): continue
        red=list(forms(D))
        if not red: continue
        first=len(records)
        for a,b,c in red:
            tau=acb(-arb(b)/(2*a),arb(-D).sqrt()/(2*a))
            x,e=theta_data(tau)
            marks=list(markings(x,e))
            if D in (-3,-4):
                # The stabilizer has order 3 or 2 in PSL. Every marking has E2*=0.
                assert 0 in e
                wanted=2 if D==-3 else 3
                unique=[]
                for w,z,v in marks:
                    if all(not z.overlaps(prev[1]) for prev in unique): unique.append((w,z,v))
                assert len(unique)==wanted
                marks=unique
            for w,z,v in marks:
                alpha,beta=ratios(z,v)
                records.append((D,a,b,c,w,z,v,alpha,beta))
        n=len(records)-first
        by_D[str(D)]={'reduced_forms':red,'marked_coordinates':n,'unordered_internal_pairs':n*(n-1)//2}
    # Both coordinates compared as rectangular complex intervals with rigorous radii.
    pairs=0; b_separates=0; alpha_separates=0; min_distance=None; witness=None
    for i,j in combinations(records,2):
        assert not i[5].overlaps(j[5])
        aa=i[7]-j[7];bb=i[8]-j[8]
        d=max(abs(aa).lower(),abs(bb).lower())
        assert d>0,(i[:5],j[:5])
        if min_distance is None or d<min_distance:
            min_distance=d; witness=[i[:5],j[:5]]
        b_separates+=int(not i[8].overlaps(j[8]));alpha_separates+=int(not i[7].overlaps(j[7]));pairs+=1
    return dict(finite_places=finite_places(),python_flint=flint.__version__,precision_bits=ctx.prec,q_lambert_terms=80,orders=by_D,
                marked_coordinates=len(records),all_pairs_separated=pairs,beta_alone_separates=b_separates,
                alpha_alone_separates=alpha_separates,min_sup_distance_greater_than_1_over=int((1/min_distance).ceil().unique_fmpz()),
                nearest_pair=witness)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path)
    out=parser.parse_args().out
    text=json.dumps(certificate(),indent=2,sort_keys=True)+'\n'
    if out:out.write_text(text)
    else:print(text,end='')
