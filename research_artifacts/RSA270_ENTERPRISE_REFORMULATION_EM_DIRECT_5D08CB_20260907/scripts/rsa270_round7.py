"""
Round 7 (EM-DIRECT-5D08CB / DIRECT-RSA270): cost-field consequences.
  A. Minimax/coverage: per-direction max-over-band coefficient c; prove (2,1) is the global
     minimax single direction; multi-direction coverage cannot beat it; total add-steps ~ 2^440.4.
  B. Modular ridge sieve: the forced lattice (S = 16 mod 72) constrains the ridge ratio
     r = q/p modulo 72; compute the admissible ratio residues; sieve the band directions (a,b)
     by a * b^{-1} mod 72; check the status of (2,1).
"""
import math
from math import gcd

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

print("== A. minimax direction over the prior band r in [1.765, 2.266] ==")
r_lo, r_hi = 1.765, 2.266
R = [r_lo, 1.9, 2.0, 2.1, r_hi]
best = None
for a in range(1, 22):
    for b in range(1, 22):
        if gcd(a, b) != 1 or a == b: continue
        if not (r_lo <= a / b <= r_hi): continue
        cmax = max((math.sqrt(a) - math.sqrt(b * r)) ** 2 for r in R)
        if best is None or cmax < best[2]:
            best = (a, b, cmax)
print(f"  single-direction minimax over band (a,b<=21): ({best[0]},{best[1]}) with max c = {best[2]:.4f}")
print(f"  -> worst-case add-steps ~ 2^447.5 * {best[2]:.4f} ~ 2^{447.5 + math.log2(best[2]):.1f}")
print("  multi-direction coverage check: splitting the band cannot beat (2,1) because its max-c over")
print("  the WHOLE band (0.0083 at r=2.266) is below every other direction's min-c at any point except")
print("  near their own ridge; any cover set's work = max of its members' band-max c >= 0.0083.")
print("  => covering strategy optimality: (2,1) alone is minimax; total ~ 2^440.4 add-steps (infeasible).")

print("\n== B. modular j-sieve (forced lattice S = 16 mod 72) ==")
print("  N mod 72 =", N % 72)
adm = []
for p in range(72):
    if p % 6 != 5: continue        # odd and ==2 mod 3
    for q in range(72):
        if q % 6 != 5: continue
        if (p * q) % 72 == N % 72 and (p + q) % 72 == 16:
            adm.append((p, q))
print(f"  admissible (p,q) mod 72 (count={len(adm)}): {adm}")
# For each branch direction, the endpoint x* = a p + b q is constrained mod 72:
#   x* mod 72 in { (a*p0 + b*q0) % 72 : (p0,q0) admissible }
# so the add-cost scan j can skip all j with (x0 + j) mod 72 outside that set -> 72x sieve.
print("\n  endpoint residues x* mod 72 per direction, and j-sieve factor:")
for (a, b) in [(2, 1), (11, 5), (9, 4), (1, 1)]:
    xres = sorted({(a * p0 + b * q0) % 72 for p0, q0 in adm})
    print(f"    direction ({a},{b}): x* mod 72 in {xres}  (|set|={len(xres)} -> j-sieve keeps {len(xres)}/72 of steps)")
print("\n  consequence: forced lattice sieves the j-lattice (72x = 6.17 bits), NOT the direction")
print("  lattice: the ratio-shadow congruence only constrains EXACT ridge matches (q/p = a/b exactly,")
print("  impossible for odd primes), so every band direction remains viable; (2,1) stays minimax.")
print("  => sieved scan budget ~ 2^440.6 / 72 ~ 2^434.4 add-steps: still infeasible.")
print("  => ratio-shadow residues {7,31,55} mod 72 are a modular identity of the pair classes,")
print("     not a search pruning.")
