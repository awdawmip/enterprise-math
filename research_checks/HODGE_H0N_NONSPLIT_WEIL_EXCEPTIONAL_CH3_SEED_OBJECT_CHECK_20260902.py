#!/usr/bin/env python3
"""Task-local exact certificate for HODGE H0N exceptional-ch3 no-go.

This checker verifies only finite/symbolic reductions used by the written proof:
- the mod-3 norm obstruction certificate;
- the exact K=Q(i) H^6 eigenvalue blocks for u=1+2i;
- the rational spectral projector onto the p=0,6 exceptional Weil blocks;
- the rank-symbolic degree-three Chern-character identity.

It is not a substitute for Mukai's semihomogeneous-bundle theorem, the Hodge
decomposition argument, or any unbounded algebraic-geometric theorem.
"""
from fractions import Fraction

CHECKS = 0
FAILURES = []

def check(label, cond):
    global CHECKS
    CHECKS += 1
    if not cond:
        FAILURES.append(label)

def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])

def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def gscale(q, z):
    return (q * z[0], q * z[1])

def gpow(z, n):
    out = (1, 0)
    for _ in range(n):
        out = gmul(out, z)
    return out

def qpair(z):
    return (Fraction(z[0]), Fraction(z[1]))

def qadd(z, w):
    return (z[0] + w[0], z[1] + w[1])

def qmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def qscale(q, z):
    q = Fraction(q)
    return (q * z[0], q * z[1])

def qsub_scalar(z, a):
    return (z[0] - Fraction(a), z[1])

def qlin(z, a, b):
    # a*z+b
    return (Fraction(a) * z[0] + Fraction(b), Fraction(a) * z[1])

def qquad(z, a, b):
    # z^2 + a*z + b
    z2 = qmul(z, z)
    return (z2[0] + Fraction(a) * z[0] + Fraction(b),
            z2[1] + Fraction(a) * z[1])

def projector(z):
    # P(t)=-(t-125)(9881t-609029)(t^2+70t+15625)
    #       (t^2+150t+15625) / 57000000000000000.
    factors = [
        qsub_scalar(z, 125),
        qlin(z, 9881, -609029),
        qquad(z, 70, 15625),
        qquad(z, 150, 15625),
    ]
    out = (Fraction(1), Fraction(0))
    for f in factors:
        out = qmul(out, f)
    return qscale(Fraction(-1, 57000000000000000), out)

# 1. [-3] differs from split [-1] because 3 is not a Q(i)-norm.
# After clearing denominators x^2+y^2=3z^2. Mod 3, the only
# solution to x^2+y^2=0 is x=y=0, forcing infinite descent.
zero_pairs = [(x, y) for x in range(3) for y in range(3)
              if (x*x + y*y) % 3 == 0]
check("mod3_sum_two_squares_zero_only_origin", zero_pairs == [(0, 0)])

# 2. Exact H^6 K-weight eigenvalues for u=1+2i.
u = (1, 2)
ubar = (1, -2)
lambdas = [gmul(gpow(u, p), gpow(ubar, 6-p)) for p in range(7)]
expected = [
    (117, -44), (-35, 120), (-75, -100), (125, 0),
    (-75, 100), (-35, -120), (117, 44),
]
check("h6_block_eigenvalues", lambdas == expected)

# Rational minimal factors for conjugate block pairs p=0/6,1/5,2/4 and p=3.
# All conjugate-pair products are Norm(u)^6=5^6=15625.
def pair_factor(z, tr, norm):
    # z^2-tr*z+norm
    z2 = gmul(z, z)
    return (z2[0] - tr*z[0] + norm, z2[1] - tr*z[1])

for p in (0, 6):
    check(f"F0_root_p{p}", pair_factor(lambdas[p], 234, 15625) == (0, 0))
for p in (1, 5):
    check(f"F1_root_p{p}", pair_factor(lambdas[p], -70, 15625) == (0, 0))
for p in (2, 4):
    check(f"F2_root_p{p}", pair_factor(lambdas[p], -150, 15625) == (0, 0))
check("F3_root_p3", lambdas[3] == (125, 0))

# 3. P is exactly 1 on W_K blocks p=0,6 and 0 on p=1,...,5.
projector_values = [projector(qpair(z)) for z in lambdas]
for p, value in enumerate(projector_values):
    want = (Fraction(1), Fraction(0)) if p in (0, 6) else (Fraction(0), Fraction(0))
    check(f"projector_value_p{p}", value == want)

# It therefore kills the divisor-generated theta^3 block p=3.
check("projector_kills_theta3", projector((Fraction(125), Fraction(0))) ==
      (Fraction(0), Fraction(0)))

# On W_K the polynomial t^2-234t+15625 has negative non-square rational
# discriminant -7744=-88^2, hence no rational eigenvalue. Any nonzero rational
# vector w has {w,u^*w} Q-linearly independent and spans the 2D W_K.
discriminant = 234*234 - 4*15625
check("WK_minpoly_discriminant", discriminant == -7744)
check("WK_minpoly_no_rational_root", discriminant < 0)

# 4. Rank-symbolic degree-three Chern-character identity.
# Mukai gives c(E)=(1+c1/r)^r. Newton's formula gives
# 6 ch_3/c1^3 = 1 - 3(r-1)/(2r) + (r-1)(r-2)/(2r^2) = 1/r^2.
# Clearing 2r^2 leaves the polynomial identity
# 2r^2 - 3r(r-1) + (r-1)(r-2) - 2 == 0.
r2_coeff = 2 - 3 + 1
r1_coeff = 3 - 3
r0_coeff = 2 - 2
check("semihomogeneous_ch3_symbolic_identity",
      (r2_coeff, r1_coeff, r0_coeff) == (0, 0, 0))

print(f"HODGE_H0N_CHECKS={CHECKS}")
print(f"HODGE_H0N_FAILURES={len(FAILURES)}")
if FAILURES:
    for item in FAILURES:
        print(f"FAIL: {item}")
    raise SystemExit(1)
print("HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK: PASS")
