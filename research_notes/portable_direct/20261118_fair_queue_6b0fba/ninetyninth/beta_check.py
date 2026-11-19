"""Two positive-integer completion probes for a path with two hidden vertices."""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path

# Coefficients of f=F_+/K^4 as monomials r^i X^j Y^k.
TERMS = {
    (0,0,0):64,
    (1,0,0):48,(0,1,0):-4,(0,0,1):28,
    (2,0,0):244,(1,1,0):-360,(1,0,1):-318,(0,2,0):252,(0,1,1):254,(0,0,2):270,
    (2,1,0):44,(2,0,1):34,(1,2,0):-76,(1,1,1):-120,(1,0,2):-50,
    (0,3,0):32,(0,2,1):122,(0,1,2):130,(0,0,3):16,
    (2,2,0):16,(2,1,1):2,(2,0,2):16,(1,3,0):-32,(1,2,1):-18,(1,1,2):-18,
    (1,0,3):-32,(0,4,0):16,(0,3,1):16,(0,2,2):36,(0,1,3):16,(0,0,4):16,
}


def evaluate(poly,r,x,y):
    return sum(n*r**i*x**j*y**k for (i,j,k),n in poly.items())


def derivative(poly,coordinate):
    out={}
    for exps,coef in poly.items():
        power=exps[coordinate]
        if power:
            idx=list(exps)
            idx[coordinate]-=1
            out[tuple(idx)]=coef*power
    return out


def linear(p,q,sign=1):
    return {e:p.get(e,0)+sign*q.get(e,0) for e in p.keys()|q.keys()
            if p.get(e,0)+sign*q.get(e,0)}


def minimum_scale(resistance):
    p,q=resistance.numerator,resistance.denominator
    return 1+(113*p+isqrt(12561*p*p))//(8*q)


def exact_ok(resistance,k):
    # R/K is below the smaller root. Rational positive inputs cannot attain it.
    t=Q(resistance,k)
    return t<Q(1,25) and 13*t*t-113*t+4>0


def load_previous(path):
    pin='ca5cbac238324f4851ace7fe25c762dd88c583d8ed1ee82b530c5c4721dba128'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==pin
    spec=importlib.util.spec_from_file_location('source_1162',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_checks(reference):
    def both(resistors,k):
        R=sum(resistors)
        t=R/k
        x,y=resistors[0]/k,resistors[2]/k
        result=[]
        for probe,z,w in [([k,2*k],x,y),([2*k,k],y,x)]:
            ring=resistors+probe
            beta=reference.resistance_beta(ring)
            assert beta==reference.value(ring)
            assert beta*(5*(t+3))**4/8==evaluate(TERMS,t,z,w)
            result.append(beta)
        return result

    def prepare(triple,k):
        return both(list(map(Q,triple)),Q(k))

    points=0
    # The integer simplex nodes (positive shifts) are unisolvent for total degree <=4.
    for i,j,k in product(range(5),repeat=3):
        if i+j+k<=4:
            prepare([1+i,1+j,1+k],1)
            points+=1
    assert points==35
    exam=[]
    for inputs in [(Q(1,7),Q(3,2),Q(10,3)),(Q(16),Q(9),Q(22))]:
        R=sum(inputs)
        k=minimum_scale(R)
        exam.append(dict(unknown=list(map(str,inputs)),R=str(R),minimum_K=k,
                         beta=list(map(str,prepare(inputs,k)))))
    bad1,bad2=[8,33,6],[6,33,8]
    left=prepare(bad1,3)
    assert left==prepare(bad2,3)
    new=prepare(bad1,minimum_scale(Q(47)))
    assert new[0]!=new[1] and new[::-1]==prepare(bad2,minimum_scale(Q(47)))
    return dict(unisolvent_positive_simplex_nodes=points,exact_positive_ring_reads=2*(points+2+4),
                examples=exam,collision=dict(K=3,R=47,unknowns=[bad1,bad2],both_readings=list(map(str,left))),
                repaired_47_at_K=minimum_scale(Q(47)),repaired_readings=list(map(str,new)))


def certificate():
    dx,dy=derivative(TERMS,1),derivative(TERMS,2)
    g,h=linear(dy,dx),linear(dy,dx,-1)
    def at_origin(P):
        return [P.get((i,0,0),0) for i in range(4)]
    assert at_origin(g)==[24,-678,78,0] and at_origin(h)==[32,42,-10,0]
    assert [g[0,1,0],g[0,0,1],h[0,1,0],h[0,0,1]]==[758,794,-250,286]
    second_bounds={}
    for total in (3,4):
        second_bounds[total]=sum(abs(c)*(j+k)*(j+k-1)
            for (i,j,k),c in TERMS.items() if i+j+k==total)
    assert list(second_bounds.values())==[2292,1868]
    correction=Q(2292,25)+Q(1868,25**2)
    assert correction<95
    for r in range(5):
        assert evaluate(g,Q(r),Q(r,2),Q(r,2))==(r+3)*(9*r*r+30*r+8)
    # A polynomial identity in three variables of total degree <=4.
    for i,j,k in product(range(5),repeat=3):
        if i+j+k>4:
            continue
        r,x,y=map(Q,(1+i,1+j,1+k))
        d=-16-21*r-9*(x+y)+5*r*r-13*r*(x+y)+8*x*x+4*x*y+8*y*y
        assert evaluate(TERMS,r,x,y)-evaluate(TERMS,r,y,x)==2*(x-y)*d
    scales=0
    for p,q in product(range(1,121),range(1,38)):
        R=Q(p,q)
        k=minimum_scale(R)
        assert exact_ok(R,k)
        assert k==1 or not exact_ok(R,k-1)
        scales+=1
    return dict(source_quartic_terms=len(TERMS),g_at_origin=list(at_origin(g)),h_at_origin=list(at_origin(h)),
                component_linear_coefficients=[758,794,-250,286],higher_coefficient_norms=second_bounds,
                Hessian_remainder_bound_at_1_over_25=str(correction),rational_scale_tests=scales)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prior-check',type=Path,
                   default=Path(__file__).resolve().parents[1]/'fiftyfirst/terminals_check.py')
    p.add_argument('--out',type=Path)
    args=p.parse_args()
    report=dict(algebra=certificate(),replays=source_checks(load_previous(args.prior_check)))
    encoded=json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    if args.out:
        args.out.write_text(encoded)
    else:
        print(encoded,end='')
