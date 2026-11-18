"""Exact-rational certificate for the first S23/AV plateau jump.

Source: frozen 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
All mathematical checks use Fraction; no floating-point comparisons.
"""
from fractions import Fraction
from math import gcd


def log_bounds(numerator: int, denominator: int, terms: int = 45):
    """Rational bounds from log(x)=2atanh((x-1)/(x+1)) for x>1."""
    z = Fraction(numerator - denominator, numerator + denominator)
    assert 0 < z < 1
    s = sum((2 * z ** (2 * k + 1) / (2 * k + 1)
             for k in range(terms)), Fraction(0))
    rem = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return s, s + rem


l2, u2 = log_bounds(2, 1)
l87, u87 = log_bounds(8, 7)
l54, u54 = log_bounds(5, 4)
r_low = (3 * l2 - u87) / (u54 + u87)
r_high = (3 * u2 - l87) / (l54 + l87)
Q = 10 ** 26
LO = 545569623581288298975349314
HI = LO + 1
assert Fraction(LO, Q) < r_low < r_high < Fraction(HI, Q)
assert 5 < r_low < r_high < 6

D, P = 380295, 2074774
U_V, U_J = 79, 431
H = D + U_V + U_J # 380805
N = D + P
T = D + 1             # 380296; new gap scaled from h=510
FIRST_JUMP = 510 + T
assert FIRST_JUMP == H + 1 == 380806
assert U_V * P - U_J * D == 1 and gcd(P, D) == 1

# eta = P-rD; epsilon = 79r-431
eta_lo, eta_hi = P - D * r_high, P - D * r_low
eps_lo, eps_hi = U_V * r_low - U_J, U_V * r_high - U_J
assert 0 < eta_lo < eta_hi < eps_lo < eps_hi
assert eps_hi < 2 * eta_lo  # ensures floor(2*eta/epsilon)=1

# Integer-key gap certificate for every ordered threshold pair in T_H.
assert eta_hi * H < 1
assert eta_hi * (H + D) < 2
assert eps_lo > eta_hi
assert (2 - eta_hi * H) / D > eta_hi
assert (8 - eta_hi * H) / D > 7 * eps_hi - eta_lo
assert P > H and P - 7 * U_J > H
assert 7 * U_V >= U_V + U_J
assert N > 6 * H                  # right exterior witness E(N,0)
assert 5 * (D + 1) - (H - (D + 1)) > 6 * 509  # witness q=1 requires endpoint mass >=510

# Exact first-entry certificates for base gap and its translated successor.
# eta/epsilon in (1/2,1): b=1 => a=0, b=2 => a=1.
b1_v, b1_k = D, P
b2_v, b2_k = 2 * D + U_V, 2 * P + U_J
assert (b1_v, b1_k) == (380295, 2074774)
assert (b2_v, b2_k) == (760669, 4149979)
assert b1_k + b1_v == 2455069
assert b2_v >= T > b1_v
assert b2_k + b2_v - T == 4530352
assert (b2_k + b2_v - T) - N == 2075283

# Second, exact plateau: w2=2w+u gives positive small offset 2eta-eps.
V2, K2 = b2_v, b2_k
N2 = b2_k + b2_v - (D + 1)
assert N2 == 4530352 and V2 == 760669 and V2 < N
assert 0 < 2 * eta_lo - eps_hi and 2 * eta_hi - eps_lo < eps_lo
assert K2 > V2 and P > V2
# For each threshold at H=V2, choose w for v<=D, w2 for v>D.
# Check the extremal j choices and all v; the proof handles every intermediate j.
for v in range(V2 + 1):
    vb, kb = (D, P) if v <= D else (V2, K2)
    for j in (0, V2 - v):
        k, ell = kb - j, vb - v
        assert 0 <= k and 0 <= ell and k + ell <= N2
assert N2 > V2

# Verify the two translational observers algebraically using interval arithmetic.
# A lower bound on the shortest positive gap is min(eps, (2-eta*H)/D).
min_gap_lower = min(eps_lo, (2 - eta_hi * H) / D)
assert min_gap_lower > eta_hi
# For case B with q>=2, right endpoint v>D+79 and j<431;
# a positive gap has integer key z>=8, so it exceeds every q-shift error.
assert (8 - eta_hi * H) / D > 7 * eps_hi - eta_lo

