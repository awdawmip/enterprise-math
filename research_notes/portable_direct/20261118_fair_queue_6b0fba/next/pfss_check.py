"""Count only the published X=100000 PFSS carrier and its synthetic nulls."""
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt

def prime(n):
    return n >= 2 and all(n % q for q in range(2, isqrt(n) + 1))

X, U = 100000, 101000
rows = {p: set(range(max(p, X//p + 1), U//p + 1))
        for p in range(2, isqrt(U)+1) if prime(p)}
addresses = set().union(*rows.values())
layer = {q for q in addresses if q % 30 == 29}
inside = layer & rows[2]
assert (len(rows), len(addresses), len(layer), sum(map(prime, layer)), len(inside)) == (66,2016,69,29,17)
assert {p for p, row in rows.items() if 419 in row} == {239,241}
a, b = (50009,50039,50069), (419,33359,33389)
assert set(a) <= inside and set(b) <= layer-inside

delta = [0] * 18
for picks in product(range(2), repeat=3):
    h = sum(picks)
    for j in range(15):
        delta[h+j] += (-1)**(3-h)*comb(14,j)*comb(49,26-j)
moments = [sum(weight * comb(c, k) for c,weight in enumerate(delta) if c>=k) for k in range(4)]
assert moments == [0,0,0,comb(63,26)]
assert F(delta[0],comb(69,29)) == -F(135198,54966990749)
assert F(moments[3],comb(69,29)) == F(34713,2305336)
for law in [{0:F(5,92),7:F(29,69),8:F(145,276)}, {1:F(5,69),7:F(8,23),8:F(40,69)}]:
    def mean(f):
        return sum(prob*f(c) for c,prob in law.items())
    assert (mean(lambda x:1),mean(lambda x:x),mean(lambda x:x*x)) == (1,F(493,69),F(1247,23))
    for expected, denom in [(lambda c:c*(c-1),17*16), (lambda c:c*(29-c),17*52),
                            (lambda c:(29-c)*(28-c),52*51)]:
        assert mean(expected)/denom == F(29*28,69*68)
print(len(addresses), len(layer), len(inside), moments, 'sharp range:', F(0), F(5,92))
