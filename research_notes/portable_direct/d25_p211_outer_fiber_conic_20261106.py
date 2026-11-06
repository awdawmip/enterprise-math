"""D25 p=211 outer-source conic: finite-field proof certificate / independent direct readout.

Runs in the same folder as d25_p211_second_digit_certificate_20261106.py.
This is author-side exact computation, not native Source acceptance.
"""
from d25_p211_second_digit_certificate_20261106 import (
    P, source_jets, direct_weighted_source
)

assert P == 211
_, A, _ = source_jets(P**2)
_, T, H = source_jets(P, True)
assert A == [28696, 10279, 42622]
assert T == [0, 151, 0]
assert H == [[22, 170, 29], [170, 4, 71], [29, 71, 182]]

v = (-pow(3, -1, P), -pow(2, -1, P), -2*pow(3, -1, P))
Lx = (A[0]//P + sum(v[k]*H[k][0] for k in range(3))) % P
Ly = (A[2]//P + sum(v[k]*H[k][2] for k in range(3))) % P
assert (Lx, Ly) == (165, 141)

def Q(x, y):
    return (11*x*x + 29*x*y + 91*y*y + Lx*x + Ly*y) % P

assert (29**2-4*11*91) % P == 2
assert pow(2, (P-1)//2, P) == P-1
zeros = [(x, y) for x in range(P) for y in range(P) if Q(x, y) == 0]
assert len(zeros) == 212
assert sum(x != 0 and y != 0 for x,y in zeros) == 209
base = direct_weighted_source((0,0,0))
assert base == P
for x,y in zeros:
    assert direct_weighted_source((x,0,y)) == base, (x,y)
for x,y in [(0,1),(1,0),(1,1),(1,53),(0,17),(5,1),(210,210),(74,39)]:
    delta = (direct_weighted_source((x,0,y)) - base) % (P**3)
    assert delta == P**2 * Q(x,y), (x,y,delta,Q(x,y))
assert Q(1,53)==0
assert (35 + 53*123) % P == 13
print("PASS P=211; Q zeros=212, nonzero=211, both nonzero=209")
print("Example (1,53): full weighted sum mod p^3 stays 211; local j=1 coefficient changes by 211*13 mod p^2")
