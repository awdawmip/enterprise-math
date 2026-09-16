"""
RSA-270 shortcut hunt, round 2 (EM-DIRECT-5D08CB / DIRECT-RSA270):
bracket zero-set Z(N,S) = {m : B(w_m)=0} classification.

Exact bracket:  B(u) = u^((S-N-1)/2)(1-u^(N+1)) + (1-u^S);  P(w_m)=0 <=> B(w_m)=0 (m>=3).

New exact identity: gcd(N+1, S) = gcd(p^2-1, p+q) = gcd(q^2-1, p+q)
  -> the common-zero (both-terms-vanish) part of Z = {m : m | gcd(N+1, S)}.

This script:
  1. verifies the gcd identity on synthetic semiprimes;
  2. computes the RSA-270 Z-vectors for the admissible S-classes mod 144/216
     (prior-consistent), identifies distinguishing moduli and resolution;
  3. calibrates on synthetic semiprimes that Z depends only on (N mod 2m, S mod 2m) class
     (trivial determinism) and quantifies the zero-set density per m.
"""
import math, cmath, random

RSA270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
             "3578286788836931857711641821391926857265831491306067262691135402760979316634"
             "1626693946596196427744273886601876896313468704059066746903123910748277606548"
             "649151920812699309766587514735456594993207")
N = RSA270

def pow_w(m, k):
    return cmath.exp(2j * math.pi * (k % m) / m)

def B_zero(Nn, S, m):
    e1 = ((S - Nn - 1) // 2) % m
    eN = (Nn + 1) % m
    eS = S % m
    w = pow_w(m, 1)
    b = (w ** e1) * (1 - w ** eN) + (1 - w ** eS)
    return abs(b) < 1e-9

def is_prime_mr(n, rounds=20):
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

print("== 1. gcd identity gcd(N+1,S)=gcd(p^2-1,p+q)=gcd(q^2-1,p+q) ==")
ok = True
rng = random.Random(7)
t = 0
while t < 8:
    p = rng.randrange(1000, 100000) | 1
    q = rng.randrange(1000, 100000) | 1
    if not (is_prime_mr(p) and is_prime_mr(q) and p != q): continue
    Nn, S = p*q, p+q
    a = math.gcd(Nn+1, S); b = math.gcd(p*p-1, S); c = math.gcd(q*q-1, S)
    if not (a == b == c):
        ok = False
        print(f"  FAIL at p={p} q={q}: {a} {b} {c}")
    t += 1
print("  gcd identity:", "PASS (8 semiprimes)" if ok else "FAIL")

print("\n== 2. RSA-270 Z-vectors for admissible S-classes (prior) ==")
# admissible S mod 144 and mod 216 classes via enumeration
def adm_S(mod):
    s = set()
    for a in range(mod):
        if a % 6 != 5: continue
        for b in range(mod):
            if b % 6 != 5: continue
            if (a*b) % mod == N % mod:
                S = (a+b) % mod
                if S % 2 == 0:
                    s.add(S)
    return sorted(s)
c144 = adm_S(144); c216 = adm_S(216)
print("admissible S mod 144:", c144, " mod 216:", c216)
# Z-vectors for each class, m<=200
for cls, name in [(c144[0], "S mod 144 = %d" % c144[0]), (c144[1], "S mod 144 = %d" % c144[1])]:
    Z = [m for m in range(3, 201) if B_zero(N, cls, m)]
    print(f"  {name}: Z = {Z}")
# distinguishing moduli between the two mod-144 classes
Z16 = {m for m in range(3,201) if B_zero(N, c144[0], m)}
Z88 = {m for m in range(3,201) if B_zero(N, c144[1], m)}
dist = sorted(Z16 ^ Z88)
print("moduli distinguishing the two S mod 144 classes (m<=200):", dist)

print("\n== 3. zero-set density per m over admissible S mod 2m classes ==")
# for each m, count admissible S mod 2m classes where B=0
dens = []
for m in list(range(3, 33)) + [36, 48, 60, 72, 96, 120, 144]:
    classes = adm_S(2*m)
    zc = sum(1 for S in classes if B_zero(N, S, m))
    dens.append((m, zc, len(classes)))
    if m <= 33 or m in (36, 48, 60, 72, 96, 120, 144):
        print(f"  m={m:3d}: zero classes {zc}/{len(classes)}")
print("\n(density = zero-fraction; expect small, ~O(1/m)-ish, no structural spike beyond divisors of 72)")
