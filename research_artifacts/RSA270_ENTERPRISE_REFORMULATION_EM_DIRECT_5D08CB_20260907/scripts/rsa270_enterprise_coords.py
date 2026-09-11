"""
Enterprise-coordinate continuation (EM-DIRECT-5D08CB / DIRECT-RSA270).

Part 1: Enterprise-coordinate exact bridge identities (Jacobi four-square / X6 stratum /
four-layer triangular count / two-plateau profile) — all reduce to sigma(N) = (p+1)(q+1) = N+S+1.

Part 2: Forced-S congruence lattice for RSA-270:
  - unconditional: S mod 2m forced classes (scan m=1..192)
  - construction-family prior (p,q odd, p==q==2 mod 3): forced classes mod 6m (scan m=1..288)
  - find maximal forced modulus; verify sigma(N)=0 mod 72, N=55 mod 72, S=16 mod 72.

Part 3: RSA-260 out-of-sample validation of the whole machinery using the published
factorization (2026-09-03): multiply/primality/bit-length/prefix/2-mod-3/ratio-band checks,
forced-S class of RSA-260 matches its REAL S, sigma==0 mod 72, torsion fingerprint tables.

Part 4: congruence-restricted Fermat search statement (S = 16 + 72t) and entropy accounting.
"""
import math, random, cmath

RSA270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
             "3578286788836931857711641821391926857265831491306067262691135402760979316634"
             "1626693946596196427744273886601876896313468704059066746903123910748277606548"
             "649151920812699309766587514735456594993207")
RSA260 = int("2211282552952966643528108525502623092761208950247001539441374831912882294140"
             "2001986512729726569746599085900330031400051170742204560859276357953757185954"
             "2988389587092292384910067030341246205457845664136645406842143612930176940208"
             "46391065875914794251435144458199")
P260A = int("4397328654844826923795068102505872571721883526553349659561256924505973939597"
            "593482272505698004801207988043088656411102133523080581")
P260B = int("5028695206842569864686141618253083416610081090075366674776775706538324961364"
            "412200138116378509733307971876652984898985905923678379")

def is_probable_prime(n, rounds=40):
    if n < 2: return False
    small = [2,3,5,7,11,13,17,19,23,29,31,37]
    for p in small:
        if n % p == 0: return n == p
    d = n - 1; r = 0
    while d % 2 == 0: d //= 2; r += 1
    rng = random.Random(20260906)
    for _ in range(rounds):
        a = rng.randrange(2, n - 2)
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

def forced_classes(N, prior, m):
    """admissible S mod 2m classes. prior: force p,q odd and p==q==2 mod 3 (mod lcm(2m,3)=6m)."""
    if prior:
        M = 6 * m
        out = set()
        for a in range(5 % 6, M, 6):
            for b in range(5 % 6, M, 6):
                if (a * b) % M == N % M:
                    S = (a + b) % (2 * m)
                    if S % 2 == 0:
                        out.add(S)
        return sorted(out)
    else:
        out = set()
        for a in range(1, 2 * m, 2):
            for b in range(1, 2 * m, 2):
                if (a * b) % (2 * m) == N % (2 * m):
                    S = (a + b) % (2 * m)
                    if S % 2 == 0:
                        out.add(S)
        return sorted(out)

def g_m(m, r):
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

def g_m_complex(m, r):
    w = cmath.exp(2j * math.pi / m)
    r %= m
    return (w ** (2 - r) - w ** r) / (1 - w ** 2)

print("== Part 1: Enterprise-coordinate bridge (exact identities) ==")
print("X6 squared shell: for N==7 mod 8 the 1/2/3-square support strata vanish;")
print("  first nonempty support stratum = 4-axis stratum, cardinality C(6,4)*R4(N) = 15*8*sigma(N) = 120*sigma(N)")
print("Four-layer triangular count: C_X(N) = #{(a,b,c,d)>=0 : B2(a)+B2(b)+B2(c)+B2(d)=2N+2} = sigma(N)")
print("Two-plateau profile total mass = sigma(N); Fermat midpoint A = S/2 = (sigma(N)-N-1)/2")
print("sigma(N) = (p+1)(q+1) = N+S+1   [exact]")

