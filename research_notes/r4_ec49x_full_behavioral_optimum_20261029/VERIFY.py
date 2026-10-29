#!/usr/bin/env python3
"""EC49X: exact finite certificate for full unseeded behavioral delta optimum.

All mathematical inputs are finite rational numbers. Standard library only.
The universal reduction (convexity and prefix/post-U factorization) is in PROOF.md;
this checker exhaustively evaluates the complete 144-vertex family at each of
b=0 and b=1/16. A pass is not independent review or native acceptance.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import csv
import json

W = range(3)
U = range(2)
Z = range(3)
C = range(4)  # A0,A1,B0,B1
SIGMA = (1, 0, -1)
ETA = F(1, 200)
C1_TARGET = F(43, 48)
C2_TARGET = F(7, 8)
OPTIMUM = F(59, 576)


def signal(w, u):
    return F(1, 2) + (2*u-1)*ETA*SIGMA[w]


def mass(source, w, z):
    if source == 'Q':
        return F(1, 9)
    assert source == 'P'
    return F(1, 6) if w == z else F(1, 12)


def signed_leaf(w, u, z):
    return (mass('P', w, z) - mass('Q', w, z))*signal(w, u)


def max_difference(prefix):
    # Exact optimal accept/reject after buying S in each (code,u,z) cell.
    return sum(
        max(F(0), sum(prefix[w][c]*signed_leaf(w, u, z) for w in W))
        for c in C for u in U for z in Z
    )


def witness_point(prefix, masks):
    accept = {}
    for source in ('P', 'Q'):
        accept[source] = sum(
            prefix[w][c]*mass(source, w, z)*signal(w, u)
            for w in W for c in C for u in U for z in Z
            if z in masks.get(c, ())
        )
    c1 = sum(prefix[w][c]*(1 if c < 2 else 2) for w in W for c in C)/3
    c2 = sum(prefix[w][c] for w in W for c in C)/3
    return accept['P'], accept['Q'], c1, c2


def vertex(stop_w, b_w, a_tags, b_tag, b):
    stop_total = F(5, 16)+b
    prefix = [[F(0) for _ in C] for _ in W]
    for w in W:
        stop = stop_total if w == stop_w else F(0)
        bmass = b if w == b_w else F(0)
        assert stop+bmass <= 1
        prefix[w][a_tags[w]] = 1-stop-bmass
        prefix[w][b_tag] += bmass
    assert sum(prefix[w][c] for w in W for c in (2, 3)) == b
    assert sum(prefix[w][c]*(1 if c < 2 else 2)
               for w in W for c in C) == F(43, 16)
    return prefix


def sample_factorization_check():
    # General cost residual and partial-purchase contraction, not fixed-cost.
    checked = 0
    for idx in range(64):
        p = [[F((7*w + 3*c + idx) % 8 + 1, 96) for c in C]
             for w in W]
        s = [[F((5*c + u + idx) % 7 + 1, 8) for u in U]
             for c in C]
        assert all(sum(p[w]) <= 1 for w in W)
        c1 = sum(p[w][c]*(1 if c < 2 else 2) for w in W for c in C)/3
        c2 = sum(p[w][c]*signal(w, u)*s[c][u]
                 for w in W for c in C for u in U)/3
        b = sum(p[w][c] for w in W for c in (2, 3))
        unsensed = sum(p[w][c]*signal(w, u)*(1-s[c][u])
                       for w in W for c in C for u in U)
        assert 3*(c1-c2) == b+unsensed
        partial = sum(
            s[c][u]*max(F(0),sum(p[w][c]*signed_leaf(w,u,z) for w in W))
            for c in C for u in U for z in Z)
        assert partial <= max_difference(p)
        checked += 1
    return checked


def run():
    for source in ('P','Q'):
        leaves = [mass(source,w,z)*signal(w,u)
                  for w in W for u in U for z in Z]
        assert len(leaves) == 18 and all(v > 0 for v in leaves)
        assert sum(leaves) == 1
        assert [sum(mass(source,w,z) for z in Z) for w in W] == [F(1,3)]*3
    assert all(sum(signed_leaf(w,u,z) for z in Z)==0 for w in W for u in U)

    cert=[]
    endpoints=[]
    for b in (F(0), F(1,16)):
        vals=[]
        for stop_w,b_w in product(W,W):
            for tags in product((0,1),repeat=3):
                for btag in (2,3):
                    p = vertex(stop_w,b_w,tags,btag,b)
                    value = max_difference(p)
                    vals.append(value)
                    cert.append({
                        'b':str(b),'stop_w':stop_w,'b_w':b_w,
                        'a_tags':''.join(map(str,tags)), 'b_tag':btag,
                        'delta_exact':str(value)
                    })
        assert len(vals) == 144
        best = max(vals)
        assert best == OPTIMUM,(str(b),str(best))
        endpoints.append({'b':str(b),'vertices':len(vals),
                          'max_delta':str(best),
                          'maximizing_labeled_vertices':sum(x==best for x in vals)})

    p = [
        [F(1),F(0),F(0),F(0)],
        [F(0),F(1),F(0),F(0)],
        [F(9,16),F(0),F(1,16),F(0)]
    ]
    # W2 has STOP probability 3/8. All purchased histories buy S.
    alpha,beta,c1,c2 = witness_point(p,{0:{0,2},1:{1},2:{2}})
    assert (alpha,beta,c1,c2) == (F(109,192),F(67,144),C1_TARGET,C2_TARGET)
    assert alpha-beta == OPTIMUM
    assert max_difference(p) == OPTIMUM

    check_count=sample_factorization_check()
    base=Path(__file__).resolve().parent
    with (base/'ENDPOINT_VERTICES.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['b','stop_w','b_w','a_tags','b_tag','delta_exact'])
        writer.writeheader();writer.writerows(cert)
    report={
        'schema':'ENTERPRISE_MATH_EC49X_EXACT_FULL_BEHAVIORAL_OPTIMUM_V1',
        'input':{'eta':str(ETA),'source_leaves_per_source':18,
                 'stage1_cost':str(C1_TARGET),'stage2_cost':str(C2_TARGET),
                 'model':'EC49U/V/W positive-rational auxiliary BRC, no persistent shared random seed'},
        'source_leaves':'18 strictly positive rational leaves per source; normalized to 1; P(W,U)=Q(W,U)',
        'finite_certificate':{'endpoints':endpoints,'total_vertex_evaluations':len(cert),
          'tag_choices':'3 stop histories * 3 B histories * 2^3 A labels * 2 B labels',
          'interior':'bounded by convexity in b, not sampled'},
        'witness':{'alpha':str(alpha),'beta':str(beta),'C1':str(c1),'C2':str(c2),
          'delta':str(alpha-beta),'prefix':'W0:A0; W1:A1; W2:STOP 3/8, A0 9/16, B0 1/16; all paid paths buy S',
          'accept':'A0:z in {0,2}; A1:z=1; B0:z=2'},
        'full_behavioral_all_real_optimum':str(OPTIMUM),
        'proof_steps':['post-U cancellation and data contraction',
          'cost-deficit equality b + unsensed = 1/16',
          'two-simplex extremal reduction for fixed b',
          'convex endpoint reduction b in [0,1/16]',
          'exact 288-vertex Fraction certificate and rational attaining witness'],
        'generic_fraction_checks':check_count,
        'status':'AUTHOR_PROVED; FRACTION_CERT_PASS; UNREVIEWED; NOT_ADMITTED',
        'excluded':'signed/phase BRC, native X6 embedding, full fixed-cost (alpha,beta) region'
    }
    (base/'EXACT_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print('EC49X EXACT PASS',report['full_behavioral_all_real_optimum'],
          'vertices',len(cert),'witness',tuple(map(str,(alpha,beta,c1,c2))),
          'generic',check_count)

if __name__=='__main__':
    run()
