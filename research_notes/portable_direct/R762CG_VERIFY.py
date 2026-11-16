#!/usr/bin/env python3
"""Exact N-BRC verification for R762CG: finite integer branch counts and area carriers.

No float, pi, trigonometric, propagator or external numeric reference is used.
This program tests precisely the conditional Cell/Port/Link model in R762CG.
"""
from collections import Counter
from itertools import permutations, product
from math import comb
import hashlib
import json
from pathlib import Path

AXES = tuple(range(6))

def unit(axis, sign=1):
    p = [0] * 6
    p[axis] = sign
    return tuple(p)

def neg(v):
    return tuple(-x for x in v)

def make_loops(axes, signs, j):
    a, b = axes[j], axes[(j + 1) % 3]
    u, v = unit(a, signs[j]), unit(b, signs[(j + 1) % 3])
    return ((u, neg(u), v, neg(v)),
            (u, v, neg(u), neg(v)),
            (v, u, neg(v), neg(u)))

def displacement(path):
    return tuple(sum(d[i] for d in path) for i in AXES)

def histogram(path):
    return Counter((i, 1 if d[i] > 0 else -1) for d in path for i in AXES if d[i])

def area(path, axes, signs):
    # Coefficients in the signed Port directions; formula is integral on closed loops.
    out = []
    for j in range(3):
        a, b = axes[j], axes[(j+1) % 3]
        running = 0
        a_coord = 0
        for d in path:
            a_coord += running * d[b]
            running += d[a]
        out.append(signs[j] * signs[(j+1)%3] * a_coord)
    return tuple(out)

def repair_bits(n):
    return (n - 1).bit_length()

def weight(q, r):
    return 2 if r == 0 else comb(q, r)

def signature(r, q, h):
    return tuple((r[j] + k) % q == 0 for j in range(3) for k in range(-h, h+1))

def verify():
    axes = (0, 1, 2)
    signs = (1, 1, 1)
    # Exact local area and signed-direction histogram in every S6 relabeling.
    relabel_tests = 0
    for p in permutations(AXES):
        for sg in product((-1,1), repeat=3):
            for j in range(3):
                B, Lp, Lm = make_loops(p[:3], sg, j)
                assert displacement(B) == displacement(Lp) == displacement(Lm) == (0,)*6
                assert histogram(B) == histogram(Lp) == histogram(Lm)
                expected = tuple(1 if z == j else 0 for z in range(3))
                assert area(B, p[:3], sg) == (0,0,0)
                assert area(Lp, p[:3], sg) == expected
                assert area(Lm, p[:3], sg) == tuple(-z for z in expected)
                relabel_tests += 1

    # Explicit concatenation law (for closed loops) and primitive cross-term identity.
    for j in range(3):
        B, Lp, Lm = make_loops(axes, signs, j)
        for A, D in product((B,Lp,Lm), repeat=2):
            assert area(A+D, axes, signs) == tuple(x+y for x,y in zip(area(A,axes,signs),area(D,axes,signs)))
    q_records = []
    for q in range(2, 11):
        # Actual N-BRC semiring convolution, not merely an arithmetic fit.
        hist = Counter({(0,): 1})
        for _ in range(q):
            nxt = Counter()
            for (r,), multiplicity in hist.items():
                nxt[(r,)] += multiplicity                # B branch
                nxt[((r+1)%q,)] += multiplicity          # L+ branch
            hist = nxt
        assert sum(hist.values()) == 2**q
        assert all(hist[(r,)] == weight(q,r) for r in range(q))
        # Three-port factorization, including the exact total source branch mass.
        weights = {r: weight(q,r) for r in range(q)}
        assert sum(weights.values())**3 == 2**(3*q)
        states = list(product(range(q), repeat=3))
        max_h = q+2
        horizon_classes=[]
        for h in range(max_h+1):
            grouped = {}
            for r in states:
                sig = signature(r,q,h)
                grouped[sig] = grouped.get(sig,0) + weights[r[0]]*weights[r[1]]*weights[r[2]]
            K = min(q,2*h+2)
            assert len(grouped) == K**3, (q,h,len(grouped),K**3)
            assert sum(grouped.values()) == 2**(3*q)
            horizon_classes.append([h,len(grouped),repair_bits(len(grouped))])
        for j in range(3):
            for k in range(-q-1, q+2):
                mass = sum(weights[r[0]]*weights[r[1]]*weights[r[2]] for r in states if (r[j]+k)%q == 0)
                assert mass == 2**(2*q) * weights[(-k)%q]
        # All-future distinctness: one Port and one signed-loop continuation separates any two.
        if q <= 6:
            for r in states:
                for s in states:
                    if r == s:
                        continue
                    j = next(j for j in range(3) if r[j]!=s[j])
                    k = (-r[j]) % q
                    assert (r[j]+k)%q==0 and (s[j]+k)%q != 0
        q_records.append(dict(q=q,branches=2**(3*q),all_future_classes=q**3,
                              all_future_bits=repair_bits(q**3),
                              one_port_weights=[weights[r] for r in range(q)],
                              horizons=horizon_classes))
    # Exhaust all 2^(3q) explicit ordered sources for q <= 4.
    for q in range(2,5):
        c = Counter()
        loops = [make_loops(axes, signs, j) for j in range(3)]
        for bits in product((0,1), repeat=3*q):
            full_path = ()
            for j in range(3):
                for i in range(q):
                    full_path += loops[j][bits[j*q+i]]
            assert displacement(full_path) == (0,)*6
            # Every source branch has the identical signed histogram and elapsed time.
            assert len(full_path) == 12*q
            h = histogram(full_path)
            for axis in range(3):
                assert h[(axis,1)] == 2*q and h[(axis,-1)] == 2*q
            r = tuple(a % q for a in area(full_path,axes,signs))
            c[r]+=1
        assert len(c) == q**3
        for r in product(range(q),repeat=3):
            assert c[r] == weight(q,r[0])*weight(q,r[1])*weight(q,r[2])

    evidence = {
        'schema':'R762CG_EXACT_N_BRC_EVIDENCE_V1',
        'result':'PASS',
        'arithmetic':'exact_nonnegative_integer_branch_multiplicity',
        'BRC_carrier':'N-BRC labelled ordered-loop path branches; group algebra N[(Z/qZ)^3]',
        'input':'P000 signed X6; three named signed Ports with distinct axes; B, L+, L- four-primitive-step loops; fixed q',
        'observer':'endpoint Cell, named signed Ports, directed cyclic Links, elapsed primitive-step time, signed-direction histogram',
        'future_scope':'terminal Port guard after k signed oriented loops with |k|<=h; separately all finite future macro-event sequences',
        'relabel_and_sign_checks':relabel_tests,
        'q_range':list(range(2,11)),
        'explicit_source_enumeration_q':[2,3,4],
        'closed_path_area':'A_j(H)=s_j s_(j+1) sum_{p<t} delta_p[a_j] delta_t[a_(j+1)]',
        'source_counts':q_records,
        'not_checked':'genuine native TRIADIC_CLOSURE_E license; V17/V29/V39 transport; physical calibration; independent review'
    }
    return evidence

if __name__ == '__main__':
    e=verify()
    path = Path(__file__).with_name('R762CG_EVIDENCE.json')
    path.write_text(json.dumps(e,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print('PASS relabel/sign tests',e['relabel_and_sign_checks'])
    for o in e['source_counts']:
        print('q=%s branches=%s classes=%s bits=%s'%(o['q'],o['branches'],o['all_future_classes'],o['all_future_bits']))
    print('sha256 evidence',hashlib.sha256(path.read_bytes()).hexdigest())
