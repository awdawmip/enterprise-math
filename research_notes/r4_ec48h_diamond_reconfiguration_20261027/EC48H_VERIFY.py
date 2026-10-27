#!/usr/bin/env python3
"""EC48H: exact rational test of a two-decoder collision-face reconfiguration.

Auxiliary finite positive two-stage BRC model only. No native X6 dynamics are tested.
"""
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import pathlib

PATTERN = (
    ('H', 'M', 'L'),
    ('H', 'L', 'M'),
    ('M', 'M', 'L'),
    ('M', 'L', 'M'),
)
T_GRID = (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))


def source(q_raw, levels):
    assert len(q_raw) == 12 and all(x > 0 for x in q_raw)
    Praw = [F(q_raw[3 * h + y]) * levels[PATTERN[h][y]]
            for h in range(4) for y in range(3)]
    Psum, Qsum = sum(Praw), sum(q_raw)
    p = [[v / Psum for v in Praw[3 * h:3 * h + 3]] for h in range(4)]
    q = [[F(v, Qsum) for v in q_raw[3 * h:3 * h + 3]] for h in range(4)]
    return p, q


def coordinates(p, q, enc, dec):
    # deterministic history encoder; decoder probabilities per (memory label, y)
    assert len(enc) == 4 and all(m in (0, 1) for m in enc)
    assert len(dec) == 2 and all(len(row) == 3 for row in dec)
    assert all(0 <= x <= 1 for row in dec for x in row)
    alpha = sum((p[h][y] * dec[enc[h]][y]
                 for h in range(4) for y in range(3)), F(0))
    beta = sum((q[h][y] * dec[enc[h]][y]
                for h in range(4) for y in range(3)), F(0))
    return alpha, beta


def face(p, q, r):
    v = sum((max(p[h][y] - r * q[h][y], F(0))
             for h in range(4) for y in range(3)), F(0))
    beta_low = sum((q[h][y] for h in range(4) for y in range(3)
                    if p[h][y] > r * q[h][y]), F(0))
    tied_q = sum((q[h][y] for h in range(4) for y in range(3)
                  if p[h][y] == r * q[h][y]), F(0))
    return v, beta_low, beta_low + tied_q


def segments(label):
    # A decoder row is an exact conditional P-decision probability vector.
    if label == 'L':
        for s in T_GRID:
            yield 'L', s, (0, 1, 0, 1), ((F(1), F(1), s), (F(1), s, F(1)))
    elif label == 'M':
        # Complete high-collision face: four tied histories, two decoders.
        for s in T_GRID:
            yield 'M1', s, (1, 1, 0, 0), ((s, F(0), F(0)), (F(1), F(0), F(0)))
        for s in T_GRID:
            yield 'M2', s, (1, 0, 1, 0), ((F(1), F(0), F(0)), (F(1), s, F(0)))
        for s in T_GRID:
            yield 'M3', s, (1, 0, 1, 0), ((F(1), F(0), s), (F(1), F(1), F(0)))
    elif label == 'H':
        for s in T_GRID:
            yield 'H', s, (1, 1, 0, 0), ((F(0), F(0), F(0)), (s, F(0), F(0)))
    else:
        raise ValueError(label)


def strict_profiles(p, q, ratio_levels):
    uniq = sorted({p[h][y]/q[h][y] for h in range(4) for y in range(3)})
    assert len(uniq) == 3
    intervals = (uniq[0] / 2, (uniq[0] + uniq[1]) / 2,
                 (uniq[1] + uniq[2]) / 2, 2 * uniq[2])
    counts = []
    for r in intervals:
        signatures = {tuple(int(p[h][y] > r * q[h][y]) for y in range(3))
                      for h in range(4)}
        counts.append(len(signatures))
    assert counts == [1, 2, 2, 1], (counts, uniq)
    return counts


