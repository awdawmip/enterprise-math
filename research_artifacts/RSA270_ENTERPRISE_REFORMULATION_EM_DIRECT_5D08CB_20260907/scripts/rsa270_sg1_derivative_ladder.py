"""
SG1: derivative ladder at torsion points (EM-DIRECT-5D08CB / DIRECT-RSA270).
W'_s(u) closed form at u=w_m (m>=3):
  W'_s(w) = [(2-s)w^(1-s) - s w^(s-1)]/(1-w^2) + 2w(w^(2-s) - w^s)/(1-w^2)^2
  =: h_m(s mod m).
Test: fiber structure of r -> h_m(r); whether h_m resolves MORE S-classes per m than g_m
(e.g. the even-m sign ambiguity of g_m); and verification on synthetic semiprimes.
"""
import math, cmath

def W_s(s, u):
    return sum(u ** (2 - s + 2*j) for j in range(s - 1))

def Wp_s(s, u):
    return sum((2 - s + 2*j) * u ** (2 - s + 2*j - 1) for j in range(s - 1))

def h_m(m, r):
    w = cmath.exp(2j * math.pi / m)
    r %= m
    return ((2 - r) * w ** (1 - r) - r * w ** (r - 1)) / (1 - w * w) \
         + 2 * w * (w ** (2 - r) - w ** r) / ((1 - w * w) ** 2)

def g_m(m, r):
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

print("== A. h_m closed form vs direct W'_s (s up to 40, m=3..16) ==")
ok = True
for m in range(3, 17):
    w = cmath.exp(2j * math.pi / m)
    for s in range(2, 41):
        a = Wp_s(s, w)
        b = h_m(m, s % m)
        if abs(a - b) > 1e-9:
            ok = False
            print(f"  MISMATCH m={m} s={s}: {a} vs {b}")
print("  closed form:", "PASS" if ok else "FAIL")

print("\n== B. h_m fiber structure (does the derivative resolve the even-m sign ambiguity?) ==")
for m in range(3, 17):
    vals = {}
    for r in range(m):
        v = round(complex(h_m(m, r)).real, 9) + 1j * round(complex(h_m(m, r)).imag, 9)
        vals.setdefault(v, []).append(r)
    fibers = [g for g in vals.values() if len(g) > 1]
    # even m: g_m fiber pairs {r, 2+m/2-r}; check whether h_m separates them
    if m % 2 == 0:
        separated = all(h_m(m, r) != h_m(m, (2 + m//2 - r) % m) for r in range(m)
                        if (r != (2 + m//2 - r) % m))
        print(f"  m={m:2d}: multi-fibers={len(fibers)}  h_m separates g_m-pairs: {separated}")
    else:
        injective = len(fibers) == 0
        print(f"  m={m:2d}: injective: {injective}  multi-fibers={len(fibers)}")

print("\n== C. synthetic verification: P'(w_m) = 2h_m(r0) + 2h_m(r1) ==")
def profile_poly(Nn, p, q):
    S = p + q
    P = {}
    for s, mult in [((Nn + 3)//2, 2), ((S + 2)//2, 2)]:
        for j in range(s - 1):
            e = 2 - s + 2*j
            P[e] = P.get(e, 0) + mult
    return P
ok = True
for (Nn, p, q) in [(35, 5, 7), (143, 11, 13), (391, 17, 23), (899, 29, 31), (3599, 59, 61)]:
    S = p + q
    P = profile_poly(Nn, p, q)
    for m in range(3, 17):
        w = cmath.exp(2j * math.pi / m)
        lhs = sum(c * e * (w ** ((e - 1) % m)) for e, c in P.items())
        r0 = ((Nn + 3)//2) % m
        r1 = ((S + 2)//2) % m
        rhs = 2 * h_m(m, r0) + 2 * h_m(m, r1)
        if abs(lhs - rhs) > 1e-9:
            ok = False
            print(f"  MISMATCH N={Nn} m={m}: {lhs} vs {rhs}")
print("  P'(w_m) identity:", "PASS (5 semiprimes, m=3..16)" if ok else "FAIL")
