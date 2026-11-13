#!/usr/bin/env python3
"""Exact Fraction checks for R749SML public routing and Walsh-union rank.
All operations are finite signed-source observer algebra, not native V29/V39 updates.
"""
from fractions import Fraction as Q
from itertools import product
import json


def parity(v, state):
    return -1 if ((v & state).bit_count() & 1) else 1


def gf2_span(vectors):
    span = {0}
    for v in vectors:
        span |= {x ^ v for x in tuple(span)}
    return span


def rowrank(rows):
    A = [list(map(Q, r)) for r in rows]
    if not A:
        return 0
    h, w = len(A), len(A[0])
    rank = 0
    for j in range(w):
        pivot = next((k for k in range(rank, h) if A[k][j]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        scale = A[rank][j]
        A[rank] = [u / scale for u in A[rank]]
        for i in range(h):
            if i != rank and A[i][j]:
                c = A[i][j]
                A[i] = [a - c*b for a, b in zip(A[i], A[rank])]
        rank += 1
        if rank == h:
            break
    return rank


def channel_rows(d, branches):
    """branches: iterable (route weight, [(parity_mask, bias), ...])."""
    states = range(1 << d)
    rows = []
    for weight, queries in branches:
        assert weight > 0
        for observations in product((-1, 1), repeat=len(queries)):
            row = []
            for x in states:
                p = weight
                for y, (mask, a) in zip(observations, queries):
                    p *= (1 + a*y*parity(mask, x)) / 2
                row.append(p)
            rows.append(row)
    return rows


def predicted_rank(branches):
    union = set()
    for _, queries in branches:
        union |= gf2_span([v for v, a in queries if a != 0])
    return len(union), sorted(union)


def run():
    tests = []
    def check(name, d, branches, expected=None):
        assert sum((w for w, _ in branches), Q(0)) == 1
        rows = channel_rows(d, branches)
        actual = rowrank(rows)
        predicted, vectors = predicted_rank(branches)
        assert actual == predicted, (name, actual, predicted)
        if expected is not None:
            assert actual == expected, (name, actual, expected)
        assert all(sum((r[x] for r in rows), Q(0)) == 1 for x in range(1 << d))
        tests.append({"case":name, "rank":actual, "minimum_affine_coordinates":actual-1,
                      "walsh_masks":vectors, "rows":len(rows), "source_states":1<<d})

    check("R749SMG-rank-three-public-routing", 3,
          [(Q(1,2), [(1,Q(1,2))]), (Q(1,2), [(2,Q(1,2))])], 3)
    check("overlapping-two-bit-branches", 3,
          [(Q(1,3),[(1,Q(1,2)),(2,Q(1,3))]),
           (Q(2,3),[(2,Q(3,5)),(4,Q(-1,4))])], 6)
    check("one-erased-branch-parity", 3,
          [(Q(1,3),[(1,Q(1,2)),(2,Q(0))]),
           (Q(2,3),[(2,Q(3,5)),(4,Q(-1,4))])], 5)
    check("three-public-routes", 3,
          [(Q(1,6),[(1,Q(1,2))]),(Q(1,3),[(2,Q(1,2))]),
           (Q(1,2),[(4,Q(1,2))])],4)
    check("all-branch-signals-erased",3,
          [(Q(1,2),[(1,Q(0))]),(Q(1,2),[(2,Q(0))])],1)

    # Entire finite family of two one-query branches: all three nonzero coordinate masks;
    # three bias cases for each, multiple routing weights.
    parameters=(Q(0),Q(1,2),Q(-1,3))
    idx=0
    for m1,m2,a1,a2,w in product((1,2,4), (1,2,4),parameters,parameters,(Q(1,3),Q(1,2),Q(2,3))):
        check("single-parity-grid-%03d"%idx, 3,
              [(w,[(m1,a1)]),(1-w,[(m2,a2)])])
        idx+=1

    # If the branch label is omitted, the two public-route observations are mixed.
    # For two equiprobable routes querying different source bits, the 2-output observer
    # has rank 2, whereas the public-route observer has rank 3.
    pub=channel_rows(2,[(Q(1,2),[(1,Q(1,2))]),(Q(1,2),[(2,Q(1,2))])])
    hidden=[ [pub[0][i]+pub[2][i] for i in range(4)],
             [pub[1][i]+pub[3][i] for i in range(4)] ]
    assert rowrank(pub)==3 and rowrank(hidden)==2

    # Strictly positive priors with equal one-bit marginals and opposite joint mode.
    # x=00 and 11 are positive-correlation, 01 and 10 negative-correlation.
    eta = Q(1,2)
    pos = [eta/4 + (1-eta)*(Q(1,2) if x in (0,3) else 0) for x in range(4)]
    neg = [eta/4 + (1-eta)*(Q(1,2) if x in (1,2) else 0) for x in range(4)]
    assert all(u > 0 for u in pos+neg)
    assert [sum(row[x]*pos[x] for x in range(4)) for row in pub] == \
           [sum(row[x]*neg[x] for x in range(4)) for row in pub]
    joint_rows = channel_rows(2, [(Q(1),[(1,Q(1,2)),(2,Q(1,2))])])
    plus_out=[sum(row[x]*pos[x] for x in range(4)) for row in joint_rows]
    minus_out=[sum(row[x]*neg[x] for x in range(4)) for row in joint_rows]
    witness_tv = sum(abs(u-v) for u,v in zip(plus_out,minus_out))/2
    assert rowrank(joint_rows)==4 and witness_tv==Q(1,8)
    result={"schema":"ENTERPRISE_MATH_R749SML_CHECK_V1",
            "status":"PASS", "model":"public source-independent routing over signed-provenance Walsh parities",
            "frozen_scientific_pin":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "method":"exact Fraction likelihood matrix and Gauss-Jordan rational rank; predicted union of GF(2) Walsh subspaces",
            "validated_cases":len(tests), "grid_cases":idx,
            "hidden_route_rank":rowrank(hidden),"public_route_rank":rowrank(pub),"expanded_joint_query_rank":rowrank(joint_rows),
            "strict_positive_prior_joint_query_tv":str(witness_tv),
            "featured":tests[:5],"limits":"finite grid regression; arbitrary finite-family result relies on algebraic proof"}
    with open("R749SML_PUBLIC_ROUTING_WALSH_UNION_RESULTS.json","w") as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
        f.write("\n")
    print("PASS",len(tests),"exact public-routing cases; hidden-route rank",rowrank(hidden),"public rank",rowrank(pub))


if __name__=="__main__":
    run()
