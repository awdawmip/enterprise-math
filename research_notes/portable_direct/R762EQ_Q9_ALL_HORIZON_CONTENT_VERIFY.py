#!/usr/bin/env python3
"""R762EQ — exact finite certificate for an ALL-HORIZON q=9 BRC theorem.

The accompanying mathematical proof uses an integral degree-729 recurrence
to lift these 2214 exact horizons to every n>=0. The six *named* positive
terminal BRC branches are preserved. No physical/native signed-event claim.

Standard library only. No floating point, pi, trigonometry, classical
propagators or approximation.
"""
import hashlib
import json

Q = 9
MAX_N = 2213
CAP = 744
MOD = 3 ** CAP
BRANCHES = (
    ("one", 0, 0, 0),
    ("X", 1, 0, 0),
    ("Z", 0, 0, 1),
    ("XY", 1, 1, 0),
    ("YZ", 0, 1, 1),
    ("XYZ", 1, 1, 1),
)

def addr(i, j, k, q):
    return (i*q + j)*q + k

def shift_maps(q):
    return [
        [addr((i-di)%q, (j-dj)%q, (k-dk)%q, q)
         for i in range(q) for j in range(q) for k in range(q)]
        for _name, di, dj, dk in BRANCHES
    ]

def step(a, maps):
    return [sum(a[p[i]] for p in maps) % MOD for i in range(len(a))]

def rank3(rows):
    pivots = {}
    for row in rows:
        v = list(row)
        for j in sorted(pivots):
            if v[j]:
                m = v[j]
                v = [(a-m*b)%3 for a,b in zip(v,pivots[j])]
        first = next((j for j,x in enumerate(v) if x), None)
        if first is not None:
            m = v[first]  # inverse of 1 or 2 in F3 equals itself
            pivots[first] = [(m*x)%3 for x in v]
    return len(pivots), sorted(pivots)

def main():
    maps9, maps3 = shift_maps(9), shift_maps(3)
    reduction = [addr(i%3,j%3,k%3,3)
                 for i in range(9) for j in range(9) for k in range(9)]
    a9, a3 = [1]+[0]*728, [1]+[0]*26
    powers3 = [3**i for i in range(CAP+1)]
    mass = 1
    base = []
    periodic_comparisons = 0

    for n in range(MAX_N+1):
        assert sum(a9)%MOD == mass, ("augmentation",n)
        reduced = [0]*27
        for source,v in enumerate(a9):
            j = reduction[source]
            reduced[j] = (reduced[j]+v)%MOD
        assert reduced == a3, ("q9_to_q3_observer",n)

        exponent = max(0,n//3-2)
        assert exponent < CAP
        d = powers3[exponent]
        assert all(v%d == 0 for v in a9), ("lower_content_bound",n)
        shadow = bytes((v//d)%3 for v in a9)
        assert any(shadow), ("nondivisibility_witness",n)

        if n >= 9:
            if n < 27:
                base.append(shadow)
            else:
                assert shadow == base[(n-9)%18], ("18_step_shadow",n)
                periodic_comparisons += 1

        if n < MAX_N:
            a9 = step(a9,maps9)
            a3 = step(a3,maps3)
            mass = (mass*6)%MOD

    assert len(base)==18 and periodic_comparisons==2187
    rank,pivots = rank3(base)
    assert rank == 17, ("shadow_rank",rank)
    assert all((2*base[2][i]+base[5][i]+base[11][i]+base[17][i])%3==0
               for i in range(729)), "explicit_null_relation"

    h = hashlib.sha256(b"".join(base)).hexdigest()
    assert h == "fb37bdb7463e493b32dbd5d43157621dfaab2b8f92381a062c25da7b9f4798a4"

    result = {
        "schema": "R762EQ_ALL_HORIZON_Q9_BRC_CERTIFICATE_V1",
        "input": "P=1+X+Z+XY+YZ+XYZ in Z[(Z/9)^3]",
        "named_branches": [x[0] for x in BRANCHES],
        "complete_horizons_checked": MAX_N+1,
        "max_n": MAX_N,
        "terminal_positions_per_horizon": 729,
        "modulus": "3^744",
        "max_content_exponent": MAX_N//3-2,
        "augmentation_checks": MAX_N+1,
        "q3_projection_checks": MAX_N+1,
        "nonzero_normalized_vector_checks": MAX_N+1,
        "period_first_n": 9,
        "period_difference": 18,
        "period_comparisons_for_n_from_27_to_2213": periodic_comparisons,
        "proof_recurrence_order": 729,
        "proof_shifted_zero_tests": 3*729,
        "period_base_rank_mod3": rank,
        "period_base_pivot_columns": pivots,
        "period_base_sha256": h,
        "period_base_supports": [sum(bool(x) for x in v) for v in base],
        "checked_linear_relation": "2*S_11+S_14+S_20+S_26=0 in F3[G]",
        "finite_check": "PASS",
        "all_horizon_inference":
            "monic degree729 annihilator of B=P^3/3 in Z_(3)[T]; see theorem",
        "review": "NOT_REVIEWED",
        "native_signed_event": "NOT_TESTED",
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
