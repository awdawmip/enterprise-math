#!/usr/bin/env python3
"""Exact zero-locus audit for six-branch BRC characters, no floating-point arithmetic."""
import hashlib
import json
from collections import Counter

def named_exponents(i, j, k, q):
    return (0, i % q, k % q, (i+j) % q, (j+k) % q, (i+j+k) % q)

def cyclotomic_zero(i, j, k, q):
    """P(zeta^i,zeta^j,zeta^k)=0 via Phi_{3^a} coefficient equality."""
    d = q // 3
    cnt = [0] * q
    for exponent in named_exponents(i, j, k, q):
        cnt[exponent] += 1
    return all(cnt[r] == cnt[r+d] == cnt[r+2*d] for r in range(d))

def line_hits(i, j, k, q):
    d = q // 3
    return tuple(
        family
        for t in (d, 2*d)
        for family, yes in (
            (f'A{t}', j == t and k == t),
            (f'B{t}', i == t and k == (q-t) % q),
            (f'C{t}', i == t and j == t),
            (f'D{t}', j == (t-i) % q and k == (t+i) % q),
        )
        if yes
    )

def verify(q):
    total = 0
    multiplicity = Counter()
    sha = hashlib.sha256()
    for i in range(q):
        for j in range(q):
            for k in range(q):
                zero = cyclotomic_zero(i, j, k, q)
                hits = line_hits(i, j, k, q)
                assert zero == bool(hits), (q, i, j, k, hits)
                if zero:
                    total += 1
                    multiplicity[len(hits)] += 1
                    sha.update(bytes((i, j, k)))
    assert total == 8*q - 12, (q, total)
    assert multiplicity[2] == 12 and multiplicity[1] == total-12
    assert set(multiplicity) == ({2} if q == 3 else {1, 2})
    return {'Q': q, 'characters_checked': q**3, 'exact_zeros': total,
            'nonzero_characters': q**3-total,
            'line_multiplicity': {str(k):v for k,v in sorted(multiplicity.items())},
            'zero_triples_sha256_byte_triplets_lex': sha.hexdigest()}

def exceptional_partition_check():
    forms = lambda i, j, k: (0, i, k, i+j, j+k, i+j+k)
    exceptional = [(0, 1, 4), (0, 1, 5), (0, 2, 3),
                   (0, 2, 5), (0, 3, 5), (0, 4, 5)]
    table = {}
    for A in exceptional:
        B = tuple(v for v in range(6) if v not in A)
        points = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    ex = tuple(v % 3 for v in forms(i, j, k))
                    if len({ex[t] for t in A}) == len({ex[t] for t in B}) == 3:
                        points.append([i,j,k])
        assert len(points) == 4, (A, points)
        assert all(line_hits(*p, 3) for p in points)
        table[''.join(map(str,A))] = points
    return table

def main():
    rows = [verify(q) for q in (3,9,27,81)]
    out = {'schema':'R762ED_EXACT_ZERO_LOCUS_EVIDENCE_V1',
           'model':'P=1+X+Z+XY+YZ+XYZ, Q=3^a',
           'arithmetic':'integer cyclotomic coefficient equality',
           'all_a_proof':'eight q-point lines; exactly twelve double overlaps; six exceptional partitions reduce to points on those lines',
           'finite_checks':rows,
           'exceptional_partitions_top_digits': exceptional_partition_check(),
           'independent_review':'NOT_REVIEWED'}
    print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
