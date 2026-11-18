"""Exact output-fibre heat-Gram checks for the positive-helicity lattice family."""
from argparse import ArgumentParser
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
from runpy import run_path
import json
import sympy as s

K=(1,0,0)
SEED='ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59'


def neg(k):
    return tuple(-v for v in k)


def norm2(k):
    return sum(v*v for v in k)


def envelope(n):
    """Floating-point-free enclosure with denominator 10**6."""
    k=n*10**6
    return [str(F(k.numerator//k.denominator,10**6)),
            str(F(-(-k.numerator//k.denominator),10**6))]


def structure(L):
    pairs=[((L,j,0),(1-L,-j,0)) for j in range(L//2,L+1)]
    support={v for p,q in pairs for v in (p,q,neg(p),neg(q))}
    found={(p,q) for p,q in product(support,repeat=2) if tuple(a+b for a,b in zip(p,q))==K}
    assert found==set(pairs)|{(q,p) for p,q in pairs}
    rates=tuple(norm2(p)+norm2(q) for p,q in pairs)
    S=2*L*L
    assert len(set(rates))==len(pairs) and all(S<=a<2*S for a in rates)
    # In the minus-helicity readout every vector equals t, ||t||^2=1/2.
    J=sum((F(1,2*(a+b)) for a,b in product(rates,repeat=2)),F())
    D=sum((F(1,4*a) for a in rates),F())
    r=J/D
    assert F(len(pairs),2)<=r<=len(pairs)
    return pairs,dict(L=L,parents=len(support),unordered=len(pairs),two_ordered=len(found),
                      rates=[rates[0],rates[-1]],ratio_interval=envelope(r),
                      ratio_exact=str(r) if L<=16 else None)


def symbolic_packet(p,q,helical):
    """Independent actual signed/ordered convolution at e1, including helicity and reality."""
    P,Q=s.Matrix(p),s.Matrix(q);rp=s.sqrt(norm2(p));rq=s.sqrt(norm2(q))
    j=p[1]
    z=1/(rp+rq)
    x=(p[0]*rq+(-q[0])*rp)/(j*(rp+rq))
    # The pinned helper emits the real/conjugate convention
    # with its own factor of 1/2. Phase argument 2 gives vertical component 1.
    modes=helical([p,q],[s.Integer(2),s.Integer(2)])
    a,b=modes[p],modes[q]
    assert all(s.simplify(t)==0 for t in [P.dot(a),Q.dot(b)])
    alpha=1/((rp-rq)*j*(1/rp+1/rq)*(1-z))
    ap=alpha*a
    # Original C=-v cross Lambda v, sum both ordered terms separately.
    raw=-ap.cross(rq*b)-b.cross(rp*ap)
    expected=s.Matrix([-s.I*x,-s.I,z])/(1-z)
    assert all(s.simplify(v)==0 for v in raw-expected)
    e=s.Matrix(K);projected=raw-e*e.dot(raw)
    minus=(projected-s.I*e.cross(projected))/2
    target=s.Matrix([0,-s.I/2,-s.Rational(1,2)])
    assert all(s.simplify(v)==0 for v in minus-target)
    assert all(s.simplify(v)==0 for v in
               modes[neg(p)]-s.conjugate(a))
    # The attached receiver at +k, -k is divergence-free, negative-helical.
    assert (s.I*e.cross(target)+target)==s.zeros(3,1) and e.dot(target)==0


def verify_finite_gram():
    checks=0
    for rates in ((1,2),(2,3,7),(3,8,11,19),(2,5,12,20,33)):
        G=s.Matrix([[s.Rational(1,a+b) for b in rates] for a in rates])
        e=s.ones(len(rates),1);v=G.inv()*e
        assert G.is_positive_definite
        assert (e.T*v)[0]==2*sum(rates)
        H=2*sum(rates)*G-e*e.T
        assert H.is_positive_semidefinite and H*v==s.zeros(len(rates),1)
        # Signed source derivative against a complex packet family.
        b=s.Matrix([i+s.I*(-1)**i for i in rates])
        v=s.Matrix([i%5-s.I*i for i in rates]);t=s.Symbol('t',real=True)
        g=(b+t*v).conjugate().T*G*(b+t*v)
        assert s.simplify(s.diff(g[0],t).subs(t,0)-2*s.re((b.conjugate().T*G*v)[0]))==0
        L=s.diag(*rates)
        assert L*G+G*L==e*e.T
        checks+=1
    return checks


def main():
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    f=args.repo/'research_notes/ns-causal-inverse-newton-basin-20260909/inherited_fourier.py'
    assert sha256(f.read_bytes()).hexdigest()==SEED
    helical=run_path(str(f))['helical_data']
    rows=[];tested=0
    for L in (8,16,32,64,128):
        pairs,row=structure(L);rows.append(row)
        for pair in pairs if L==8 else (pairs[0],pairs[-1]) if L==16 else ():
            symbolic_packet(*pair,helical);tested+=1
    result=dict(pinned_fourier_sha256=SEED,physical_exact_helical_pair_checks=tested,
                finite_gram_trials=verify_finite_gram(),families=rows)
    print(json.dumps(result,ensure_ascii=True,indent=2))
    if args.json:args.json.write_text(json.dumps(result,ensure_ascii=True,indent=2)+'\n')


if __name__=='__main__':main()
