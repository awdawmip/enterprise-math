#!/usr/bin/env python3
"""Exact constructive witness for EC48L, finite two-source horizon-two model.
All arithmetic is fractions.Fraction; no float and no external dependencies.
"""
from fractions import Fraction as F
from collections import defaultdict
import json
import random


def qstr(x):
    return f"{x.numerator}/{x.denominator}"


def exact_model(leaves, continue_prob, stop_accept, term_accept):
    """leaves: (history, P_raw, Q_raw), positive integer masses."""
    histories = sorted({h for h, _, _ in leaves})
    np = sum(p for _, p, _ in leaves)
    nq = sum(q for _, _, q in leaves)
    assert np > 0 and nq > 0
    L = [(h, F(p, np), F(q, nq)) for h, p, q in leaves]
    pm, qm = defaultdict(F), defaultdict(F)
    for h, p, q in L:
        assert p > 0 and q > 0
        pm[h] += p
        qm[h] += q
    assert sum(pm.values()) == sum(qm.values()) == 1
    assert set(continue_prob) == set(stop_accept) == set(histories)
    assert len(term_accept) == len(L)
    for h in histories:
        assert 0 <= continue_prob[h] <= 1
        assert 0 <= stop_accept[h] <= 1-continue_prob[h]
    assert all(0 <= z <= 1 for z in term_accept)

    # Aggregate the two decision stages by exactly the likelihood-ratio fibers.
    er_num, er_den = defaultdict(F), defaultdict(F)
    tr_num, tr_den = defaultdict(F), defaultdict(F)
    for h in histories:
        lr = pm[h] / qm[h]
        er_num[lr] += qm[h] * stop_accept[h]
        er_den[lr] += qm[h] * (1-continue_prob[h])
    for (h, p, q), z in zip(L, term_accept):
        lr = p/q
        tr_num[lr] += q * continue_prob[h] * z
        tr_den[lr] += q * continue_prob[h]
    eta = {r: er_num[r] / er_den[r] if er_den[r] else F(0) for r in er_den}
    theta = {r: tr_num[r] / tr_den[r] if tr_den[r] else F(0) for r in tr_den}
    assert all(0 <= v <= 1 for v in eta.values())
    assert all(0 <= v <= 1 for v in theta.values())

    # Full-history policy readout.
    af = sum((pm[h] * stop_accept[h] for h in histories), F(0))
    bf = sum((qm[h] * stop_accept[h] for h in histories), F(0))
    tfp = 1 + sum((pm[h] * continue_prob[h] for h in histories), F(0))
    tfq = 1 + sum((qm[h] * continue_prob[h] for h in histories), F(0))
    for (h, p, q), z in zip(L, term_accept):
        af += p * continue_prob[h] * z
        bf += q * continue_prob[h] * z

    # B1 encoder b=1 with probability continue_prob[h]. Decoder:
    # b=1 continue; b=0 stop and accept with eta(stage-1 LR).
    # At terminal b=1 and accept with theta(terminal LR).
    ab = sum((pm[h] * (1-continue_prob[h]) * eta[pm[h]/qm[h]] for h in histories), F(0))
    bb = sum((qm[h] * (1-continue_prob[h]) * eta[pm[h]/qm[h]] for h in histories), F(0))
    tbp = 1 + sum((pm[h] * continue_prob[h] for h in histories), F(0))
    tbq = 1 + sum((qm[h] * continue_prob[h] for h in histories), F(0))
    for h, p, q in L:
        ab += p * continue_prob[h] * theta[p/q]
        bb += q * continue_prob[h] * theta[p/q]
    full = (af, bf, tfp, tfq)
    one_bit = (ab, bb, tbp, tbq)
    assert full == one_bit, (full, one_bit)
    return {"full_readout": [qstr(x) for x in full],
            "one_bit_readout": [qstr(x) for x in one_bit],
            "first_stage_accept_fibers": {qstr(k): qstr(v) for k,v in sorted(eta.items())},
            "terminal_accept_fibers": {qstr(k): qstr(v) for k,v in sorted(theta.items())}}


def run():
    fixture = [('A',3,1),('A',1,3),('B',1,3),('B',3,1),('C',2,2),('C',2,2)]
    t = {'A':F(1,4),'B':F(2,3),'C':F(1,2)}
    a = {'A':F(1,8),'B':F(1,9),'C':F(1,4)}
    z = [F(0),F(1,2),F(1),F(1,4),F(1,3),F(2,3)]
    witness = exact_model(fixture,t,a,z)
    rng = random.Random(4848127)
    count=0
    # Enumerate stochastic policies and positive trees with collision-heavy mass values;
    # includes zero denominators, deterministic and genuinely randomized actions.
    for n in range(1,9):
        for repetition in range(300):
            arr=[]; zs=[]
            for i in range(n):
                k=rng.randint(1,4)
                for _ in range(k):
                    arr.append((f'h{i}',rng.randint(1,9),rng.randint(1,9)))
                    zs.append(rng.choice([F(0),F(1),F(1,2),F(1,3),F(2,5)]))
            tr={}; ar={}
            for i in range(n):
                h=f'h{i}'
                tr[h]=rng.choice([F(0),F(1),F(1,2),F(1,3),F(2,3),F(3,4)])
                ar[h]=(1-tr[h])*rng.choice([F(0),F(1),F(1,2),F(1,3),F(3,5)])
            exact_model(arr,tr,ar,zs)
            count+=1
    return {'schema':'EC48L_EXACT_TWO_STAGE_B1_V1','models_checked':count+1,
            'fixture':witness,'random_seed':4848127,
            'random_model_domain':'n=1..8, 300 seeded positive-integer trees per n; 1..4 leaves/history; raw P,Q masses 1..9; rational random stage actions',
            'numeric_method':'fractions.Fraction, exact identities, no floating point',
            'assertion_failures':0,'theorem_proof':'constructive fiber-preserving formulas in PROOF.md',
            'formal_checker':'NOT_RUN','project_admission':'UNREVIEWED_NOT_ADMITTED'}


if __name__ == '__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