def check_one(q_raw, levels):
    p, q = source(q_raw, levels)
    raw_r = {x: F(sum(q_raw), 1) * levels[x] /
             sum((F(q_raw[3*h+y]) * levels[PATTERN[h][y]]
                  for h in range(4) for y in range(3)), F(0))
             for x in ('L','M','H')}
    strict_profiles(p, q, raw_r)
    checks = 0
    for label in ('L', 'M', 'H'):
        r = raw_r[label]
        support, beta_min, beta_max = face(p, q, r)
        previous = None
        sampled = []
        for stage, s, enc, dec in segments(label):
            a, b = coordinates(p, q, enc, dec)
            assert a - r * b == support, (label, stage, s, a, b, support)
            assert beta_min <= b <= beta_max
            if previous is not None:
                assert b >= previous, (label, stage, s, b, previous)
            previous = b
            sampled.append((stage, s, b))
            checks += 2
        assert sampled[0][2] == beta_min and sampled[-1][2] == beta_max
        checks += 2
    return checks


def ff(x):
    return f'{x.numerator}/{x.denominator}'


def main():
    # Exhaustive grid of all 2^12 positive Q integer tables in {1,2}.
    levels = {'L':F(1,2), 'M':F(1), 'H':F(2)}
    examples = 0
    claims = 0
    for qraw in product((1,2), repeat=12):
        claims += check_one(qraw, levels)
        examples += 1

    # Shifted rational source ratios to verify normalization is handled correctly.
    extra = [
        {'L':F(1,3), 'M':F(5,4), 'H':F(7,2)},
        {'L':F(2,5), 'M':F(2), 'H':F(9,2)},
        {'L':F(1), 'M':F(5,3), 'H':F(9,4)},
    ]
    for j, other in enumerate(extra):
        for k in range(48):
            qraw = tuple(1 + ((i*i + 3*i + 7*j + 5*k + (k//(i+1))) % 9)
                         for i in range(12))
            claims += check_one(qraw, other)
            examples += 1

    qraw = (2,)*12
    p,q = source(qraw,levels)
    central = face(p,q,raw_r:=F(1))
    critical = {label: face(p,q,lv) for label,lv in levels.items()}
    sample = {
        'P_raw': [[int((p[h][y] * 24)) for y in range(3)] for h in range(4)],
        'Q_raw': [[2,2,2] for _ in range(4)],
        'P_total':24,'Q_total':24,
        'strict_profile_counts':[1,2,2,1],
        'K_hull':2,'K_seed':2,
        'central_support':ff(central[0]),
        'central_beta_start':ff(central[1]),
        'central_beta_finish':ff(central[2]),
        'central_phase_betas': [[ff(coordinates(p,q,enc,dec)[1])
                                 for stage,s,enc,dec in segments('M') if stage==st]
                                for st in ('M1','M2','M3')],
        'critical_faces': {label:{'r':ff(levels[label]),
            'support':ff(critical[label][0]),
            'beta_min':ff(critical[label][1]),
            'beta_max':ff(critical[label][2])} for label in ('L','M','H')}
    }
    report={
        'title':'EC48H diamond-reconfiguration exact rational witness',
        'model':'strictly-positive finite two-stage binary-decision BRC source; deterministic encoder, two stochastic decoder rows',
        'parameter_family':'P_raw[h,y]=Q_raw[h,y]*level[pattern[h,y]], Q_raw>0, 0<L<M<H',
        'exhaustive_Q_domain':'all 4096 Q_raw arrays {1,2}^(4x3), L=1/2,M=1,H=2',
        'extra_Q_domain':'3 rational level triples x 48 deterministic positive integer tables =144',
        'models_checked':examples,
        'exact_face_assertions':claims,
        'checker':'Python standard-library fractions.Fraction; boundary samples t=0,1/4,1/2,3/4,1',
        'universal_statement_basis':'constructive algebraic proof, not finite enumeration',
        'failed_assertions':0,
        'witness':sample,
        'sources':{
            'global_knowledge':'3ce6c9324e7c5af8d71c7adee778d084e7390d00',
            'enterprise_math':'52be5e12112a44131c998cebeb424eed5a663f15',
            'EC48G':'fd08c300cde18245565ce3b27d7ced523d35b627'
        },
        'remaining_problem':'does K_seed=K_hull for every finite positive two-stage BRC source, including multi-free collision patterns beyond the diamond family?'
    }
    print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
