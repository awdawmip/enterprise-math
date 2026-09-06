"""
BRC multi-layer collapse broad route test for RSA-270 (EM-DIRECT-5D08CB / DIRECT-RSA270).

D1: axis-difference reading of the profile (per-divisor fixed-sum ladders).
D2: axis-truncation collapse T_B(N) = sum_{d|N} min(B, (d+N/d)/2) — exact slope-break at Fermat midpoint A=S/2.
D3: mod-c collapse classification of the {0,2,4}-valued profile.
D4: observable-algebra summary (dyadic coarse-grain = S-bits; torsion = residues; moments = polynomials).
D5: RSA-270 joint prior-collapse certificate: allowed P(w_m) sets m=3..64, forced-zero subset, joint information summary.
F : broad coordinate-residual gcd sweep (multi-layer collapse families) on RSA-270.
"""
import math
from math import comb, gcd

RSA270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
             "3578286788836931857711641821391926857265831491306067262691135402760979316634"
             "1626693946596196427744273886601876896313468704059066746903123910748277606548"
             "649151920812699309766587514735456594993207")
N = RSA270

def g_m(m, r):
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

def admissible_r1(m, N=N):
    M6 = 6 * m
    s = set()
    for a in range(5 % 6, M6, 6):
        for b in range(5 % 6, M6, 6):
            if (a * b) % M6 == N % M6:
                S = (a + b) % (2 * m)
                if S % 2 == 0:
                    s.add(((S + 2)//2) % m)
    return sorted(s)

def T_(x):
    return x * (x + 1) // 2

print("== D2: axis-truncation collapse T_B(N) = sum_{d|N} min(B,(d+N/d)/2) ==")
def T_B_formula(N, B, divisors):
    return sum(min(B, (d + N // d) // 2) for d in divisors)

def T_B_enum(N, B):
    m = (N - 1) // 2
    cnt = 0
    amax = int((math.isqrt(8 * m + 1) - 1) // 2)
    for a in range(min(B, amax + 1)):
        r1 = m - T_(a)
        if r1 < 0: break
        for b in range(0, int((math.isqrt(8 * r1 + 1) - 1) // 2) + 1):
            r2 = r1 - T_(b)
            if r2 < 0: break
            for c in range(0, int((math.isqrt(8 * r2 + 1) - 1) // 2) + 1):
                r3 = r2 - T_(c)
                if r3 < 0: break
                # d such that T_d = r3
                disc = 8 * r3 + 1
                s = math.isqrt(disc)
                if s * s == disc and (s - 1) % 2 == 0:
                    cnt += 1
    return cnt

def divisors_of(N):
    out = set()
    for i in range(1, math.isqrt(N) + 1):
        if N % i == 0:
            out.add(i); out.add(N // i)
    return sorted(out)

for (Nn, p, q) in [(143, 11, 13), (391, 17, 23)]:
    S = p + q
    divs = divisors_of(Nn)
    print(f"N={Nn} p={p} q={q} S={S} (slope break expected at B=S/2={S//2} and B=(N+1)/2={(Nn+1)//2})")
    prev = None
    ok = True
    for B in range(1, 16):
        f = T_B_formula(Nn, B, divs)
        e = T_B_enum(Nn, B)
        d = f - prev if prev is not None else None
        mark = " <<< slope break" if prev is not None and d != 4 else ""
        if f != e: ok = False
        print(f"  B={B:2d}: formula={f:3d} enum={e:3d} increment={d}{mark}")
        prev = f
    print("  formula==enumeration:", ok)

print("\n== D3: mod-c collapse of the {0,2,4} profile ==")
print("mod 2: identically 0  -> total erasure (no S info)")
print("mod c>=3: values {0,2,4} distinct mod c  -> plateau boundary (S-2)/2 retained exactly")
print("         -> every mod-c collapse with c>=3 is S-equivalent; c=2 erases everything")

print("\n== D5: RSA-270 joint prior-collapse certificate (allowed P(w_m) sets, m=3..64) ==")
total_info = 0.0
forced = []
for m in range(3, 65):
    ar1 = admissible_r1(m)
    r0 = ((N + 3)//2) % m
    allowed = sorted({round(2*g_m(m, r0) + 2*g_m(m, r), 9) for r in ar1})
    total_info += math.log2(m / len(ar1))
    if len(ar1) == 1:
        forced.append((m, allowed[0]))
print("forced P(w_m) (|admissible|=1):", forced)
print("joint ladder information summary (sum log2(m/|adm|), upper estimate):", round(total_info, 2), "bits")
# sample of multi-class members
for m in (5, 7, 11, 13, 16, 17, 31):
    ar1 = admissible_r1(m); r0 = ((N + 3)//2) % m
    allowed = sorted({round(2*g_m(m, r0) + 2*g_m(m, r), 6) for r in ar1})
    print(f"  m={m:2d}: |adm|={len(ar1):2d}  allowed P(w_{m}) values={allowed}")

print("\n== F: broad multi-layer collapse gcd sweep on RSA-270 ==")
def ball(d, r):
    return sum((1 << j) * comb(d, j) * comb(r, j) for j in range(d + 1))

sweep = 0; hits = 0; worst = 0
# family 1: L1 balls B_d(r) near r ~ N^{1/d}, d=2..6, window 256
for d in range(2, 7):
    r0 = int(round(N ** (1.0 / d)))
    for r in range(max(0, r0 - 256), r0 + 257):
        v = ball(d, r)
        g = gcd(N, abs(N - v)) if v != N else N
        sweep += 1
        if g > 1: hits += 1; worst = max(worst, g)
print(f"family 1 (B_d(r) near N^(1/d), d=2..6, w=256): tests={sweep} nontrivial={hits}")
# family 2: triangular-shell B2 offsets (four-layer axes) near sqrt(N/4), window 512
sweep = 0; hits = 0
r0 = int(math.isqrt(N // 4))
for r in range(max(0, r0 - 512), r0 + 513):
    v = 4 * T_(r) + 1  # B2(r)
    for mult in (1, 2, 4):
        g = gcd(N, abs(mult * N - v)) if mult * N != v else N
        sweep += 1
        if g > 1: hits += 1
print(f"family 2 (B2 triangular shells near sqrt(N/4), w=512): tests={sweep} nontrivial={hits}")
# family 3: dimension-descending L1 collapse chain 6->5->...->1 (bit telescoping), window 32
print("family 3: dimension-descending collapse chain (see 20260906T104500):")
res = N
for d in range(6, 0, -1):
    r = int(round(res ** (1.0 / d)))
    v = ball(d, r)
    res = abs(res - v)
    print(f"  d={d}: r={r} bitlen(res)={res.bit_length()}  gcd(N,res)={gcd(N, res) if res else 'N'}")
# family 4: k-multiplier shell midpoints near ceil(sqrt(4kN)), k=1..64
sweep = 0; hits = 0
for k in range(1, 65):
    x0 = math.isqrt(4 * k * N)
    if x0 * x0 < 4 * k * N: x0 += 1
    for j in range(0, 8):
        dkj = (x0 + j) ** 2 - 4 * k * N
        g = gcd(N, dkj) if dkj else N
        sweep += 1
        if g > 1: hits += 1
print(f"family 4 (multiplier shell d_(k,j), k<=64, j<=7): tests={sweep} nontrivial={hits}")
