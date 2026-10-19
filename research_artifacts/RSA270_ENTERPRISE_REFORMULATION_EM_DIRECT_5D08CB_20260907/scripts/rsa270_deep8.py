"""
Deep research round 8 (EM-DIRECT-5D08CB / DIRECT-RSA270):
general vertex-side law and the forced-sum certificate family.

General side law (branch l):  x = l p + q,  y = |l p - q|
  l p >= q  <=>  x + y = 2 l p  <=>  x + y = 0 (mod 2l)
  l p <  q  <=>  x + y = 2 q   <=>  x + y = 2 (q mod l) (mod 2l)
  => for l > r (=q/p), the left side is FORCED: x+y = 0 mod 2l.
RSA-270 prior band r in [1.765, 2.266]: all primes l >= 3 have l > r
  => x+y = 0 (mod 2l) FORCED for every prime l >= 3  (strong certificate family);
  only l=2 carries a genuine side bit (r<2 vs r>2).
Bit accounting: lattice 6.17 bits (N-only computable) + 1 vertex-side bit (verification-only,
layer-2); the N-only computable part remains 6.17 bits.
"""
import math

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n + 1) if sieve[i]]

N = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
        "3578286788836931857711641821391926857265831491306067262691135402760979316634"
        "1626693946596196427744273886601876896313468704059066746903123910748277606548"
        "649151920812699309766587514735456594993207")

print("== A. general side law (synthetic, both sides) ==")
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (13, 29), (17, 23), (29, 61), (11, 41), (5, 17)]:
    for l in primes_upto(31):
        x, y = l * p + q, abs(l * p - q)
        side_left = (l * p >= q)
        val = (x + y) % (2 * l)
        pred = 0 if side_left else (2 * q) % (2 * l)
        if val != pred:
            ok = False
            print(f"  FAIL p={p} q={q} l={l}: val={val} pred={pred}")
print("  x+y = 0 mod 2l iff l*p >= q; else 2q mod 2l:", "PASS" if ok else "FAIL")

print("\n== B. forced-sum certificate (l >= 3, prior band r < l): REAL-side constraint ==")
# (i) synthetic verification: for semiprimes with r < 3, any l >= 3 branch has x+y = 2l p = 0 mod 2l
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (17, 23), (29, 31)]:
    for l in (3, 5, 7, 11):
        x, y = l * p + q, abs(l * p - q)
        if (x + y) % (2 * l) != 0:
            ok = False
            print(f"  REAL-constraint FAIL p={p} q={q} l={l}")
print("  synthetic r<3: x+y = 0 mod 2l for l>=3:", "PASS" if ok else "FAIL")
# (ii) RSA-270 class-level shadow: the class-level values mix sides; the certificate for a
#      CLAIMED observation is the real-side constraint x+y = 0 mod 2l.
print("  RSA-270 certificate: any claimed (x,y) for l >= 3 must satisfy x+y = 0 (mod 2l);")
print("  class-level shadow values (mixed sides, informational only):")
adm = []
for p0 in range(72):
    if p0 % 6 != 5: continue
    for q0 in range(72):
        if q0 % 6 != 5: continue
        if (p0 * q0) % 72 == N % 72 and (p0 + q0) % 72 == 16:
            adm.append((p0, q0))
for l in (3, 5, 7):
    vals = sorted({(l * p0 + q0 + abs(l * p0 - q0)) % (2 * l) for p0, q0 in adm})
    print(f"  l={l}: class-level x+y mod {2*l} values = {vals} (real-side value is 0)")

print("\n== C. bit accounting ==")
print("  N-only computable: forced lattice S = 16 mod 72  -> 6.17 bits")
print("  verification-only (layer-2): 1 vertex-side bit (l=2) + forced-sum family (l>=3)")
print("  -> total certificate information: 6.17 bits computable + 1 bit verifiable;")
print("     the side bit does NOT extend the N-only computable part (layer-2 observability wall).")
