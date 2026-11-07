#!/usr/bin/env python3
"""Exact finite BRC branch-mass witness for Stage300-B.

All assertions use fractions.Fraction. This program checks the finite witness,
1024 deterministic source-blind adaptive examiners, and explicit certificates.
The continuum lower bound is established in the accompanying proof, not by
finite sampling.
"""
from fractions import Fraction as F
from itertools import product

Z = F(0)
ONE = F(1)
HALF = F(1, 2)
PARAMS = (F(1, 4), F(3, 4))
BITS3 = tuple(product((0, 1), repeat=3))

def bern(p, b):
    return p if b else ONE - p

def tv(p, q):
    assert set(p) == set(q)
    return sum(abs(p[k] - q[k]) for k in p) / 2

def static_source(s, actions):
    """X fair; each H draws Ber(1/2); each F draws Ber(p_s)."""
    p = PARAMS[s]
    out = {}
    for x, y1, y2 in BITS3:
        out[(x, y1, y2)] = HALF * bern(HALF if actions[0]=='H' else p, y1) * bern(HALF if actions[1]=='H' else p, y2)
    assert sum(out.values()) == 1 and all(w > 0 for w in out.values())
    return out

def iid_shared_pre_mix(mixture):
    """One Theta chosen initially, all three bits conditionally IID Ber(Theta)."""
    assert sum(weight for _, weight in mixture) == 1
    assert all(0 <= p <= 1 and weight > 0 for p, weight in mixture)
    return {
        word: sum(weight * bern(p, word[0]) * bern(p, word[1]) * bern(p, word[2])
                  for p, weight in mixture)
        for word in BITS3
    }

def pooled(p, q):
    return {k: (p[k] + q[k])/2 for k in p}

def policy_path_law(source, a1_map, a2_map):
    """Path key (x,a1,y1,a2,y2). The common examiner sees only x,a1,y1."""
    rates = (HALF, PARAMS[source]) # H=0, F=1
    out = {}
    for x in (0, 1):
        a1 = a1_map[x]
        for y1 in (0, 1):
            a2 = a2_map[(x, a1, y1)]
            for y2 in (0, 1):
                out[(x, a1, y1, a2, y2)] = HALF * bern(rates[a1], y1) * bern(rates[a2], y2)
    assert sum(out.values()) == 1 and all(v > 0 for v in out.values())
    return out

def free_mixture_path_law(a1_map, a2_map):
    """Source-blind causal Bayes kernel implementing the exact pooled law."""
    out = {}
    for x in (0, 1):
        a1 = a1_map[x]
        for y1 in (0, 1):
            p0 = bern(HALF if a1 == 0 else PARAMS[0], y1)
            p1 = bern(HALF if a1 == 0 else PARAMS[1], y1)
            prior_obs = (p0 + p1)/2
            rho0, rho1 = p0/(p0+p1), p1/(p0+p1)
            a2 = a2_map[(x,a1,y1)]
            q_next = (rho0*(HALF if a2 == 0 else PARAMS[0])
                      + rho1*(HALF if a2 == 0 else PARAMS[1]))
            for y2 in (0, 1):
                out[(x,a1,y1,a2,y2)] = HALF * prior_obs * bern(q_next, y2)
    assert sum(out.values()) == 1 and all(v > 0 for v in out.values())
    return out

def all_deterministic_policies():
    for p1 in product((0,1),repeat=2):
        a1map = {x:p1[x] for x in (0,1)}
        for p2 in product((0,1),repeat=8):
            hists=tuple(product((0,1),repeat=3))
            a2map={h:p2[j] for j,h in enumerate(hists)}
            yield a1map,a2map

def main():
    P0 = static_source(0, 'FF')
    P1 = static_source(1, 'FF')
    M = pooled(P0,P1)
    expected = [F(x,32) for x in (5,3,3,5,5,3,3,5)]
    assert [M[w] for w in BITS3] == expected
    assert tv(P0,P1)==F(1,2)
    for actions in ('HH','HF','FH'):
        assert pooled(static_source(0,actions),static_source(1,actions)) == {w:F(1,8) for w in BITS3}

    mu_pool = ((F(1,4),F(1,6)),(F(1,2),F(2,3)),(F(3,4),F(1,6)))
    Qpool = iid_shared_pre_mix(mu_pool)
    assert [Qpool[w] for w in BITS3]==[F(5,32),F(11,96),F(11,96),F(11,96),F(11,96),F(11,96),F(11,96),F(5,32)]
    assert tv(M,Qpool)==F(1,12)
    # The analytic L1 orbit lower certificate holds for every exchangeable Q:
    # x_k=32 Q(word with k ones), t=x1+x2,
    # L1*32>= (t-2)+|22-3t|>=16/3; hence TV>=1/12.
    x=[32*Qpool[(0,)* (3-k) + (1,)*k] for k in range(4)]
    assert sum((F(1),F(3),F(3),F(1))[i]*x[i] for i in range(4))==32
    assert x == [F(5),F(11,3),F(11,3),F(5)]
    assert (x[1]+x[2]-2)+abs(22-3*(x[1]+x[2]))==F(16,3)

    mu_tag = ((F(0),F(3,16)),(F(1,2),F(3,4)),(F(1),F(1,16)))
    Qtag = iid_shared_pre_mix(mu_tag)
    assert [Qtag[w] for w in BITS3]==[F(x,32) for x in (9,3,3,3,3,3,3,5)]
    assert tv(P0,Qtag)==F(3,16) and tv(P1,Qtag)==F(5,16)
    assert (tv(P0,Qtag)+tv(P1,Qtag))/2 == F(1,4)
    assert (tv(P0,M)+tv(P1,M))/2 == F(1,4)
    assert tv(M,Qtag) == F(1,8)

    policies=0
    positive_source_paths=0
    for a1map,a2map in all_deterministic_policies():
        A=policy_path_law(0,a1map,a2map)
        B=policy_path_law(1,a1map,a2map)
        C=free_mixture_path_law(a1map,a2map)
        assert C == pooled(A,B)
        assert tv(A,B)<=F(1,2)
        positive_source_paths += len(A)+len(B)
        policies+=1
    assert policies == 1024 and positive_source_paths==1024*16

    print('source_FF_word_laws:', [str(P0[w]) for w in BITS3], [str(P1[w]) for w in BITS3])
    print('pooled_FF:', [str(M[w]) for w in BITS3])
    print('exact_pooled_iid_TV_infimum=1/12; rational_3_atom_witness=PASS')
    print('source_labelled_pair_TV=1/2; free_and_shared_IID_tagged_optimum=1/4')
    print('tagged_iid_witness: TV_s0=3/16, TV_s1=5/16, pooled_TV=1/8')
    print('one_or_zero_F_interventions_pooled_uniform=PASS')
    print(f'adaptive_source_blind_bayes_exact_policies={policies}, positive_source_paths={positive_source_paths}')
    print('STAGE300B_INTERVENTIONAL_MIXTURE_EXACT_PASS')

if __name__=='__main__':
    main()
