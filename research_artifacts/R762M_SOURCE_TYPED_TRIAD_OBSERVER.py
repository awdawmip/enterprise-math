#!/usr/bin/env python3
"""Exact census: source-typed signed X6 triads and two-source N-BRC observer."""
from itertools import product, permutations
from collections import Counter, defaultdict
import json

AXES = range(6)
BITS = tuple(product((0, 1), repeat=3))
LAWS = tuple(product((0, 1), repeat=8))
INDEX = {s:i for i,s in enumerate(BITS)}

def law_value(a, s):
    return a[INDEX[s]]

def marginals(a):
    return tuple(tuple(
        a[INDEX[s]] + a[INDEX[tuple(1-x if j == missing else x for j,x in enumerate(s))]]
        for s in BITS if s[missing] == 0
    ) for missing in range(3))

def fixed_pair_count(a, missing, ports):
    """ports maps two distinct visible source slots to (axis, negative-bit)."""
    assert set(ports) == set(range(3)) - {missing}
    assert len({v[0] for v in ports.values()}) == 2
    ans = 0
    for hidden_axis in AXES:
        if hidden_axis in {v[0] for v in ports.values()}:
            continue
        for hidden_bit in (0, 1):
            signs = tuple(hidden_bit if j == missing else ports[j][1] for j in range(3))
            ans += law_value(a, signs)
    return ans

def main():
    typed_triads = [(assign, sign) for assign in permutations(AXES,3) for sign in BITS]
    assert len(typed_triads) == 960
    orbit_counts = Counter(s for _,s in typed_triads)
    assert set(orbit_counts.values()) == {120}
    for perm in permutations(AXES):
        for assign,sign in typed_triads:
            mapped = tuple(perm[i] for i in assign)
            assert len(set(mapped)) == 3 and sign in orbit_counts
    sigs = defaultdict(list)
    for a in LAWS:
        ms = marginals(a)
        sigs[ms].append(a)
        for missing in range(3):
            sources = [j for j in range(3) if j != missing]
            for assigned_axes in permutations(AXES,2):
                for visible_signs in product((0,1),repeat=2):
                    ports = {sources[j]:(assigned_axes[j],visible_signs[j]) for j in range(2)}
                    s0 = [0]*3
                    for j,bit in zip(sources,visible_signs):
                        s0[j]=bit
                    expected = 4*(law_value(a,tuple(s0)) +
                                  law_value(a,tuple(s0[:missing]+[1]+s0[missing+1:])))
                    assert fixed_pair_count(a,missing,ports) == expected
    sizes = Counter(map(len,sigs.values()))
    assert len(sigs) == 255 and sizes == {1:254,2:1}, sizes
    exceptional = [group for group in sigs.values() if len(group)==2][0]
    even = tuple(int(sum(x)%2 == 0) for x in BITS)
    odd = tuple(int(sum(x)%2 == 1) for x in BITS)
    assert set(exceptional) == {even,odd}
    assert marginals(even) == marginals(odd) == ((1,1,1,1),)*3
    assert all(e+o == 1 for e,o in zip(even,odd))
    output = {
      "schema":"R762M_SOURCE_TYPED_X6_TRIAD_MARGINAL_CENSUS_V1",
      "scientific_scope":"S6-invariant 3-source-labeled signed X6 candidate incidence, not native TRIADIC_CLOSURE_E",
      "signed_source_patterns":8,
      "axis_injective_assignments_per_pattern":120,
      "total_typed_candidates":len(typed_triads),
      "boolean_laws":len(LAWS),
      "two_source_marginal_signature_count":len(sigs),
      "signature_fiber_sizes":{str(k):v for k,v in sorted(sizes.items())},
      "exceptional_pair":{"even":list(even),"odd":list(odd),"marginal":[[1]*4 for _ in range(3)]},
      "accepted_candidates_per_exceptional_law":120*sum(even),
      "visible_pair_count":3*6*5*4,
      "branches_per_visible_pair_before_admission":8,
      "marginal_pair_count_for_parity_laws":4,
      "full_axis_permutations_checked":720,
      "observed_all_256_laws_all_360_visible_pairs":True
    }
    print(json.dumps(output,sort_keys=True,indent=2))

if __name__ == "__main__":
    main()
