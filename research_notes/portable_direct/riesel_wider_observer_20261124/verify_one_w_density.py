"""Exact population counting using immutable v13 and v15 branch predicates."""
from math import comb, factorial, prod
from fractions import Fraction
from decimal import Decimal, localcontext

# Each category corresponds to exactly two residues per prime; masks
# record active categories without double counting overlaps.
def count(qs, k, keep, raw=False):
    weights = [1] + [0] * (2**k - 1)
    for q in qs:
        new = [0] * len(weights)
        for mask, w in enumerate(weights):
            new[mask] += (q - 2*k)*w
            for j in range(k):
                new[mask | (1 << j)] += 2*w
        weights = new
    assert sum(weights) == prod(qs)
    return sum(w for m,w in enumerate(weights) if keep(m if raw else m.bit_count()))

def C(qs,k):
    out = sum((-1)**j*comb(k,j)*prod(q-2*j for q in qs) for j in range(k+1))
    assert out == count(qs,k,lambda n:n==k)
    return Fraction(out, prod(qs))

G=(29,43,1429,5419)
K=(92737,649657,77158673929,40388473189,118750098349)
H=(3361,15790321,88959882481)
I=(211,421,86171,106681,122921,152041,664441,1564921,
   7416361,47392381,146919792181,1041815865690181)
B=(193,1153,6337,22253377,38941695937,278452876033)
D=(33975937,138991501037953)
Cfamily=(61681,4562284561,168692292721,469775495062434961)
groups=(G,K,H,I,B,D,Cfamily)
S3=398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
assert len({q for qs in groups for q in qs})==36
from math import gcd
assert all(gcd(S3,q)==1 for qs in groups for q in qs)
for c in range(1,6):
    for q in K:
        phases=(c,c+7,c+14)
        cs={s*pow(2,-(4+6*b),q)%q for b in phases for s in (-1,1)}
        assert len(cs)==6
UM=prod(K)
N=UM-prod(q-2 for q in K)-prod(q-4 for q in K)+prod(q-6 for q in K)
assert N==count(K,3,lambda m:bool(m&4) and bool(m&3),raw=True)
g=Fraction(factorial(4)*2**4,prod(G))
D9_unfiltered = 5*g*Fraction(N,UM)
D9= g*Fraction(N,UM)*(1-C(B,2))*(1-C(D,2))*(1-C(Cfamily,3))*(1-C(H,2))*(5-2*C(I,2))
D8_overlap=D9_unfiltered-D9
with localcontext() as ctx:
    ctx.prec=55
    for label,x in [('K hits mandatory class and at least one optional class', Fraction(N,UM)),('classified one-W geometry exists', D9_unfiltered),('exact nine and one-W dictionary exists',D9),('classified geometry overlap with budget-eight',D8_overlap)]:
        print(label)
        print(x)
        print(Decimal(x.numerator)/Decimal(x.denominator))