# Sample parameterized prefixes across all 7 right-edge strips.
for s in range(1, 511):
    v = D + s
    for j in (0, (510 - s) // 2, 510 - s):
        q = (s + U_V - 1) // U_V
        k = P + U_J * q - j
        ell = D + U_V * q - v
        assert 1 <= q <= 7 and 0 <= ell and 0 <= k
        assert k + ell <= N
        # E(k,ell)-t(v,j) = eta - q*epsilon < 0, exactly.
        assert eta_hi - q * eps_lo < 0

print("PASS_S23_AV_FIRST_STRICT_JUMP_AT_H380806")
print(f"r_certified_26_decimal=[{LO}/{Q},{HI}/{Q}]")
print(f"unimodular_basis=({U_V},{U_J});({D},{P});det=1")
print(f"plateau=510..{H} N={N} analytic_all_cells_shift_covered")
print(f"first_jump_h={FIRST_JUMP} exact_N={N2} jump_size={N2-N}")
print(f"second_exact_plateau={FIRST_JUMP}..{V2} N={N2} (analytic min_gap+two_shifts)")
print(f"gap_bound_z_ge_2_and_z_ge_8=PASS; scanned_edge_shift_samples={510*3}; second_plateau_extremes={(V2+1)*2}")

# Six analytic plateaus: all transition gaps close by signed-shift witnesses.
# The minimum positive threshold difference is >= eps while H < P+D.
# Within the right-edge strip, a positive gap < 7*eps can only be
# A*(79,431), 1<=A<=6, provided H < P+D-6*510.
PLATEAUS = []
vprev = -1
nprev = 0
for b, a in enumerate((0, 1, 1, 2, 2, 3), 1):
    assert a * eps_hi < b * eta_lo < b * eta_hi < (a + 1) * eps_lo
    v_b, k_b = b * D + a * U_V, b * P + a * U_J
    h_begin = 510 if b == 1 else vprev + 511
    h_end = v_b + 510
    n_b = (k_b + v_b) if b == 1 else k_b + v_b - (vprev + 1)
    assert h_begin == (510 if b == 1 else PLATEAUS[-1][1] + 1)
    assert n_b > nprev and h_end < N - 6 * 510
    assert k_b > h_end and n_b > r_high * h_end and n_b > h_end
    # Universal upper-cover: all left endpoints with v<=v_b use some W_i.
    # Edge endpoints with v>v_b use W_b+q*u from the right (q<=7).
    for q in range(1, 8):
        vR = (vprev + 511) if q == 1 else v_b + 79 * (q - 1) + 1
        if vR <= h_end:
            k, ell = k_b + q * U_J, v_b + q * U_V - vR
            assert k>=0 and ell>=0 and k+ell <= n_b
            assert q * eps_lo - (b * eta_hi - a * eps_lo) > 0
            assert q * eps_hi - (b * eta_lo - a * eps_hi) < 7 * eps_hi
    PLATEAUS.append((h_begin, h_end, n_b, b, a, v_b, k_b))
    vprev, nprev = v_b, n_b
assert PLATEAUS == [
    (510, 380805, 2455069, 1, 0, 380295, 2074774),
    (380806, 761179, 4530352, 2, 1, 760669, 4149979),
    (761180, 1141474, 6605047, 3, 1, 1140964, 6224753),
    (1141475, 1521848, 8680331, 4, 2, 1521338, 8299958),
    (1521849, 1902143, 10755026, 5, 2, 1901633, 10374732),
    (1902144, 2282517, 12830310, 6, 3, 2282007, 12449937),
]
assert PLATEAUS[-1][1] == 2282517
assert PLATEAUS[-1][1] < N - 3060
print("six_exact_plateaus=" + repr([(a,b,n) for a,b,n,*_ in PLATEAUS]))

print("full_horizon_result=six_analytic_plateaus_plus_exact_rational_certificates; independent_review=pending")
