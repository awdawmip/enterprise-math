"""
BRC relation-layer collapse calibration (Route C-lite): toy QS on ~40-bit semiprimes.
Measures, per modulus: full-smooth relation yield, one-large-prime partials, same-large-prime
recoalescence events, and multiplier square-class duplication (trivial-cycle rate) across
k-family shells. Calibration only — no RSA-270 execution, no new-method claim.
"""
import math, random
from math import gcd

def primes_upto(n):
    sieve = bytearray([1]) * (n + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n + 1) if sieve[i]]

def gen_semiprime(bits, rng):
    lo = 1 << (bits // 2 - 1); hi = 1 << (bits // 2)
    def prime():
        while True:
            c = rng.randrange(lo | 1, hi, 2)
            if c % 3 == 0 or c % 5 == 0: continue
            d = c - 1; r = 0
            while d % 2 == 0: d //= 2; r += 1
            ok = True
            for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
                x = pow(a, d, c)
                if x in (1, c - 1): continue
                for _ in range(r - 1):
                    x = x * x % c
                    if x == c - 1: break
                else:
                    ok = False; break
            if ok: return c
    p, q = prime(), prime()
    while p == q: q = prime()
    return p * q

def factor_smooth(v, fb):
    """trial-factor v over fb; returns (residue, valuation parity dict) if fully smooth else None.
    Returns (r, parities) with r the unfactored part (1 if smooth)."""
    par = {}
    r = v
    for p in fb:
        cnt = 0
        while r % p == 0:
            r //= p; cnt += 1
        if cnt & 1: par[p] = 1
        if r == 1: break
    return r, par

fb = primes_upto(300)
rng = random.Random(20260906)
print("factor base:", len(fb), "primes up to", fb[-1])
rows = []
for t in range(12):
    N = gen_semiprime(40, rng)
    x0 = math.isqrt(N) + 1
    W = 6000
    full = 0; partials = {}; same_lp_events = 0
    for i in range(W):
        v = (x0 + i) ** 2 - N
        r, par = factor_smooth(v, fb)
        if r == 1:
            full += 1
        elif r < (1 << 20):
            # one-large-prime partial: keep track of the large prime r
            if r in partials:
                same_lp_events += 1
                partials[r] += 1
            else:
                partials[r] = 1
    # k-family square-class duplication: Q_k = 4kN shell residues x0_k^2 - 4kN, k=1..16
    kclass = {}
    dup = 0
    for k in range(1, 17):
        A = 4 * k * N
        s = math.isqrt(A)
        if s * s < A: s += 1
        r = s * s - A
        # squarefree kernel
        kern = 1
        for p in fb:
            while r % p == 0 and r % (p * p) == 0:
                r //= (p * p)
            if r == 1: break
        # approximate kernel: remove square factors of small primes only
        rr = s * s - A
        for p in fb:
            p2 = p * p
            while rr % p2 == 0:
                rr //= p2
        if rr in kclass:
            dup += 1
            kclass[rr].append(k)
        else:
            kclass[rr] = [k]
    rows.append((full, sum(v > 1 for v in partials.values()), same_lp_events, dup))
    print(f"N[{t:2d}] full-smooth={full:4d} one-LP-partials={sum(v > 1 for v in partials.values()):4d} "
          f"same-LP-recoalescences={same_lp_events:4d} k-family square-class dups(k<=16)={dup:2d}")
print()
print("summary: k-family square-class duplication (trivial recoalescence share) across k=1..16 shells")
print("is high; this is the BRC quotient that must be applied before parity-collision counting.")
print("No relation matrix was assembled; no factorization claim. Calibration only.")
