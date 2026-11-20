"""Unit176 independent exact integer/rational A3->A4 support-fiber check.
Frozen comparison: enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3.
No native six-axis physical interpretation and no R063 benchmark run.
"""
from fractions import Fraction
from itertools import product
import json

U = (0, 1)
V = (2, 3)
counts = {"states": 0, "radius_cases": 0, "coarse_true_fine_false": 0, "coarse_true": 0, "fine_true": 0}

def verify_sizes_totals(m, c, radius):
    z = tuple(tuple(m[j]*c[i]-m[i]*c[j] for j in range(4)) for i in range(4))
    mu = Fraction(sum(c[i] for i in U), sum(m[i] for i in U)) - Fraction(sum(c[j] for j in V), sum(m[j] for j in V))
    delta = [Fraction(z[i][j], m[i]*m[j]) for i in U for j in V]
    alpha = max(x-mu for x in delta)
    beta = max(mu-x for x in delta)
    weighted_mu = sum((Fraction(m[i]*m[j], sum(m[k] for k in U)*sum(m[k] for k in V)) * Fraction(z[i][j], m[i]*m[j])) for i in U for j in V)
    if mu != weighted_mu or alpha < 0 or beta < 0:
        raise AssertionError("weighted mean or centered envelope mismatch")
    fine_by_producer = all(abs(z[i][j]) <= radius*m[i]*m[j] for i in U for j in V)
    coarse_by_producer = abs(sum(z[i][j] for i in U for j in V)) <= radius*sum(m[i] for i in U)*sum(m[j] for j in V)
    fine_by_envelope = (mu + alpha <= radius and mu - beta >= -radius)
    if fine_by_producer != fine_by_envelope or coarse_by_producer != (abs(mu) <= radius) or (fine_by_producer and not coarse_by_producer):
        raise AssertionError(f"support mismatch {m=} {c=} {radius=}")
    return coarse_by_producer, fine_by_producer

for sizes in product((1,2,3), repeat=4):
    for totals in product(range(-2,3), repeat=4):
        counts["states"] += 1
        for r in range(4):
            coarse, fine = verify_sizes_totals(sizes, totals, r)
            counts["radius_cases"] += 1
            counts["coarse_true"] += int(coarse)
            counts["fine_true"] += int(fine)
            counts["coarse_true_fine_false"] += int(coarse and not fine)

witnesses = []
for r in range(12):
    t = r + 1
    m = (1,1,1,1)
    c = (t, -t, 0, 0)
    coarse, fine = verify_sizes_totals(m, c, r)
    if not coarse or fine:
        raise AssertionError("unbounded cancellation witness failed")
    z_cross = [[m[j]*c[i]-m[i]*c[j] for j in V] for i in U]
    witnesses.append({"r":r,"t":t,"coarse_totals":[0,0],"cross_relations":z_cross,"coarse":coarse,"fine":fine})

out = {"schema":"X6_UNIT176_EXACT_CHECK_V1","source_commit":"fd2bcff10ca6e147348b6c1236027fc0d2877df3","arithmetic":"Python Fraction exact, integer only","capacities":[1,2,3],"totals":[-2,-1,0,1,2],"radii":[0,1,2,3],"blocks":{"U":[0,1],"V":[2,3]},"counts":counts,"witnesses":witnesses,"violations":0,"native_R063_executed":False,"production_module_imported":False,"theorem_scope":"typed A3 weighted relation field and A4 support bridge; independent oracle cross-check"}
print(json.dumps(out, sort_keys=True, ensure_ascii=False, indent=2))
