"""Exact integer source-cover checks for the R5 cyclic triangle indexed-center model.
Run: python VERIFY_R5_SLACK_DYNAMIC.py
No external dependencies. Optional MILP spectrum is a separate file.
"""
from itertools import combinations
import json


def q(u, k):
    return sum(((u >> i) & 1) * ((u >> ((i + 1) % k)) & 1) for i in range(k))


def edges(k):
    e = []
    for i in range(k):
        j = (i + 1) % k
        e.extend(((i, j), (i, k + i), (j, k + i)))
    return e


def canonical(k, unavailable):
    e = edges(k)
    L = set()
    for i in range(k):
        if not ((unavailable >> i) & 1):
            L.add(("H0", i))
            L.add(("H4", i))
    for t, (a, b) in enumerate(e):
        L.add(("E1", t))
        if not any(v < k and not ((unavailable >> v) & 1) for v in (a, b)):
            L.add(("E0", t))
    assert len(L) == 5 * k + q(unavailable, k)
    return L


def source_ok(L, u, k):
    for i in range(k):
        if (u >> i) & 1 and (("H0", i) in L or ("H4", i) in L):
            return False
    for t, (a, b) in enumerate(edges(k)):
        if ("E1", t) not in L:
            return False
        if ("E0", t) not in L and not any(
            v < k and ("H0", v) in L and ("H4", v) in L for v in (a, b)
        ):
            return False
    return True


def center_covers(k, s, v, u):
    return (u & v) == u and q(v, k) - q(u, k) <= s


def test_near_max():
    checks = 0
    for k in range(3, 13):
        allones = (1 << k) - 1
        for r in (1, 2):
            s = k - r
            centers = [allones] + [allones ^ (1 << i) for i in range(r + 1)]
            libraries = {v: canonical(k, v) for v in centers}
            for u in range(1 << k):
                witnesses = [v for v in centers if center_covers(k, s, v, u)]
                assert witnesses, (k, s, u)
                for v in witnesses:
                    assert len(libraries[v]) <= 5 * k + q(u, k) + s
                    assert source_ok(libraries[v], u, k)
                    checks += 1
    return checks


def delta(B, i, v, n):
    out = 0
    for u in range(n):
        if (B >> u) & 1:
            w = (u & ~(1 << i)) | (v << i)
            out |= 1 << w
    return out


def dynamic_three_state_no_go():
    k, s = 3, 2
    n, complete = 1 << k, (1 << (1 << k)) - 1
    candidates = []
    for B in range(1, complete + 1):
        members = [u for u in range(n) if (B >> u) & 1]
        aggregate = 0
        for u in members:
            aggregate |= u
        if q(aggregate, k) - min(q(u, k) for u in members) <= s:
            candidates.append(B)
    count_covered_triples = count_closed_triples = 0
    for Bs in combinations(candidates, 3):
        if Bs[0] | Bs[1] | Bs[2] != complete:
            continue
        count_covered_triples += 1
        if all(any(delta(B, i, v, n) & ~C == 0 for C in Bs)
               for B in Bs for i in range(k) for v in (0, 1)):
            count_closed_triples += 1
    assert count_closed_triples == 0
    states = []
    for bit0 in (0, 1):
        for bit2 in (0, 1):
            u0 = bit0 | (bit2 << 2)
            states.append((1 << u0) | (1 << (u0 | 2)))
    assert len(states) == 4
    assert states[0] | states[1] | states[2] | states[3] == complete
    for B in states:
        members = [u for u in range(n) if (B >> u) & 1]
        v = members[0] | members[1]
        library = canonical(k, v)
        for u in members:
            assert source_ok(library, u, k)
            assert len(library) <= 5 * k + q(u, k) + s
        for i in range(k):
            for val in (0, 1):
                assert any(delta(B, i, val, n) & ~C == 0 for C in states)
    return {"compatible_beliefs": len(candidates),
            "covered_three_state_families_checked": count_covered_triples,
            "closed_three_state_families": count_closed_triples,
            "four_state_witness_beliefs": states}


def main():
    result = {"status": "PASS_R5_SLACK_SOURCE_DYNAMIC",
              "frozen_pin": "435e77af0d180eac32bd1f9c4c464bc4010b7551",
              "arithmetic": "exact integers and finite bitset enumeration",
              "special_static_source_checks": test_near_max(),
              "k_range_static": [3, 12],
              "k3_slack2_full_set": dynamic_three_state_no_go(),
              "universal_proofs": "see SLACK_SOURCE_COVER_AND_DYNAMIC_BELIEF_THEOREMS.md",
              "independent_review": "NOT_REVIEWED"}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
