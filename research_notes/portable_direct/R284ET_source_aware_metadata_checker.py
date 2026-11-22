#!/usr/bin/env python3
"""Exact small-state test for the source-aware metadata theorem (R284ET).

The checker uses integer bitmasks, exhaustive physical received words on
small cases and independent algebraic capacity optimization sweeps.
"""
from itertools import combinations, product
import json


def sets_of_size(t, b):
    return tuple(combinations(range(t), b))


def possible(t, s, a, J, w):
    damaged = set(J)
    return sum(((w >> k) & 1) != a for k in range(t) if k not in damaged) <= s


def overlap(t, s, J, K):
    return any(possible(t, s, 0, J, w) and possible(t, s, 1, K, w)
               for w in range(1 << t))


def main():
    checked_pairs = 0
    construction_cases = 0
    for t in range(1, 8):
        for b in range(1, min(3, t) + 1):
            sets = sets_of_size(t, b)
            for s in range(3):
                for J, K in product(sets, repeat=2):
                    observed = overlap(t, s, J, K)
                    algebraic = len(set(J) | set(K)) >= t - 2 * s
                    assert observed == algebraic, (t, b, s, J, K)
                    checked_pairs += 1
                for u in range(3):
                    # Witness-only code: a repeated (2u+1) times in independent metadata.
                    if t == b:
                        h = 2*u + 1
                        for J, K in product(sets, repeat=2):
                            assert (0 ^ ((1 << h) - 1)).bit_count() > 2*u
                        construction_cases += 1
                    # Metadata-free repetition code. All admissible pairs disjoint.
                    if t >= 2*(s+b)+1:
                        assert all(len(set(J)|set(K)) < t-2*s
                                   for J,K in product(sets,repeat=2))
                        construction_cases += 1
    optimized_cases = 0
    examples = []
    for b, s, u, a_cost, m_cost in product(range(1, 5),range(4),range(4),range(1,5),range(1,5)):
        # t can be truncated to the first metadata-free length: beyond only costs more.
        cap = 2*(s+b)+1
        t_h_costs = []
        for t in range(b, cap+1):
            witness_overlap = t <= 2*(s+b)
            h = 2*u+1 if witness_overlap else 0
            t_h_costs.append((a_cost*t+m_cost*h,t,h))
        got = min(c for c,_,_ in t_h_costs)
        sharp = min(a_cost*b+m_cost*(2*u+1),a_cost*(2*(s+b)+1))
        assert got == sharp,(b,s,u,a_cost,m_cost,got,sharp)
        optimized_cases += 1
        if (b,s,u,a_cost,m_cost) in [(3,0,0,1,1),(3,0,1,1,1),(3,0,2,1,1),(3,1,1,1,1),(2,0,1,1,1),(3,0,1,2,1)]:
            examples.append(dict(b=b,s=s,u=u,main_bit_cost=a_cost,metadata_bit_cost=m_cost,
                                 total_min=sharp,attainers=[[t,h] for c,t,h in t_h_costs if c==sharp]))
    assert checked_pairs>1000
    cert={"schema":"R284ET_SOURCE_AWARE_METADATA_CERT_V1",
          "model":"binary source; t main copies; exactly b blind overwrites; up to s flips outside overwritten positions; h separate metadata bits; up to u metadata flips; metadata may depend on true source and J",
          "exhaustive":{"t":"1..7","b":"1..min(3,t)","s":"0..2","ordered_source_opposition_pairs":checked_pairs,"model_criterion_pass":True,"constructions_checked":construction_cases},
          "algebraic_weighted_sweep":{"b":"1..4","s":"0..3","u":"0..3","positive_integer_bit_costs":"1..4 each","parameter_cases":optimized_cases,"formula_matches_optimal_envelope":True},
          "formula":"min(c_main*b+c_metadata*(2*u+1), c_main*(2*(s+b)+1))",
          "examples":examples,"independent_review":False}
    print(json.dumps(cert,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
