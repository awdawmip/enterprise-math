"""
Round 8 (EM-DIRECT-5D08CB / DIRECT-RSA270): combined sieve x cost optimization —
the complete per-direction strategy table for the prior band, and the true optimum.
Budget model: add-steps ~ 2^447.5 * c_max * (|x* residues mod 72| / 72).
"""
import math
from math import gcd

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

# admissible (p,q) mod 72 (forced lattice S = 16 mod 72, prior)
adm = []
for p in range(72):
    if p % 6 != 5: continue
    for q in range(72):
        if q % 6 != 5: continue
        if (p * q) % 72 == N % 72 and (p + q) % 72 == 16:
            adm.append((p, q))

def c_of(a, b, r):
    return (math.sqrt(a) - math.sqrt(b * r)) ** 2

r_lo, r_hi = 1.765, 2.266
R = [r_lo, 1.8, 1.9, 2.0, 2.1, 2.2, r_hi]

print("combined strategy table (band directions, a,b <= 21, coprime):")
print(f"  {'(a,b)':7s} {'ratio':6s} {'c_max':8s} {'|res|':5s} {'sieve':6s} {'budget bits':11s}")
best = None
rows = []
for a in range(1, 22):
    for b in range(1, 22):
        if gcd(a, b) != 1 or a == b: continue
        if not (r_lo <= a / b <= r_hi): continue
        cmax = max(c_of(a, b, r) for r in R)
        xres = {(a * p0 + b * q0) % 72 for p0, q0 in adm}
        nres = len(xres)
        bits = 447.5 + math.log2(cmax) + math.log2(nres / 72)
        rows.append((bits, a, b, a/b, cmax, nres))
rows.sort()
for bits, a, b, ratio, cmax, nres in rows:
    print(f"  ({a:2d},{b:2d})  {ratio:6.3f} {cmax:8.4f} {nres:5d} {nres:2d}/72 {bits:11.2f}")
    if best is None or bits < best[0]:
        best = (bits, a, b)
print(f"\n  TRUE OPTIMUM: direction ({best[1]},{best[2]}) with combined budget ~ 2^{best[0]:.2f} add-steps")
print("  (compare un-sieved minimax (2,1): 2^440.6; the sieve changes the ranking)")
print("  conclusion: combined sieve+cost optimum still ~2^43x-scale -> infeasible; cost-field line closed.")
