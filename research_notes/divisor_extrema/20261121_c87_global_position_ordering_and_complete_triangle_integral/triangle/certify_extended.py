#!/usr/bin/env python3
"""C85 certified triangle constant using the exact A<2 formula.

Reuses C84's pinned integer outward arithmetic and monotone density enclosure.
No floating quadrature or random sampling is used in the bound.
"""
from fractions import Fraction
from pathlib import Path
from math import comb
import json,time,hashlib,argparse
import c84_interval_kernel as k

I,Q,ZETA,C1=k.I,k.Q,k.ZETA,k.C1

def centered_triangle(a):
    av=I.cv(a)
    return av*av/(36*ZETA)*k.density(Fraction(3,2)/a)

def area_cell(l,h):
    if h>2:
        return k.area_cell(l,h)
    lv,hv=I.cv(l),I.cv(h)
    _,_,bl,cl=k.moments(l)
    _,_,bh,ch=k.moments(h)
    tl,th=centered_triangle(l),centered_triangle(h)
    low=(lv-C1*hv*hv+bl-ch-th).lo
    high=(hv-C1*lv*lv+bh-cl-tl).hi
    low=max(0,low)
    high=min(high,hv.hi,Q)
    if l>=1:
        low=max(low,(3/(16*ZETA*hv*hv)).lo)
        high=min(high,(lv/(lv*lv-lv+1)).hi)
    assert low<=high
    return I(low,high)*4*(hv.sqrt()-lv.sqrt())

def tail_series(terms=256,R=3):
    """Positive rational series and ratio <=8/R^2 after n>=9."""
    assert terms>=9 and R>=3
    def moment(n):
        return Fraction(4,(n+1)*(n+2)*(n+3))*sum(
            (Fraction(2**(j+1)-1,(j+2)*(n+2-j)) for j in range(n+2)),Fraction(0))
    def term(n):
        return Fraction(comb(2*n+5,n),(2*n+5)*R**(2*n+5))*moment(n)
    total=sum((term(n) for n in range(terms)),Fraction(0))
    rem=term(terms)/(1-Fraction(8,R*R))
    lo=I.cv(total).lo;hi=I.cv(total+rem).hi
    root=I.rat(2).sqrt()
    return root/(2*ZETA*R**3)+6*root/ZETA*I(lo,hi)

def certify(mesh=1024):
    assert mesh%2==0
    start=time.time()
    half=I.rat(1,2)
    head=4*half*half.sqrt()/3-4*C1*half*half*half.sqrt()/5
    early=I.rat(0); middle=I.rat(0)
    for j in range(mesh//2,9*mesh//2):
        val=area_cell(Fraction(j,mesh),Fraction(j+1,mesh))
        if j<2*mesh: early+=val
        else: middle+=val
    tail=tail_series()
    total=head+early+middle+tail
    return {"schema":"C85_TRIANGLE_CONSTANT_CERTIFICATE_V1",
            "arithmetic":"integer outward intervals with denominator 2^112",
            "exact_formula_domain":"0<A<2", "area_mesh_per_unit":mesh,
            "head":head.json(),"exact_middle":early.json(),
            "bounded_middle":middle.json(),"tail":tail.json(),"kappa3":total.json(),
            "tail_series_terms":256,"seconds":time.time()-start,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "interval_kernel_sha256":hashlib.sha256(Path(k.__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mesh',type=int,default=1024)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('extended_certificate.json'))
    args=ap.parse_args();result=certify(args.mesh)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
