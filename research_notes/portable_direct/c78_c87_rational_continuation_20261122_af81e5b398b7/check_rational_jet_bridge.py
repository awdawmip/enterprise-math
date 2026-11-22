"""Exact finite evidence for the new rational normalization and local jet bridge.

Usage: python check_rational_jet_bridge.py [previous_reproof_directory]
The default directory is the already-published sibling research bundle.
"""
from pathlib import Path
from fractions import Fraction as Q
from functools import cache
from math import comb, isqrt
import json
import sys

ROOT = Path(__file__).resolve().parent
PREVIOUS = (Path(sys.argv[1]) if len(sys.argv) > 1 else
            ROOT.parent / "c78_c87_rational_reproof_20261122_af81e5b398b7")
sys.path.insert(0, str(PREVIOUS))
import exact_inventory as original
from explicit_algebra import (circuit, evaluate, derivative, add, mul, scale,
                              shift, power, fractions_pack)

# Same exact finite products, extended once per k to avoid rebuilding prefixes.
prefixes = {k: [Q(1)] for k in (1, 3, 5)}
def prefix(k, n):
    row = prefixes[k]
    while len(row) <= n:
        j = len(row)
        row.append(row[-1] * Q(4*j+k, 4*(j+k)))
    return row[n]
original.prefix = prefix


def tail_correction(w):
    a = prefix(1,w)/prefix(1,2)
    t = Q(840,(w+2)*(w+3)*(w+4))
    return (1+(Q(7,3)-a)*t)/((1+Q(3,32)*a*t)*(1+6*a*t))


@cache
def gamma(c,n,v,w):
    return Q(5,27)*(original.readout(n,v,w)-1)/prefix(1,c)


def factorized_gamma(c,n,v,w):
    a, ss = original.block_coefficients(n,v,5)
    d, tt = original.block_coefficients(v,w,3)
    z1, _, z3 = original.terminal_scores(w)
    ends = [(d+tt*z)/(1+tt*z) for z in (z1,z3)]
    lo, hi = min(ends), max(ends)
    u, vv = (lo,hi) if a < 1 else (hi,lo)
    return (prefix(1,w)/prefix(1,c)*tail_correction(w)
            *tt*ss*abs(1-d)*abs(1-a)
            /((1+tt*z1)*(1+tt*z3)*(1+ss*vv)*(a+ss*u)))


def forward(f,v,w,a,b):
    return sum(((-1)**(a+b-i-j)*comb(a,i)*comb(b,j)*f(v+i,w+j)
                for i in range(a+1) for j in range(b+1)),Q(0))


def spatial_jet(n,q,r,s):
    qr, qs = derivative(q,0), derivative(q,1)
    a = add(mul(q,derivative(n,0)),scale(mul(n,qr),-1))
    b = add(mul(q,derivative(n,1)),scale(mul(n,qs),-1))
    hrr = add(shift(add(mul(q,derivative(a,0)),
                        scale(mul(a,qr),-2)),1),scale(mul(a,q),-3))
    hss = add(shift(add(mul(q,derivative(b,1)),
                        scale(mul(b,qs),-2)),0,1),scale(mul(b,q),-3))
    mixed = add(mul(q,derivative(a,1)),scale(mul(a,qs),-2))
    qq=evaluate(q,r,s)
    return {(0,0):evaluate(n,r,s)/qq,
            (1,0):evaluate(a,r,s)/(4*r**3*qq**2),
            (0,1):evaluate(b,r,s)/(4*s**3*qq**2),
            (2,0):evaluate(hrr,r,s)/(16*r**7*qq**3),
            (0,2):evaluate(hss,r,s)/(16*s**7*qq**3),
            (1,1):evaluate(mixed,r,s)/(16*r**3*s**3*qq**3)}