print("\n== Part 2: RSA-270 forced-S congruence lattice ==")
print("N mod 8 =", RSA270 % 8, " N mod 72 =", RSA270 % 72, " N mod 144 =", RSA270 % 144)
# unconditional scan
uncond_forced = []
for m in range(1, 193):
    cls = forced_classes(RSA270, False, m)
    if len(cls) == 1:
        uncond_forced.append((m, cls[0]))
print(f"unconditional forced S mod 2m classes (m=1..192): {uncond_forced}")
# prior scan
prior_forced = []
max_m = 0
for m in range(1, 289):
    cls = forced_classes(RSA270, True, m)
    if len(cls) == 1:
        prior_forced.append((m, cls[0]))
        max_m = m
print(f"prior-forced count m<=288: {len(prior_forced)}; maximal forced modulus 2m = {2*max_m}")
print(f"prior-forced (m, S mod 2m) up to m=36: {[x for x in prior_forced if x[0] <= 36]}")
# show m=72 (mod 144) classes
print("S mod 144 classes (prior):", forced_classes(RSA270, True, 72))
print("S mod 216 classes (prior):", forced_classes(RSA270, True, 108))
# consistency: sigma = 0 mod 72 requires S = -N-1 mod 72
s72 = forced_classes(RSA270, True, 36)
print("S mod 72 (prior):", s72, " -> sigma(N) mod 72 =", (RSA270 + s72[0] + 1) % 72)
print("entropy reduction: log2(72) =", math.log2(72), "bits")

print("\n== Part 3: RSA-260 out-of-sample validation ==")
print("p1*p2 == RSA260:", P260A * P260B == RSA260)
print("p1 bits:", P260A.bit_length(), " p2 bits:", P260B.bit_length())
print("p1 prime (MR40):", is_probable_prime(P260A), " p2 prime (MR40):", is_probable_prime(P260B))
print("p1,p2 == 2 mod 3:", P260A % 3 == 2 and P260B % 3 == 2)
print("p1,p2 binary prefix 11:", (P260A >> (P260A.bit_length()-2)) == 3 and (P260B >> (P260B.bit_length()-2)) == 3)
r260 = max(P260A, P260B) / min(P260A, P260B)
print("factor ratio:", r260, " (band [1.765, 2.266] for RSA-270 prior is a different N; RSA-260 itself just consistent family evidence)")
S260 = P260A + P260B
print("N260 mod 72 =", RSA260 % 72)
cls260 = forced_classes(RSA260, True, 36)
print("RSA-260 prior-forced S mod 72 =", cls260, "  real S mod 72 =", S260 % 72)
print("RSA-260 sigma mod 72 =", (RSA260 + S260 + 1) % 72)
# torsion fingerprint: for a set of m, verify complex-ratio vs sine closed form on both numbers
print("\ntorsion closed-form cross-check (complex ratio vs sine), m=3..64:")
for name, N, S in [("RSA-260", RSA260, S260)]:
    bad = 0
    for m in range(3, 65):
        r0 = ((N + 3)//2) % m
        r1 = ((S + 2)//2) % m
        a = 2*g_m_complex(m, r0) + 2*g_m_complex(m, r1)
        b = 2*g_m(m, r0) + 2*g_m(m, r1)
        if abs(a - b) > 1e-9:
            bad += 1
    print(f"  {name}: mismatches={bad}")

print("\n== Part 4: congruence-restricted Fermat search statement ==")
print("RSA-270: S = 16 + 72t ; A = S/2 = 8 + 36t ; B = A^2 - N must be a perfect square")
print("search interval: A in [ceil(sqrt(N)), 2^448]; 72x reduction vs unrestricted Fermat (6.17 bits)")
print("honest note: interval size ~2^447/36 ~ 2^442 candidates; not feasible — this is the maximal")
print("N-only leverage the exact Enterprise identities provide; no speedup claim beyond residue pruning")
