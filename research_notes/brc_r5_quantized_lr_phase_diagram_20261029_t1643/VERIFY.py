#!/usr/bin/env python3
"""Exact rational certificate for the finite-resolution LR collision phase diagram.

External two-law, two-decision-time stopping model; all-real optimality follows
from the accompanying Bellman proof. Finite checks enumerate deterministic
policies, including exact bin-boundary points, and never substitute for proof.
"""
from fractions import Fraction as F
from itertools import product

ACTIONS = ('P', 'Q', 'C')
TERMINALS = ('P', 'Q')
PLUS = (F(9, 10), F(3, 5))
W = (F(1), F(1), F(1, 8), F(1, 8))


def quantize(r, delta):
    x = (r-F(1))/delta + F(1, 2)
    return x.numerator // x.denominator


def ratios(eta):
    p = (F(1, 2)+eta, F(1, 2)-eta)
    q = (F(1, 2), F(1, 2))
    first = (p[0]/q[0], p[1]/q[1])
    second = tuple(first[i]*(2*(PLUS[i] if y else 1-PLUS[i]))
                   for i in range(2) for y in (True, False))
    return first, second


def observer(eta, acts, terminal):
    p = (F(1, 2)+eta, F(1, 2)-eta)
    q = (F(1, 2), F(1, 2))
    ep=eq=F(0)
    tp=tq=F(1)
    for i in range(2):
        if acts[i]=='P':
            eq+=q[i]
        elif acts[i]=='Q':
            ep+=p[i]
        else:
            tp+=p[i]
            tq+=q[i]
            for j, y in enumerate((True,False)):
                d = terminal[2*i+j]
                if d=='Q':
                    ep+=p[i]*(PLUS[i] if y else 1-PLUS[i])
                elif d=='P':
                    eq+=q[i]*F(1, 2)
                else:
                    raise AssertionError(d)
    return ep,eq,tp,tq


def value(o):
    return sum(x*y for x,y in zip(W,o))


def extrema(eta,delta):
    first,last=ratios(eta)
    fbin=tuple(quantize(x,delta) for x in first)
    lbin=tuple(quantize(x,delta) for x in last)
    assert len(set(lbin))==4  # terminal labels not lost to binning
    full_min=bin_min=None
    full_obs=set()
    bin_obs=set()
    full_count=bin_count=0
    for acts in product(ACTIONS,repeat=2):
        compatible=(fbin[0]!=fbin[1] or acts[0]==acts[1])
        for d in product(TERMINALS,repeat=4):
            o=observer(eta,acts,d)
            s=value(o)
            full_min=s if full_min is None else min(full_min,s)
            full_obs.add(o)
            full_count+=1
            if compatible:
                bin_min=s if bin_min is None else min(bin_min,s)
                bin_obs.add(o)
                bin_count+=1
    assert full_count==144
    assert bin_count==(48 if abs(eta)<delta/4 else 144)
    if abs(eta)>=delta/4:
        assert full_obs==bin_obs
    return full_min,bin_min,bin_count


def analytic(eta,delta):
    full=F(47,40)+(F(-31,40)*eta if eta>=0 else F(9,40)*eta)
    if abs(eta)>=delta/4:
        return full,full
    compressed=F(5,4)-(F(3,10)*eta if eta>=0 else F(0))
    return full,compressed


def test():
    n=0
    ds=(F(1,100),F(1,50),F(1,20),F(1,10))
    for d in ds:
        points={F(i,1000) for i in range(-49,50)}
        points|={-d/4,-d/8,F(0),d/8,d/4,-3*d/8,3*d/8}
        for eta in sorted(points):
            assert abs(eta)<F(1,20)
            full,binval,count=extrema(eta,d)
            expected_full,expected_bin=analytic(eta,d)
            assert (full,binval)==(expected_full,expected_bin), (d,eta,full,binval,expected_full,expected_bin)
            if abs(eta)<d/4:
                gap=binval-full
                signed=F(3,40)+(F(19,40)*eta if eta>=0 else -F(9,40)*eta)
                assert gap==signed>0
            else:
                assert binval==full
            n+=1
    d=F(1,10)
    for eta,expected_gap in [(F(0),F(3,40)),(F(1,100),F(319,4000)),
                             (-F(1,100),F(309,4000)),(F(1,40),F(0)),(-F(1,40),F(0))]:
        f,b,c=extrema(eta,d)
        assert b-f==expected_gap
        print(f'delta={d} eta={eta} min_FULL={f} min_bin={b} gap={b-f} bin_deterministic={c}')
    # Strict point-separating certificate for one actual FULL behavioral witness.
    eta=F(1,100)
    witness=observer(eta,('C','Q'),('P','Q','P','Q'))
    assert witness==(F(541,1000),F(1,4),F(151,100),F(3,2))
    assert value(witness)==F(4669,4000)
    assert F(5,4)-F(3,10)*eta==F(1247,1000)
    assert F(1247,1000)-value(witness)==F(319,4000)
    assert (F(319,4000)/sum(abs(w) for w in W))==F(319,9000)
    print('example_FULL_witness=(541/1000,1/4,151/100,3/2)')
    print('example_all_real_bin_plane: 8000(eP+eQ)+1000(TP+TQ)>=9976; FULL_witness=9338')
    print('example_strict_Linfinity_distance_lower_bound=319/9000')
    print(f'exact_parameter_cases={n}; full_deterministic_per_case=144; quantized=48_or_144')
    print('PASS_EXACT_R5_QUANTIZED_LR_PHASE_DIAGRAM')


if __name__=='__main__':
    test()