def outward(q, digits=9):
    """Rational outward endpoints, without a float acceptance step."""
    q=Q(q);unit=10**digits
    lower=q.numerator*unit//q.denominator
    upper=-((-q.numerator*unit)//q.denominator)
    return [str(Q(lower,unit)),str(Q(upper,unit))]


def main():
    assert prefix(1,2)==Q(15,32)
    tail_cases=0
    for w in range(4,65):
        z1,z2,z3=original.terminal_scores(w)
        assert z1<z2<z3
        assert z3-z1==Q(27,5)*prefix(1,w)*tail_correction(w)
        assert abs(tail_correction(w)-1)<=Q(9100,w**3)
        tail_cases+=1
    sign_cases=[]
    for n,v,w in [(128,64,8),(128,64,48),(128,100,10),(128,120,100)]:
        a,_=original.block_coefficients(n,v,5)
        d,_=original.block_coefficients(v,w,3)
        assert gamma(n,n,v,w)==factorized_gamma(n,n,v,w)
        sign_cases.append({'n':n,'V':v,'W':w,
                           'outer_sign':1 if a<1 else -1,
                           'inner_sign':1 if d<1 else -1})
    assert len({(t['outer_sign'],t['inner_sign']) for t in sign_cases})==4

    cc=circuit()
    r,s=Q(3,4),Q(1,2)
    rjet=spatial_jet(cc['N'],cc['Q'],r,s)
    # d_q G at q=1 equals -(E R)-3R/4 on this positive branch.
    nb=scale(add(cc['C'],scale(mul(cc['N'],cc['Q']),3)),-1)
    qb=scale(power(cc['Q'],2),4)
    zjet=spatial_jet(nb,qb,r,s)
    assert rjet[(0,0)]>0
    rows=[]
    for c in [256,512,1024,2048,4096,8192,16384]:
        v,w=81*c//256,c//16
        assert Q(v,c)==r**4 and Q(w,c)==s**4
        assert gamma(c,c,v,w)==factorized_gamma(c,c,v,w)
        for alpha,limit in rjet.items():
            observed=c**sum(alpha)*forward(lambda vv,ww:gamma(c,c,vv,ww),v,w,*alpha)
            assert limit
            rows.append({'c':c,'coordinate':'first','alpha':list(alpha),
                         'relative_absolute_error_interval':outward(abs((observed-limit)/limit))})
        for b in [1,isqrt(c)]:
            def f(vv,ww):
                return Q(c,b)*(gamma(c,c+b,vv,ww)-gamma(c,c,vv,ww))
            for alpha,limit in zjet.items():
                observed=c**sum(alpha)*forward(f,v,w,*alpha)
                assert limit
                rows.append({'c':c,'b':b,'coordinate':'near_stock_difference',
                             'alpha':list(alpha),
                             'relative_absolute_error_interval':outward(abs((observed-limit)/limit))})
    result={'source_bundle_commit':'46eec634a39fd202babd05e66b251d90945be948',
            'arithmetic':'fractions.Fraction, integers; output intervals are outward rational endpoints',
            'normalizer':'5/(27 F_1(c)); the reference c is held fixed across n',
            'tail_identity_and_order_cases':tail_cases,
            'four_sign_branches_exact_factorization':sign_cases,
            'limiting_point':{'r':str(r),'s':str(s),'x':str(r**4),'y':str(s**4)},
            'limiting_first_jet':{str(a):fractions_pack(v) for a,v in rjet.items()},
            'limiting_second_jet':{str(a):fractions_pack(v) for a,v in zjet.items()},
            'scaled_jet_comparisons':len(rows),'rows':rows,'status':'PASS',
            'scope':'Finite exact evidence for the written all-order local theorem; sampled errors do not establish uniform convergence by themselves.'}
    (ROOT/'rational_jet_bridge_checks.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','tail_cases':tail_cases,
        'sign_branches':len(sign_cases),'scaled_jet_comparisons':len(rows),
        'value_examples':[row for row in rows if row['alpha']==[0,0]]},indent=2))


if __name__=='__main__':
    main()
