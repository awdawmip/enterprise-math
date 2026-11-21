"""EC49FVD — exact Fraction checks for 7/13 denominator and coupled-prime certificates."""
from fractions import Fraction as Q
from math import gcd

BETA = Q(3, 637)
GAMMA = Q(141024, 1653649)
U = Q(4822040484, 8132285009)

def valuation(z, p):
    assert z != 0
    n, d = abs(z.numerator), z.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v

def valuation_pair(x, p):
    t0 = (1-x) * (1-BETA*x)
    te = (1-x) * (1+GAMMA*x)
    a = x*(640-3*x)/637
    b = 1-U*te
    R = t0/(U*te)
    S = b*R/a
    assert 0 < a < b < 1 and 1 < R < S
    return valuation(R, p), valuation(S, p)

def impossible(vr, vs):
    return ((vr == 0) != (vs == 0)
        or vr*vs < 0
        or (vr*vs > 0 and abs(vr) >= abs(vs)))

# Exhaust every reduced fraction in the stated finite range with p | denominator.
counts = {7: 0, 13: 0}
for d in range(2, 351):
    for m in range(1, d):
        if gcd(m, d) != 1:
            continue
        x = Q(m, d)
        for p in counts:
            if d % p == 0:
                pair = valuation_pair(x, p)
                assert impossible(*pair), (str(x), p, pair)
                counts[p] += 1
assert counts == {7: 4758, 13: 2568}
print("DENOMINATOR_CERTIFICATE_PASS", counts)

# The exact old two-prime survivor, and the single higher lift.
assert 637 == 7**2 * 13
root7 = 640 * pow(3, -1, 2401) % 2401
root13 = 640 * pow(3, -1, 169) % 169
assert root7 == 1814 and root13 == 157
residue = (root7 + 2401 *
    ((root13 - root7) * pow(2401, -1, 169) % 169)) % (2401*169)
assert residue == 270726 and residue % 343 == 99 and residue % 169 == 157
assert (2401 - 343) * (169 - 13) == 321048
print("CRT_LIFT_PASS", residue, "mod", 405769, "certified", 321047, "/", 321048)

# A width which survives both individual 7- and 13-adic exceptional tests
# and the preceding five-prime coarse CRT filter, but not their coupling.
M = 8132285009
N = 3 * 8 * M
m0 = 56925995064
k = ((38858-m0) * pow(N, -1, 57967)) % 57967
m, d = m0 + k*N, 1 + N*57967
assert (m,d) == (9422903036783328,11313699962800873)
assert gcd(m,d)==1 and 0<m<d and m%N==m0 and d%N==1
x = Q(m,d)
assert (m*pow(d,-1,57967))%57967 == 38858
assert (m*pow(d,-1,343))%343 == 99
assert (m*pow(d,-1,169))%169 == 157
a = x*(640-3*x)/637
assert (valuation(a,7),valuation(a,13)) == (1,1)
assert valuation_pair(x,7) == (-2,-3)
assert valuation_pair(x,13) == (-1,-2)
print("EXCEPTIONAL_JOINT_WITNESS_PASS", x,
      valuation_pair(x,7), valuation_pair(x,13))
