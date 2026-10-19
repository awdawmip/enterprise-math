"""
RSA-270 shortcut hunt (EM-DIRECT-5D08CB / DIRECT-RSA270), round: closed-form profile +
zero criterion + forced-lattice tower generalization.

Closed form (exact):
  P(u) = 2 W_{(N+3)/2}(u) + 2 W_{(S+2)/2}(u),  W_s(u) = u^(2-s) (1-u^(2(s-1)))/(1-u^2)
  =>  P(u) = 2 u^((2-S)/2) B(u) / (1-u^2),
      B(u) = u^((S-N-1)/2) (1-u^(N+1)) + (1-u^S)          (bracket)

Zero criterion: P(w_m)=0 <=> B(w_m)=0 (m>=3; 1-w^2 != 0).

RSA-270 with prior-forced S = 16 mod 72: B(w_m) = w^(-20)(1-w^56) + 1 - w^16
  = 0  <=>  m | 72 and 24 does not divide m   (candidate family {3,4,6,8,9,12,18,36}).
Verification below by direct enumeration of admissible classes for m<=200.
"""
import math, cmath

RSA270 = int("2331085303444075445276376569106805241456198124803054490429486119684959182451"
             "3578286788836931857711641821391926857265831491306067262691135402760979316634"
             "1626693946596196427744273886601876896313468704059066746903123910748277606548"
             "649151920812699309766587514735456594993207")
N = RSA270

def W_poly(s):
    return {2 - s + 2*j: 1 for j in range(s - 1)}

def profile_poly(Nn, p, q):
    S = p + q
    P = {}
    for s, m in [((Nn + 3)//2, 2), ((S + 2)//2, 2)]:
        for j in range(s - 1):
            e = 2 - s + 2*j
            P[e] = P.get(e, 0) + m
    return P

def profile_closed(Nn, S):
    """returns dict u-exponent -> coeff of 2 u^((2-S)/2) B(u) / (1-u^2) computed exactly."""
    # numerator polynomial N_u(u) = 2 u^((2-S)/2) B(u) = 2 [ u^((2-S)/2)*u^((S-N-1)/2)(1-u^{N+1}) + u^((2-S)/2)(1-u^S) ]
    # = 2 [ u^((1-N)/2)(1-u^{N+1}) + u^((2-S)/2)(1-u^S) ]
    from collections import defaultdict
    num = defaultdict(int)
    for e, c in [( (1-Nn)//2, 2), ( (1-Nn)//2 + Nn + 1, -2), ( (2-S)//2, 2), ( (2-S)//2 + S, -2)]:
        num[e] += c
    # divide by (1-u^2): num = (1-u^2) * P  =>  P[e] = P[e-2] + num[e]  (solve forward from lowest exponent)
    emin = min(num)
    P = {}
    cur = 0
    e = emin
    while True:
        cur += num.get(e, 0)
        if cur != 0:
            P[e] = cur
        # terminate when remaining numerator is zero beyond max
        e += 2
        if e > max(num) + 4 and cur == 0:
            break
    # sanity: total mass
    return P

def g_m(m, r):
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

def pow_w(m, x):
    """w^x with w = primitive m-th root; x integer (exact modular reduction)."""
    return cmath.exp(2j * math.pi * (x % m) / m)

def B_eval(Nn, S, m):
    e1 = ((S - Nn - 1) // 2) % m   # exact integer reduction
    eN = (Nn + 1) % m
    eS = S % m
    return pow_w(m, e1) * (1 - pow_w(m, eN)) + (1 - pow_w(m, eS))

print("== 1. closed form vs direct profile (synthetic) ==")
ok = True
for (Nn, p, q) in [(35, 5, 7), (143, 11, 13), (391, 17, 23), (899, 29, 31), (3599, 59, 61)]:
    S = p + q
    P1 = profile_poly(Nn, p, q)
    P2 = profile_closed(Nn, S)
    if P1 != P2:
        ok = False
        print(f"  N={Nn}: MISMATCH")
    # zero criterion on synthetic
    for m in range(3, 17):
        w = cmath.exp(2j * math.pi / m)
        val = sum(c * (w ** (e % m)) for e, c in P1.items())
        zero_crit = abs(B_eval(Nn, S, m)) < 1e-9
        zero_val = abs(val) < 1e-9
        if zero_crit != zero_val:
            ok = False
            print(f"  N={Nn} m={m}: criterion mismatch crit={zero_crit} val={zero_val}")
print("  closed form + zero criterion:", "PASS" if ok else "FAIL")

print("\n== 2. RSA-270 value-forced torsion zeros (admissible-class enumeration, prior) ==")
def admissible_r1(m, Nn):
    M6 = 6 * m
    s = set()
    for a in range(5 % 6, M6, 6):
        for b in range(5 % 6, M6, 6):
            if (a * b) % M6 == Nn % M6:
                S = (a + b) % (2 * m)
                if S % 2 == 0:
                    s.add(((S + 2)//2) % m)
    return sorted(s)

valforced = []
for m in range(3, 201):
    ar1 = admissible_r1(m, N)
    r0 = ((N + 3)//2) % m
    vals = {round(2*g_m(m, r0) + 2*g_m(m, r), 9) for r in ar1}
    if len(vals) == 1:
        valforced.append((m, list(vals)[0]))
predicted = sorted([d for d in range(3, 73) if 72 % d == 0 and d % 24 != 0])
print("predicted family (m|72, 24!|m):", predicted)
print("enumerated value-forced m<=200:", [m for m, v in valforced])
print("match:", [m for m, v in valforced] == predicted)

print("\n== 3. forced-lattice towers ==")
for k in range(1, 9):
    mod = 1 << k
    classes = set()
    for a in range(1, mod, 2):
        for b in range(1, mod, 2):
            if (a * b) % mod == N % mod:
                classes.add((a + b) % mod)
    print(f"  2-adic: S mod 2^{k} classes={sorted(classes)} (count={len(classes)})")
for j in range(1, 5):
    mod = 3 ** j
    classes = set()
    for a in range(mod):
        if a % 3 != 2: continue
        for b in range(mod):
            if b % 3 != 2: continue
            if (a * b) % mod == N % mod:
                classes.add((a + b) % mod)
    print(f"  3-adic (prior): S mod 3^{j} classes={sorted(classes)} (count={len(classes)})")

print("\n== 4. bracket closed form at RSA-270 forced class (S=16 mod 72), m sample ==")
for m in (3, 4, 6, 8, 9, 12, 18, 24, 36, 72, 5, 7):
    Srep = 16  # S mod 72 representative
    e1 = ((Srep - N - 1) // 2) % m
    eN = (N + 1) % m
    eS = Srep % m
    w = cmath.exp(2j * math.pi / m)
    B = (w ** e1) * (1 - w ** eN) + (1 - w ** eS)
    print(f"  m={m:2d}: B(w_m) = {B:.2e}  (|B|<1e-12: {abs(B)<1e-12})")
