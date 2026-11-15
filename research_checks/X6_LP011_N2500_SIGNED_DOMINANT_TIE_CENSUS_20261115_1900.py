#!/usr/bin/env python3
"""Exact N=2500 signed-X6 argmax-tie census; pure stdlib, exact integers.

Author-side supplementary certificate; not the original R063 native replay.
Use --prior-result PATH to check all support/path subtotals against the
independently saved full-X6 census, and --out PATH to write JSON.
"""
import argparse
import collections
import hashlib
import json
import math
from functools import lru_cache

N, D = 2500, 6
FAC = [math.factorial(i) for i in range(124)]
EXPECTED_ENDPOINTS = 102539052
EXPECTED_PATHS = int('46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372')
counts = collections.Counter()
paths = collections.Counter()
by_support = collections.Counter()
by_support_path = collections.Counter()
by_max = collections.Counter()
by_length = collections.Counter()
partitions = 0
examples = {}


def visit(prefix, remaining, ceiling):
    """Enumerate the 3356 nonincreasing absolute-coordinate square partitions."""
    global partitions
    t = len(prefix)
    if t == D:
        if remaining:
            return
        partitions += 1
        r = tuple(prefix)
        cc = collections.Counter(r)
        perm = FAC[D] // math.prod(FAC[v] for v in cc.values())
        support = sum(a != 0 for a in r)
        m = cc[r[0]]
        maximum = r[0]
        multiplicity = perm * (1 << support)
        length = sum(r)
        weight = FAC[length] // math.prod(FAC[a] for a in r)
        counts[m] += multiplicity
        paths[m] += multiplicity * weight
        by_support[support] += multiplicity
        by_support_path[support] += multiplicity * weight
        by_max[(maximum, m)] += multiplicity
        by_length[length] += multiplicity * weight
        examples.setdefault(str(m), list(r))
        return
    if t == D - 1:
        a = math.isqrt(remaining)
        if a <= ceiling and a*a == remaining:
            visit(prefix + [a], 0, a)
        return
    for a in range(min(ceiling, math.isqrt(remaining)), -1, -1):
        residual = remaining - a*a
        if residual <= (D-t-1)*a*a:
            visit(prefix + [a], residual, a)


@lru_cache(maxsize=None)
def coeff(max_allowed, axes, q):
    """Ordered endpoint coefficient of (1+2 sum_{a=1}^M x^(a*a))^axes."""
    if axes == 0:
        return int(q == 0)
    ans = coeff(max_allowed, axes-1, q)
    for a in range(1, min(max_allowed, math.isqrt(q))+1):
        ans += 2 * coeff(max_allowed, axes-1, q-a*a)
    return ans


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prior-result', help='Saved full signed X6 result JSON')
    ap.add_argument('--out', help='JSON output file')
    args = ap.parse_args()
    visit([], N, math.isqrt(N))
    independent = collections.Counter()
    for maximum in range(1, 51):
        for m in range(1, D+1):
            remaining = N - m*maximum*maximum
            if remaining < 0:
                break
            observed = math.comb(D, m)*(2**m)*coeff(maximum-1, D-m, remaining)
            assert observed == by_max[(maximum, m)], (maximum, m)
            independent[m] += observed
    assert independent == counts
    assert partitions == 3356
    assert sum(counts.values()) == EXPECTED_ENDPOINTS
    assert sum(paths.values()) == EXPECTED_PATHS
    assert max(by_length) == 122
    assert sum(k*v for k,v in counts.items()) % 12 == 0
    assert sum(k*v for k,v in paths.items()) % 12 == 0
    prior_status = 'NOT_SUPPLIED'
    if args.prior_result:
        with open(args.prior_result, encoding='utf-8') as f:
            previous = json.load(f)
        assert sum(counts.values()) == previous['total_endpoints']
        assert sum(paths.values()) == int(previous['total_shortest_paths'])
        for k, v in previous['by_support'].items():
            assert by_support[int(k)] == v['endpoints']
            assert by_support_path[int(k)] == int(v['shortest_paths'])
        prior_status = 'ALL_SUPPORT_AND_PATH_SUBTOTALS_PASS'
    out = {
        'schema': 'X6_LP011_N2500_NATIVE_DOMINANT_TIE_CENSUS_V1',
        'radius_squared': N, 'axes': D,
        'sorted_absolute_partitions': partitions,
        'endpoints_by_tie_multiplicity': {str(k): counts[k] for k in sorted(counts)},
        'free_paths_by_tie_multiplicity': {str(k): str(paths[k]) for k in sorted(paths)},
        'total_endpoints': sum(counts.values()),
        'total_free_paths': str(sum(paths.values())),
        'nontotal_unique_endpoints': sum(v for k,v in counts.items() if k>1),
        'nontotal_unique_free_paths': str(sum(v for k,v in paths.items() if k>1)),
        'dominant_axis_membership_count': sum(k*v for k,v in counts.items()),
        'dominant_axis_membership_paths': str(sum(k*v for k,v in paths.items())),
        'duplicated_membership_count': sum((k-1)*v for k,v in counts.items()),
        'duplicated_membership_paths': str(sum((k-1)*v for k,v in paths.items())),
        'each_of_12_signed_axis_memberships': sum(k*v for k,v in counts.items())//12,
        'each_of_12_signed_axis_path_memberships': str(sum(k*v for k,v in paths.items())//12),
        'one_sorted_example_per_m': examples,
        'independent_endpoint_polynomial': 'ALL M,m EXACT PASS',
        'prior_full_x6_comparison': prior_status,
        'observer': 'argmax_i |z_i|, retain signed native axis for each tied maximum',
        'evidence_status': 'AUTHOR_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED',
    }
    payload = json.dumps(out, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    out['payload_sha256'] = hashlib.sha256(payload).hexdigest()
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, sort_keys=True, indent=2)
    print('PASS_X6_LP011_N2500_SIGNED_DOMINANCE_TIES')
    print(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
