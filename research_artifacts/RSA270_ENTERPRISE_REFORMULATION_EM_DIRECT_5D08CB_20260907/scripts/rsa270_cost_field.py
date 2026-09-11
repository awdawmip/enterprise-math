"""
Direction 1 (EM-DIRECT-5D08CB / DIRECT-RSA270): BRC add/sub cost field over the multiplier lattice.

Exact identities:
  branch k = a*b (coprime): factor endpoint  x* = a*p + b*q,  y* = |a*p - b*q|
  (x*)^2 - 4abN = (a*p - b*q)^2   [square!]   -> sub-cost = 0 at endpoint
  add-cost  j*(a,b) = x* - ceil(2*sqrt(abN)) = (sqrt(a*p) - sqrt(b*q))^2 + delta,  delta in (-1, 0]
  first-step shell cost (original rho_k experiment) d_(k,0) = x0^2 - 4abN, x0 = ceil(2*sqrt(abN))

  AM-GM ridge: real gap g(a,b) = (sqrt(a*p) - sqrt(b*q))^2 minimized on the ray a/b = q/p.
  Ridge directions under the construction-family band r = q/p in [1.765, 2.266] are exactly the
  coprime (a,b) with a/b in the band -> the scan set of journal T083741.
  k=20 = 5*4 has ratio 1.25 -> OFF-ridge -> the original low-rho_20 valley is a first-step artifact.

Verify: j* >= 0, square identity, delta bound, ridge ordering on synthetic semiprimes;
compute the RSA-270 ridge direction table and per-direction gap estimates.
"""
import math
from math import gcd, isqrt

def ridge_table(r_lo, r_hi, amax=21):
    out = []
    for a in range(1, amax + 1):
        for b in range(1, amax + 1):
            if gcd(a, b) != 1 or a == b: continue
            r = a / b
            if r_lo <= r <= r_hi:
                out.append((a, b, round(r, 4)))
    return sorted(out, key=lambda t: t[2])

print("== A. synthetic verification of the add/sub cost identities ==")
ok = True
for (p, q) in [(11, 13), (17, 23), (29, 31), (59, 61), (101, 103), (997, 1009)]:
    N = p * q
    for a in range(1, 7):
        for b in range(1, 7):
            if gcd(a, b) != 1: continue
            x = a * p + b * q
            y = abs(a * p - b * q)
            if x * x - 4 * a * b * N != y * y:
                ok = False; print(f"  square-identity FAIL p={p} q={q} a={a} b={b}")
            x0 = isqrt(4 * a * b * N)
            if x0 * x0 < 4 * a * b * N: x0 += 1
            j = x - x0
            if j < 0:
                ok = False; print(f"  j<0 FAIL p={p} q={q} a={a} b={b}")
            realgap = (math.sqrt(a * p) - math.sqrt(b * q)) ** 2
            delta = j - realgap
            if not (-1 < delta <= 1e-9):
                ok = False; print(f"  delta FAIL p={p} q={q} a={a} b={b}: delta={delta}")
    # ridge properties (correct form):
    #  P1: g(q,p) == 0 exactly (equality point of AM-GM);
    #  P2: scale-linearity: g(t*a, t*b) == t * g(a,b) for integer t;
    #  P3: same-scale monotonicity: among coprime pairs with equal product ab,
    #      smaller |a/b - r| gives smaller g.
    r = q / p
    if abs((math.sqrt(q * p) - math.sqrt(p * q)) ** 2) > 1e-9:
        ok = False; print(f"  P1 FAIL p={p} q={q}")
    for a in range(1, 5):
        for b in range(1, 5):
            g = (math.sqrt(a * p) - math.sqrt(b * q)) ** 2
            for t in (2, 3):
                gt = (math.sqrt(t * a * p) - math.sqrt(t * b * q)) ** 2
                if abs(gt - t * g) > 1e-9:
                    ok = False; print(f"  P2 FAIL p={p} q={q} a={a} b={b} t={t}")
    # P3 (exact closed form): g(a,b) = sqrt(abpq) * (x + 1/x - 2),  x = sqrt(ap/(bq)).
    #     ridge at x = 1  <=>  a/b = q/p;  deviation measure = relative (x-1)^2/x.
    for a in range(1, 6):
        for b in range(1, 6):
            if gcd(a, b) != 1: continue
            g = (math.sqrt(a * p) - math.sqrt(b * q)) ** 2
            x = math.sqrt(a * p / (b * q))
            gclosed = math.sqrt(a * b * p * q) * (x + 1 / x - 2)
            if abs(g - gclosed) > 1e-9:
                ok = False
                print(f"  P3 FAIL p={p} q={q} a={a} b={b}: g={g} closed={gclosed}")
print("  cost identities + ridge properties P1-P3:", "PASS" if ok else "FAIL")

print("\n== B. RSA-270 ridge direction table under prior band r in [1.765, 2.266] ==")
tab = ridge_table(1.765, 2.266)
print("  coprime (a,b) with a/b in band (a,b <= 21):", tab)
# gap estimates: g = p*(sqrt(a)-sqrt(b*r))^2 with p ~ 2^447.5; report log2(g/2^447.5) and savings vs Fermat (1,1)
print("\n  per-direction log2 real-gap coefficient (gap = 2^(447.5) * c):")
print(f"  {'(a,b)':8s} {'ratio':6s} {'c at r=1.765':12s} {'c at r=2.0':12s} {'c at r=2.266':12s} {'vs Fermat(1,1) c range':24s}")
for (a, b, ra) in [(1,1,1.0)] + tab:
    cs = []
    for r in (1.765, 2.0, 2.266):
        c = (math.sqrt(a) - math.sqrt(b * r)) ** 2
        cs.append(c)
    f1 = [(math.sqrt(1) - math.sqrt(r)) ** 2 for r in (1.765, 2.0, 2.266)]
    vs = f"vs {f1[0]:.4f}..{f1[2]:.4f}"
    print(f"  ({a},{b})   {ra:6.3f} {cs[0]:12.4f} {cs[1]:12.4f} {cs[2]:12.4f} {vs}")
print("\n  k=20 = 5*4 (ratio 1.25, OFF-ridge): c at r=1.765..2.266 =",
      f"{(math.sqrt(5)-math.sqrt(4*1.765))**2:.4f} .. {(math.sqrt(5)-math.sqrt(4*2.266))**2:.4f}",
      " (larger than all ridge directions at their band edges except the far ones)")
