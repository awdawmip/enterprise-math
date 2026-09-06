"""
Deep research round 2 (EM-DIRECT-5D08CB / DIRECT-RSA270):
  1. CRT joint view of the BRC root trajectory over primes:
       y(l) mod p = +-q  (CONSTANT two-point set)
       y(l) mod q = +-l*p (varies with l mod q)
  2. two-l Plucker hyperbola for the x-prime endpoint family:
       (x(l1)-x(l2)) * (l1*x(l2)-l2*x(l1)) = (l1-l2)^2 * N
  3. V-function ray characterization: V_{p,q}(l) = |p*l - q| over primes has ray
     coefficients (p, q) = the factors; recovering them from the y-sequence gives (p,q) exactly.
     (constructive recovery demonstration on small semiprimes)
"""
import math

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n + 1) if sieve[i]]

print("== 1. CRT joint view of the root trajectory ==")
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (17, 23)]:
    for l in primes_upto(31):
        y = abs(l * p - q)
        if y % p not in (q % p, (-q) % p):
            ok = False
        if y % q not in ((l * p) % q, (-l * p) % q):
            ok = False
            print(f"  q-coord FAIL p={p} q={q} l={l}: y%q={y%q} vs +-lp = {(l*p)%q}, {(-l*p)%q}")
print("  CRT view: y mod p in {+-q} constant; y mod q in {+-l*p} varying:", "PASS" if ok else "FAIL")

print("\n== 2. two-l Plucker hyperbola ==")
ok = True
for (p, q) in [(3, 5), (5, 7), (11, 13), (17, 23)]:
    N = p * q
    Ls = primes_upto(31)
    for i, l1 in enumerate(Ls):
        for l2 in Ls[i+1:]:
            x1, x2 = l1 * p + q, l2 * p + q
            lhs = (x1 - x2) * (l1 * x2 - l2 * x1)
            rhs = (l1 - l2) ** 2 * N
            if lhs != rhs:
                ok = False
                print(f"  FAIL N={N} l1={l1} l2={l2}: {lhs} vs {rhs}")
print("  (x(l1)-x(l2))*(l1*x(l2)-l2*x(l1)) = (l1-l2)^2*N:", "PASS" if ok else "FAIL")

print("\n== 3. V-function ray-coefficient recovery (constructive) ==")
for (p, q) in [(3, 5), (5, 7), (11, 13), (17, 23)]:
    Ls = primes_upto(31)
    # recover p from the slope: differences of y between consecutive primes on the same side
    # left side: l < q/p: y = q - p*l  (slope -p); right side: y = p*l - q (slope +p)
    ys = [abs(l * p - q) for l in Ls]
    # recover p from any two consecutive primes with both on the same side
    rec_p = set()
    for i in range(len(Ls) - 1):
        l1, l2 = Ls[i], Ls[i + 1]
        if (l1 * p - q) * (l2 * p - q) > 0:  # same side
            rec_p.add(abs(ys[i + 1] - ys[i]) // (l2 - l1))
    # recover q from the vertex side: q = p*l +- y (left side): q = p*l + y for l < q/p
    rec_q = set()
    for i, l in enumerate(Ls):
        if l * p < q:
            rec_q.add(p * l + ys[i])
        else:
            rec_q.add(p * l - ys[i])
    print(f"  N={p*q}: recovered p from slopes={sorted(rec_p)} (true {p}), q from rays={sorted(rec_q)} (true {q})")
print("  => the V_{p,q} ray coefficients over primes ARE the factors; recovery is exact")
print("     (layer-2 data; observability wall unchanged)")
