#!/usr/bin/env python3
"""Exact integer certificate for k=7, slack=2 and named Set_0(0/1).
Frozen input 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Requires the inherited genuine source-labelled common-library theorem.
No optimizer, floats, Python dependencies or solver trust needed.
"""
from functools import lru_cache
import json

K, SLACK, N = 7, 2, 128
CENTERS = (45,46,47,55,61,85,90,91,94,95,109,118,119,122,123,126,127)
BELIEF_HEX = (
  "00000000000000000000333300003333",
  "00000000000000000000440400004000",
  "0000000000000000000088080000c000",
  "000000000000000000cc00c000c000c0",
  "00000000000000003333300033003000",
  "00000000003300330000000000330000",
  "00000000050405040000000004040404",
  "000000000e080a080000000008080808",
  "00000000540040400000000040000000",
  "00000000a80080800000000080000000",
  "00003333000030000000300000003000",
  "00510044004000000000000000000000",
  "00e20088008000000000000000000000",
  "05040400000000000400000000000000",
  "0a080800000000000800000000000000",
  "54004000400000004000000000000000",
  "a8008000800000008000000000000000"
)
TRANSITIONS = ((0,0),(1,2),(1,2),(3,3),(4,4),(5,5),(6,7),(6,7),(8,9),(8,9),(10,10),(11,12),(11,12),(13,14),(13,14),(15,16),(15,16))

def q(u):
    return sum(((u >> i) & 1) * ((u >> ((i + 1) % K)) & 1) for i in range(K))

def members(m):
    while m:
        bit = m & -m
        yield bit.bit_length() - 1
        m -= bit

def static_cover(r):
    return sum(1 << u for u in range(N)
               if (u & ~r) == 0 and q(r) - q(u) <= SLACK)

def verify_upper():
    beliefs = [int(x, 16) for x in BELIEF_HEX]
    assert len(CENTERS) == len(beliefs) == len(TRANSITIONS) == 17
    assert len(set(CENTERS)) == 17
    total = 0
    source_checks = transition_checks = 0
    for i, (r, B) in enumerate(zip(CENTERS, beliefs)):
        assert B and B & ~static_cover(r) == 0
        for u in members(B):
            assert (u & ~r) == 0 and 0 <= q(r) - q(u) <= SLACK
            source_checks += 1
        total |= B
        for bit in (0, 1):
            dest = TRANSITIONS[i][bit]
            assert 0 <= dest < 17
            image = 0
            for u in members(B):
                image |= 1 << ((u & ~1) | bit)
                transition_checks += 1
            assert image & ~beliefs[dest] == 0, (i, bit, dest)
    assert total == (1 << N) - 1
    return {"centers":list(CENTERS), "belief_hex":list(BELIEF_HEX),
            "transitions":[list(v) for v in TRANSITIONS],
            "raw_mask_coverage":N,
            "source_membership_checks":source_checks,
            "reset_image_membership_checks":transition_checks}

def certify_static_lower():
    covers = [static_cover(r) for r in range(N)]
    keep = [r for r in range(N) if not any(
        r != s and covers[r] & ~covers[s] == 0
        and (covers[r] != covers[s] or s > r)
        for s in range(N))]
    sets = [covers[r] for r in keep]
    by_u = [[j for j,c in enumerate(sets) if (c >> u) & 1]
            for u in range(N)]
    assert all(by_u)
    calls = 0
    @lru_cache(maxsize=None)
    def possible(rem, steps):
        nonlocal calls
        calls += 1
        if rem == 0: return True
        if steps == 0: return False
        max_cover = max((c & rem).bit_count() for c in sets)
        if rem.bit_count() > steps * max_cover: return False
        pivot = min(members(rem), key=lambda u:(len(by_u[u]), -q(u)))
        choices = sorted(by_u[pivot],
                         key=lambda j:(sets[j] & rem).bit_count(),
                         reverse=True)
        for j in choices:
            if possible(rem & ~sets[j], steps - 1):
                return True
        return False
    assert possible((1 << N) - 1, 16) is False
    info = possible.cache_info()
    return {"all_source_centers":N,
            "undominated_centers":len(keep),
            "excluded_cover_size_at_most":16,
            "exact_dfs_visited_states":calls,
            "exact_dfs_cache":{"hits":info.hits,"misses":info.misses},
            "arithmetic":"exact Python integers",
            "pruning":"exact dominance and remaining-cardinality bound",
            "branching":"every source center covering chosen uncovered mask"}

def main():
    upper = verify_upper()
    lower = certify_static_lower()
    result = {
        "status":"PASS_R5_K7_SINGLE_NAMED_SET_EXACT_17",
        "frozen_scientific_input":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
        "model":{"k":7,"slack":2,"control_set":[0],
                 "q":"cyclic sum of adjacent 1-bit products",
                 "source_library_size":"35+q(r)"},
        "theorem":{"static_minimum":17,"dynamic_minimum":17},
        "upper_certificate":upper,"lower_certificate":lower,
        "scope":"auxiliary genuine source-labelled cycle-of-triangles repair",
        "review":"NOT_REVIEWED"}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == "__main__":
    main()
