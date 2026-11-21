"""Exact certificate verification; Python standard library only."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
G = (20, 20, 20, -100, 140, -100)
COEFF = (1, -4, 6, -4, 1)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def verify_record(r):
    n, a, b, s = r['n'], r['a'], r['b'], r['relative_sign']
    k = n-4
    U = tuple(G[(a+j)%6] for j in range(k))
    V = tuple(G[(b+j)%6] for j in range(k))
    h = tuple(map(F, r['primal'][:n]))
    alpha, beta, offset, radius2 = map(F, r['primal'][n:])
    y = tuple(map(F, r['dual']))
    assert len(h) == n and len(y) == k
    assert alpha >= 1 and beta >= 1 and radius2 >= 0
    assert max(map(abs, h)) <= radius2
    for j in range(k):
        assert dot(COEFF, h[j:j+5]) == alpha*U[j] - s*beta*V[j] + offset
    # Supporting-functional certificate valid for every feasible gain and noise.
    assert sum(y) == 0
    transpose_product = [F(0)]*n
    for j in range(k):
        for d, c in enumerate(COEFF):
            transpose_product[j+d] += c*y[j]
    assert sum(map(abs, transpose_product)) <= 1
    assert dot(y, U) >= 0
    assert -s*dot(y, V) >= 0
    lower = dot(y, U) - s*dot(y, V)
    assert lower == radius2 == F(r['distance'])
    assert F(r['radius']) == radius2/2

records = json.loads((HERE/'certificates.json').read_text())
records += json.loads((HERE/'saturation_certificates.json').read_text())
expected = {(n, a, b, s) for n in (7,8,9)
            for a,b in combinations(range(6),2) for s in (1,-1)}
seen = [(r['n'],r['a'],r['b'],r['relative_sign']) for r in records]
assert len(seen) == len(expected) == 90
assert set(seen) == expected
for r in records:
    verify_record(r)

summary = {}
for n in (7,8,9):
    for mode in ('positive','signed'):
        group = [r for r in records if r['n'] == n and
                 (mode == 'signed' or r['relative_sign'] == 1)]
        d = min(F(r['distance']) for r in group)
        summary[f'{n}_{mode}'] = str(d/2)
assert summary == {'7_positive':'3', '7_signed':'15/8',
                   '8_positive':'15/4', '8_signed':'3',
                   '9_positive':'15/4', '9_signed':'10/3'}

# Finite period identities are certificates for arbitrarily long windows.
def fourth(seq, j):
    return sum(c*seq[(j+d)%len(seq)] for d,c in enumerate(COEFF))

positive_period = (F(15,2), F(-15,2))
signed_period = (F(20,3), F(-20,3), F(20,3))
for j in range(6):
    assert fourth(positive_period,j) == G[j]-G[(j+3)%6]
    assert fourth(signed_period,j) == G[j]+G[(j+1)%6]

report = {
    'status':'PASS',
    'certificate_count':90,
    'exact_arithmetic':'fractions.Fraction',
    'solver_required':False,
    'finite_domain':'all 15 unordered phase pairs, both relative signs, n=7,8,9',
    'radii_in_units_g':summary,
    'positive_all_n_ge_8':'15/4',
    'signed_all_n_ge_9':'10/3',
    'infinite_extension':'prefix monotonicity plus exact period-2 and period-3 collision witnesses',
    'scientific_status':'AUTHOR_PROVED_EXACT_CERTIFICATE_CHECKED_UNREVIEWED'
}
(HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
