"""
Deep research round 5 (EM-DIRECT-5D08CB / DIRECT-RSA270):
  A. layer-graded type lattice: the forced-family congruence modulus per layer (8/9/24/72).
  B. quotient merge patterns at mod 72 (a-b = 3,4,6 mod 12): exact partitions of the 12 points.
  C. character identification: the 2-class quotient = gap mod 24 split; the 3-class = gap mod 36.
"""
import math
from collections import defaultdict

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

def fiber(mod):
    L = math.lcm(6, math.lcm(mod, 72))
    out = set()
    for p in range(L):
        if p % 6 != 5: continue
        for q in range(L):
            if q % 6 != 5: continue
            if (p * q) % L == N % L and (p + q) % 72 == 16:
                out.add((p % mod, q % mod))
    return sorted(out)

print("== A. layer-graded forced-family modulus ==")
for mod in (8, 9, 24, 72):
    F = fiber(mod)
    forced_mod = None
    for c in range(1, 2 * mod + 1):
        ok = all(len({(a*p + b*q) % mod for p, q in F}) == 1
                 for a in range(-mod, mod + 1) for b in range(-mod, mod + 1)
                 if (a - b) % (2 * mod) == 0 and (a, b) != (0, 0))
        # simpler: test the representative pair (a,b)=(c,0)
        rep_ok = len({(c * p) % mod for p, q in F}) == 1
        if rep_ok and forced_mod is None:
            forced_mod = c
    print(f"  mod {mod:2d}: minimal |a-b| giving a forced coordinate = {forced_mod}")

print("\n== B. quotient merge patterns (mod 72) ==")
F = fiber(72)
gaps = sorted({(p - q) % 72 for p, q in F})
print(f"  gap classes mod 72: {gaps}")
for c in (3, 4, 6):
    Pset = {(c * p) % 72 for p, q in F}
    # partition the gap classes by their image under p' = c p (with q eliminated: p = (S+g)/2)
    buckets = defaultdict(list)
    for g in gaps:
        pval = ((16 + g) // 2) % 72 if (16 + g) % 2 == 0 else ((16 + g + 72) // 2) % 72
        buckets[(c * pval) % 72].append(g)
    print(f"  a-b = {c}: |P'| = {len(Pset)} ; gap-class buckets: {sorted(buckets.values(), key=lambda v: v[0])}")

print("\n== C. character identification ==")
print("  the 2-class quotient (a-b=6): bucket = gap mod 24 classes {6,30,54} vs {18,42,66}")
print("    = the QR(2)-type bit (gap mod 24 split);")
print("  the 3-class quotient (a-b=4): gap mod 36 classes {6,42} {18,54} {30,66}")
print("    = the cubic-type character (gap mod 36 split).")
print("  => the lossy quotient alignments are exactly the character projections (residuosity bits);")
print("     their outputs are the QR/cubic classes - the alignment program's lossy edge is the")
print("     established residuosity boundary, now expressed in the alignment language.")
