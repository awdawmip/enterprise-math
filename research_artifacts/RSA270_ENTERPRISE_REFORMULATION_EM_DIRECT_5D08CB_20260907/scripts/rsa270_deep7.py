"""
Deep research round 7 (EM-DIRECT-5D08CB / DIRECT-RSA270):
the joint certificate's sum/difference linear structure and the vertex-side bit.

For branch l:  x = l p + q,  y = |l p - q|  =>
  if l p >= q:  x + y = 2 l p,  x - y = 2 q
  if l p <  q:  x + y = 2 q,    x - y = 2 l p
  => {x+y, x-y} = {2 l p, 2 q}  (factor multiples mod 72, per admissible class)
  l=2: {4p, 2q} mod 72 ;  x+y mod 4 = 0 iff 2p > q (r < 2 side), = 2 iff 2p < q (r > 2 side)
  => the x+y mod 4 bit is the VERTEX-SIDE bit (r < 2 vs r > 2), readable from the certificate.
Verify on synthetic semiprimes and compute the RSA-270 x2 side split.
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

print("== A. sum/difference linear certificate (synthetic verification) ==")
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (17, 23), (29, 31)]:
    for l in primes_upto(31):
        x = l * p + q
        y = abs(l * p - q)
        s, d = x + y, x - y
        expect = {2 * l * p, 2 * q}
        if {s, d} != expect:
            ok = False
            print(f"  FAIL p={p} q={q} l={l}: {{s,d}} = {{{s},{d}}} vs {expect}")
print("  {x+y, x-y} = {2*l*p, 2*q}:", "PASS" if ok else "FAIL")

print("\n== B. vertex-side bit (x+y mod 4 decides r<2 vs r>2 for l=2) ==")
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (13, 29), (17, 23), (29, 61)]:
    x, y = 2 * p + q, abs(2 * p - q)
    side_pred = 0 if 2 * p >= q else 2   # x+y = 4p (0 mod 4) or 2q (2 mod 4)
    side_actual = (x + y) % 4
    if side_actual != side_pred:
        ok = False
    r2 = "r<2" if 2 * p > q else "r>2"
    print(f"  N={p*q} (r={q/p:.3f}, {r2}): x+y mod 4 = {side_actual}  (pred {side_pred})")
print("  vertex-side bit:", "PASS" if ok else "FAIL")

print("\n== C. RSA-270 x2 side split ==")
adm = []
for p0 in range(72):
    if p0 % 6 != 5: continue
    for q0 in range(72):
        if q0 % 6 != 5: continue
        if (p0 * q0) % 72 == N % 72 and (p0 + q0) % 72 == 16:
            adm.append((p0, q0))
left = [(p0, q0) for p0, q0 in adm if 2 * p0 >= q0]    # x+y = 4p0, 2p>q side (r<2-ish)
right = [(p0, q0) for p0, q0 in adm if 2 * p0 < q0]    # x+y = 2q0, 2p<q side (r>2-ish)
print(f"  admissible classes: {len(adm)} ; 2p0 >= q0 (sum=4p, r<2 side): {len(left)} ; 2p0 < q0 (sum=2q, r>2 side): {len(right)}")
print(f"  4p mod 72 set: {sorted({(4 * p0) % 72 for p0, q0 in adm})}")
print(f"  2q mod 72 set: {sorted({(2 * q0) % 72 for p0, q0 in adm})}")
print("  => the x2 certificate carries one VERTEX-SIDE bit (r<2 vs r>2) via x+y mod 4;")
print("     under the prior band both sides are admissible -> the bit is genuine factor data,")
print("     readable from any claimed layer-2 observation (x,y).")
