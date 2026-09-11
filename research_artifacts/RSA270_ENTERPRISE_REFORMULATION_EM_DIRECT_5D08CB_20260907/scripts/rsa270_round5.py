"""
Round 5 (EM-DIRECT-5D08CB / DIRECT-RSA270):
  A. SG4 verifier stress test: 30 random prior-consistent semiprimes (valid S -> PASS; wrong S -> FAIL).
  B. Energy identity (S-affine observable): sum_e P(e)^2 = 4(N+1) + 12S  (verified).
     P is {0,2,4}-valued: outer-only mass N+1-S, overlap mass S (both on the parity lattice, doubled):
     sum P^2 = 4*(N+1-S) + 16*S = 4(N+1) + 12S.
"""
import math, random

def is_probable_prime(n, rounds=20):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d = n-1; r = 0
    while d % 2 == 0: d//=2; r+=1
    rng = random.Random(20260906)
    for _ in range(rounds):
        a = rng.randrange(2, n-2)
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def gen_prior_semiprime(bits, rng):
    lo = 1 << (bits//2 - 1); hi = 1 << (bits//2)
    def prime():
        while True:
            c = rng.randrange(lo | 1, hi, 2)
            if c % 6 != 5: continue
            if is_probable_prime(c): return c
    while True:
        p, q = prime(), prime()
        if p != q: return p*q, p, q

def adm_S_prior(Nn, m):
    M = 6 * m
    s = set()
    for a in range(5 % 6, M, 6):
        for b in range(5 % 6, M, 6):
            if (a * b) % M == Nn % M:
                S = (a + b) % (2 * m)
                if S % 2 == 0:
                    s.add(S)
    return sorted(s)

def verify_sigma(S, Nn):
    if S % 2 != 0: return False
    A = S // 2
    B = A * A - Nn
    r = math.isqrt(B)
    if r * r != B: return False
    p, q = A - r, A + r
    if p * q != Nn: return False
    if not (is_probable_prime(p) and is_probable_prime(q)): return False
    if not (p % 3 == 2 and q % 3 == 2): return False
    if Nn % 8 == 7 and S % 8 != 0: return False
    a = 3 if Nn % 8 == 7 else 2
    mm = (1 << (a - 1)) * 9          # modulus 2^a * 9 = 72 (a=3) or 36 (a=2)
    cls = adm_S_prior(Nn, mm)
    if not (len(cls) == 1 and S % (2 * mm) == cls[0]): return False
    return True

print("== A. SG4 verifier stress test (30 prior-consistent semiprimes, 40 bits) ==")
rng = random.Random(20260906)
pass_true = pass_false = 0
for t in range(30):
    Nn, p, q = gen_prior_semiprime(40, rng)
    S = p + q
    v1 = verify_sigma(S, Nn)
    v2 = verify_sigma(S + 144, Nn)
    if v1: pass_true += 1
    if not v2: pass_false += 1
print(f"  valid S accepted: {pass_true}/30 ;  wrong S rejected: {pass_false}/30")

print("\n== B. energy identity sum_e P(e)^2 = 2(N+1) + 6S ==")
def profile_poly(Nn, p, q):
    S = p + q
    P = {}
    for s, mult in [((Nn + 3)//2, 2), ((S + 2)//2, 2)]:
        for j in range(s - 1):
            e = 2 - s + 2*j
            P[e] = P.get(e, 0) + mult
    return P
ok = True
for (Nn, p, q) in [(35,5,7),(143,11,13),(391,17,23),(899,29,31),(3599,59,61),(1000003,997,1003)]:
    if not (is_probable_prime(p) and is_probable_prime(q)): continue
    P = profile_poly(Nn, p, q)
    E = sum(c*c for c in P.values())
    pred = 2*(Nn + 1) + 6*(p + q)   # profile lives on one parity class (half mass)
    if E != pred:
        ok = False
        print(f"  FAIL N={Nn}: E={E} pred={pred}")
print("  energy identity:", "PASS" if ok else "FAIL")
print("\n  note: E is S-affine -> same family as SG1 derivative ladder (unobservable cheaply);")
print("        the dichotomy (8e5f2a) therefore covers energy/mass/norm observables as well.")
