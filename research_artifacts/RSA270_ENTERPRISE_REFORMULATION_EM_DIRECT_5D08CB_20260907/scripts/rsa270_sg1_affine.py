"""
SG1 corrected: W'_s(w_m) is AFFINE in s, not periodic in s mod m.
  W'_s(w) = s * A_m(r) + B_m(r),  r = s mod m   (A_m, B_m periodic, exact in Q(zeta_m))
Implication: P'(w_m) = 2[s1 A(r0)+B(r0)] + 2[s2 A(r1)+B(r1)], s2=(S+2)/2:
  the derivative ladder is LINEAR in S (factoring-equivalent information), unlike the
  value ladder which is periodic (S mod 2m). Observability is the only wall.
Verify: periodicity of W'_s - s*A_m(r); affine law on synthetic semiprimes;
A_m(r)!=0 prevalence.
"""
import math, cmath

def Wp_s(s, u):
    return sum((2 - s + 2*j) * u ** (2 - s + 2*j - 1) for j in range(s - 1))

def Wp_formula(m, s):
    w = cmath.exp(2j * math.pi / m)
    return ((2 - s) * w ** (1 - s) - s * w ** (s - 1)) / (1 - w * w) \
         + 2 * w * (w ** (2 - s) - w ** s) / ((1 - w * w) ** 2)

print("== A. affine law W'_s(w) = s*A_m(r) + B_m(r), r = s mod m ==")
ok = True
for m in range(3, 13):
    w = cmath.exp(2j * math.pi / m)
    A = {}; B = {}
    for r in range(m):
        s1, s2 = r + m, r + 2 * m
        v1, v2 = Wp_formula(m, s1), Wp_formula(m, s2)
        A[r] = (v2 - v1) / m
        B[r] = v1 - s1 * A[r]
    # verify for s up to 60
    for s in range(2, 61):
        r = s % m
        pred = s * A[r] + B[r]
        if abs(Wp_formula(m, s) - pred) > 1e-9:
            ok = False
            print(f"  AFFINE FAIL m={m} s={s}")
    nz = sum(1 for r in range(m) if abs(A[r]) > 1e-9)
    print(f"  m={m:2d}: affine law holds; A_m(r) nonzero on {nz}/{m} residues")
print("  affine law:", "PASS" if ok else "FAIL")

print("\n== B. synthetic: P'(w_m) = 2[s1 A(r0)+B(r0)] + 2[s2 A(r1)+B(r1)] ==")
def AB(m):
    A = {}; B = {}
    for r in range(m):
        s1, s2 = r + m, r + 2 * m
        v1, v2 = Wp_formula(m, s1), Wp_formula(m, s2)
        A[r] = (v2 - v1) / m
        B[r] = v1 - s1 * A[r]
    return A, B

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
    s1 = (Nn + 3)//2; s2 = (S + 2)//2
    for m in range(3, 17):
        w = cmath.exp(2j * math.pi / m)
        lhs = sum(c * e * (w ** ((e - 1) % m)) for e, c in P.items())
        A, B = AB(m)
        r0, r1 = s1 % m, s2 % m
        rhs = 2 * (s1 * A[r0] + B[r0]) + 2 * (s2 * A[r1] + B[r1])
        if abs(lhs - rhs) > 1e-8:
            ok = False
            print(f"  FAIL N={Nn} m={m}: {lhs} vs {rhs}")
print("  P' affine identity:", "PASS (5 semiprimes, m=3..16)" if ok else "FAIL")

print("\n== C. S-linearity consequence ==")
print("  Given r1 (from the value ladder) and the derivative value P'(w_m) at any m with A_m(r1)!=0:")
print("  S+2 = (P'(w_m) - 2[s1 A(r0)+B(r0)] - 2 B(r1)) / A(r1)   ->  S recovered EXACTLY (one scalar equation).")
print("  => derivative ladder is factoring-equivalent in information; the wall is observability of P'(w_m) from N alone.")
