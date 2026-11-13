#!/usr/bin/env python3
"""EC49Y: exact, finite terminal-face and no-omission certificate.

Uses the EC49X source laws but independently evaluates all endpoint vertices,
paid-code signal gains, optimal acceptance face and rational witness. The proof
that these finite checks cover all real unseeded policies is in PROOF.md.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import csv
import json

W = range(3)
U = range(2)
Z = range(3)
C = range(4)  # A0, A1, B0, B1
SIGMA = (1, 0, -1)
ETA = F(1, 200)
BMAX = F(1, 16)
TARGET_C1 = F(43, 48)
TARGET_C2 = F(7, 8)
DELTA_STAR = F(59, 576)
FACE_A0 = F(109, 192)
FACE_A1 = F(133, 192)


def signal(w, u):
    return F(1, 2) + (2*u-1)*ETA*SIGMA[w]


def law(R, w, z):
    if R == 'Q':
        return F(1, 9)
    if R == 'P':
        return F(1, 6) if w == z else F(1, 12)
    raise ValueError(R)


def mass(R, w, u, z):
    return law(R, w, z)*signal(w, u)


def terminal_mass(prefix, R, c, u, z):
    return sum(prefix[w][c]*mass(R, w, u, z) for w in W)


def contrast(prefix, c, u, z):
    return terminal_mass(prefix, 'P', c, u, z)-terminal_mass(prefix, 'Q', c, u, z)


def gain(prefix, c, u):
    return sum(max(F(0), contrast(prefix, c, u, z)) for z in Z)


def discrimination_relaxation(prefix):
    return sum(gain(prefix, c, u) for c in C for u in U)


def paid_mass(prefix, c, u):
    return sum(prefix[w][c]*signal(w, u) for w in W)


def prefix_vertex(stop_w, expensive_w, a_labels, b_label, b):
    h=F(5,16)+b
    p=[[F(0) for _ in C] for _ in W]
    for w in W:
        stop=h if w == stop_w else F(0)
        expensive=b if w == expensive_w else F(0)
        p[w][a_labels[w]] = 1-stop-expensive
        p[w][b_label] += expensive
        assert sum(p[w]) <= 1
    assert sum(p[w][c]*(1 if c < 2 else 2) for w in W for c in C) == 3*TARGET_C1
    return p


def positive_face(prefix):
    positive_p=F(0)
    positive_q=F(0)
    zero_p=F(0)
    for c,u,z in product(C,U,Z):
        d=contrast(prefix,c,u,z)
        p=terminal_mass(prefix,'P',c,u,z)
        q=terminal_mass(prefix,'Q',c,u,z)
        if d>0:
            positive_p += p
            positive_q += q
        elif d==0:
            assert p==q
            zero_p += p
    stop=sum(1-sum(prefix[w]) for w in W)/3
    return (positive_p,positive_q,positive_p+zero_p+stop,
            positive_q+zero_p+stop,zero_p,stop)


def witness(r):
    # W2: 3/8 STOP; paid paths all buy S. r is STOP acceptance.
    p=[
      [F(1),F(0),F(0),F(0)],
      [F(0),F(1),F(0),F(0)],
      [F(9,16),F(0),F(1,16),F(0)],
    ]
    source_accept={}
    for R in ('P','Q'):
        paid=sum(terminal_mass(p,R,c,u,z)
                 for c,u,z in product(C,U,Z) if contrast(p,c,u,z)>0)
        stop=sum((1-sum(p[w]))/3*r for w in W)
        source_accept[R]=paid+stop
    c1=sum(p[w][c]*(1 if c<2 else 2) for w in W for c in C)/3
    c2=sum(p[w][c] for w in W for c in C)/3
    return source_accept['P'],source_accept['Q'],c1,c2


def run():
    for R in ('P','Q'):
        leaves=[mass(R,w,u,z) for w,u,z in product(W,U,Z)]
        assert len(leaves)==18 and all(q>0 for q in leaves)
        assert sum(leaves)==1
    assert all(sum(mass('P',w,u,z)-mass('Q',w,u,z) for z in Z)==0
               for w,u in product(W,U))

    counts=[]
    records=[]
    smallest_positive_gain=None
    for b in (F(0), BMAX):
        maximizers=0
        maxval=F(-1)
        for i,j,labels,blabel in product(W,W,product((0,1),repeat=3),(2,3)):
            p=prefix_vertex(i,j,labels,blabel,b)
            d=discrimination_relaxation(p)
            if d>maxval:
                maxval=d
            records.append({'b':str(b),'stop_w':i,'B_w':j,
                            'A_labels':''.join(map(str,labels)),
                            'B_label':blabel,'D':str(d)})
            if d!=DELTA_STAR:
                continue
            maximizers+=1
            for c,u in product(C,U):
                mass_cu=paid_mass(p,c,u)
                gain_cu=gain(p,c,u)
                assert mass_cu>=0 and gain_cu>=0
                # No maximizing endpoint has a paid but blind code-and-u state.
                assert mass_cu==0 or gain_cu>0, (b,i,j,labels,blabel,c,u)
                if mass_cu>0 and (smallest_positive_gain is None or gain_cu<smallest_positive_gain):
                    smallest_positive_gain=gain_cu
            if b==BMAX:
                low_p,low_q,high_p,high_q,zero,stop=positive_face(p)
                assert (low_p,low_q,high_p,high_q,zero,stop)==(
                  FACE_A0,FACE_A0-DELTA_STAR,FACE_A1,FACE_A1-DELTA_STAR,F(0),F(1,8))
        assert maxval==DELTA_STAR, (str(b),str(maxval))
        counts.append({'b':str(b),'max_D':str(maxval),'maximizers':maximizers})
    assert counts[0]['maximizers']==72 and counts[1]['maximizers']==48
    assert len(records)==288

    for r in (F(0),F(1,3),F(1)):
        a,b,c1,c2=witness(r)
        assert (a,b,c1,c2)==(FACE_A0+r/F(8),FACE_A0-DELTA_STAR+r/F(8),TARGET_C1,TARGET_C2)
        assert a-b==DELTA_STAR

    folder=Path(__file__).resolve().parent
    with (folder/'ENDPOINT_CENSUS.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['b','stop_w','B_w','A_labels','B_label','D'])
        writer.writeheader();writer.writerows(records)
    report={
        'schema':'EC49Y_EXACT_MAXIMAL_ACCEPTANCE_FACE_V1',
        'status':'AUTHOR_PROVED / FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED',
        'model':{'eta':str(ETA),'C1':str(TARGET_C1),'C2':str(TARGET_C2),
                 'source_positive_rational_leaves_each':18,
                 'randomization':'independent source-blind fresh behavioral coins; no persistent common seed'},
        'endpoint_certificate':{'total_vertices':len(records),'groups':counts,
             'smallest_gain_over_used_code_U_in_max_endpoint_vertices':str(smallest_positive_gain),
             'no_blind_code_U_in_max_endpoint_vertices':True,
             'max_b_endpoint_same_optimal_acceptance_interval':True},
        'proven_all_real':{'delta_star':str(DELTA_STAR),
           'every_delta_star_policy_senses_S_on_all_positive_probability_paid_paths':True,
           'face_alpha':['109/192','133/192'],
           'face_beta':['67/144','85/144'],
           'face_relation':'beta=alpha-59/576'},
        'rational_realization':{'prefix':'W0:A0, W1:A1, W2:A0 with 9/16, B0 with 1/16, STOP with 3/8',
            'S':'buy with probability 1 on every paid path',
            'accept':'positive signed-contrast cells, plus STOP with probability r',
            'formula':'alpha=109/192+r/8, beta=67/144+r/8, 0<=r<=1',
            'sample_r':['0','1/3','1']},
        'bounds':'Applies only to the alpha-beta=59/576 maximal slice at fixed exact C1,C2; not whole (alpha,beta) image.',
        'provenance':'All-real reduction supplied in PROOF.md; 288 endpoints checked exactly with Python fractions.'
    }
    (folder/'EXACT_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('EC49Y EXACT PASS', 'vertices',len(records),'maximizers',counts,
          'minimum_used_gain',smallest_positive_gain,
          'face alpha',FACE_A0,FACE_A1, 'delta', DELTA_STAR)


if __name__=='__main__':
    run()
