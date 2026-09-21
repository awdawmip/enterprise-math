from fractions import Fraction as F


def rk4_affine(y, a, b, h):
    f = lambda x: a * x + b
    k1 = f(y)
    k2 = f(y + h * k1 / 2)
    k3 = f(y + h * k2 / 2)
    k4 = f(y + h * k3)
    return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


# Exact support-shrink counterexample for a transverse Fourier mode pair.
k = (F(1), F(0), F(0))
u = (F(0), F(1), F(0))
src = (F(0), F(-3, 5), F(0))
dot = lambda x, y: sum(a * b for a, b in zip(x, y))
assert dot(k, u) == 0 and dot(k, src) == 0
assert dot(u, k) == 0 and dot(u, tuple(-x for x in k)) == 0

y0 = F(1)
a = F(-1)
b = F(-3, 5)
h = F(1)
y1 = rk4_affine(y0, a, b, h)
assert y1 == 0

# Closed-form RK4 coefficients give an independent exact cross-check.
z = a * h
R = 1 + z + z * z / 2 + z**3 / 6 + z**4 / 24
Psi = 1 + z / 2 + z * z / 6 + z**3 / 24
assert R == F(3, 8) and Psi == F(5, 8)
assert R * y0 + h * Psi * b == 0

# Future-only latch regret identity. Dynamic continues guarding K future calls,
# executing sparse on m of them; latch uses dense unconditionally.
identity_cases = 0
for K in range(1, 9):
    for m in range(K + 1):
        for D in range(1, 9):
            for S in range(D + 1):
                for G in range(0, 5):
                    for L in range(0, 5):
                        dynamic = K * G + m * S + (K - m) * D
                        latch = K * D + L
                        regret = latch - dynamic
                        assert regret == m * (D - S) - K * G + L
                        identity_cases += 1

# If future sparse opportunities <= M, each saving <= U, future guards >= H,
# and latch switching overhead is L, regret <= M*U-H+L.
bound_cases = 0
for M in range(0, 7):
    for U in range(0, 7):
        for H in range(0, 13):
            for L in range(0, 5):
                for m in range(0, M + 1):
                    for saving in range(0, U + 1):
                        regret = m * saving - H + L
                        assert regret <= M * U - H + L
                        if M * U + L <= H:
                            assert regret <= 0
                        bound_cases += 1

print(
    {
        "rk4_y1": str(y1),
        "R_minus_1": str(R),
        "Psi_minus_1": str(Psi),
        "source_ratio": str(b),
        "identity_cases": identity_cases,
        "bound_cases": bound_cases,
        "status": "PASS",
    }
)
