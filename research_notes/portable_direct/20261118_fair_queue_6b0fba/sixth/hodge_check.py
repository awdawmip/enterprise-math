"""Independent exact checks for the 32 Weil graph sheaves. Python 3, SymPy."""
from collections import Counter
from itertools import product
from math import comb
import sympy as S

i = S.I
u = 1+2*i
roots = [S.expand(u**p*S.conjugate(u)**(6-p)) for p in range(7)]
target = [1,0,0,0,0,0,1]
norm = 5**6
X = S.symbols("X")
projector = -(X+35)*(X+75)*(X-125)/233472
old = -(X-125)*(9881*X-609029)*(X**2+70*X+15625)*(X**2+150*X+15625)/57000000000000000
for p,r in enumerate(roots):
    assert S.expand(old.subs(X,r)) == target[p]
    assert projector.subs(X,S.re(r)) == target[p]
moments = [int(S.expand_complex(abs(u**n-S.conjugate(u)**n)**6)) for n in range(4)]
assert moments == [0,4096,262144,4096]
Delta = moments[3]-30*moments[2]+2375*moments[1]-1781250*moments[0]
assert Delta == 1867776
print("four moments, detector:", moments, Delta)

positive = [a for a in product(range(4),repeat=3) if sum(a)%4 == 0]
negative = [a for a in product(range(4),repeat=3) if sum(a)%4 == 2]
assert len(positive)==len(negative)==16
for exponents in product((-1,0,1),repeat=3):
    pos = sum(i**(sum(k*j for k,j in zip(exponents,a))%4) for a in positive)
    neg = sum(i**(sum(k*j for k,j in zip(exponents,a))%4) for a in negative)
    if len(set(exponents)) == 1:
        assert pos == 16 and neg == (-16 if exponents[0] else 16)
    else:
        assert pos == neg == 0

squared_distance = (0,2,4,2)
def distances(a,b):
    return [squared_distance[(ak-bk)%4] for ak,bk in zip(a,b)]

counts = Counter()
ext = [0]*7
for a,b in product(positive,negative):
    ds = [d for d in distances(a,b) if d]
    k = len(ds)
    counts[k]+=1
    for j in range(2*(3-k)+1):
        ext[k+j] += int(S.prod(ds))*comb(2*(3-k),j)
assert counts == {1:48,2:96,3:112} and ext == [0,192,1152,4480,1152,192,0]
graphs = positive+negative
sign = lambda a: 1 if sum(a)%4==0 else -1
square = sum(sign(a)*sign(b)*S.prod(distances(a,b)) for a,b in product(graphs,repeat=2))
assert square == -2048 and S.Rational(square,32**2) == -2
print("signed square; unequal count; Ext:", square, dict(counts), ext)

def normal_rows(a):
    # delta_a(B) = D^{-1} B^T - diag(a) B diag(conjugate(a)).
    rows = S.zeros(9,9)
    for j,k in product(range(3),repeat=2):
        rows[3*j+k,3*k+j] += S.Rational(1,(1,1,3)[j])
        rows[3*j+k,3*j+k] -= i**((a[j]-a[k])%4)
    return rows

def kernel(graphs):
    return S.Matrix.vstack(*(normal_rows(a) for a in graphs)).nullspace()

units = S.eye(9)
diagonal = normal_rows((0,0,0))
assert diagonal.rank() == 6
assert all(diagonal*v == S.zeros(9,1) for v in (units.col(0),units.col(4),units.col(1)+units.col(3)))
for a in graphs:
    assert normal_rows(a).rank() == 6
for selected in (positive,negative,graphs):
    assert kernel(selected) == [units.col(0),units.col(4)]
print("individual normal rank 6, both groups and all graphs have common rank 7")

# Independently test the infinitesimal Hodge locus, without using normal kernels.
# Slots: dz[0:3], dw[3:6], dbar(z)[6:9], dbar(w)[9:12].
def term(indices, scale=1):
    if len(set(indices)) != len(indices):
        return {}
    inv = sum(j>k for h,j in enumerate(indices) for k in indices[h+1:])
    return {tuple(sorted(indices)): (-1)**inv*scale}

def variation(terms, j, k):
    result = Counter()
    for component in terms:
        for p,slot in enumerate(component):
            if slot == j:
                result.update(term(component[:p]+(9+k,)+component[p+1:]))
            if slot == k+3:
                result.update(term(component[:p]+(6+j,)+component[p+1:], S.Rational(1,(1,1,3)[k])))
    return result

q_terms = [tuple(u for j,h in enumerate(choice) for u in (3*h+j,6+3*h+j))
           for choice in product((0,1),repeat=3)]
columns = [variation(q_terms,j,k) for j,k in product(range(3),repeat=2)]
keys = sorted(set().union(*(c.keys() for c in columns)))
period = S.Matrix([[c[key] for c in columns] for key in keys])
assert period.nullspace() == [units.col(0),units.col(4)]
for j,k in product(range(3),repeat=2):
    for pure in [(0,1,2,9,10,11),(6,7,8,3,4,5)]:
        assert all(v==0 for v in variation([pure],j,k).values())
print("Hodge variation of q1*q2*q3 has independent rank", period.rank(),
      "; both pure Weil lines have zero variation to (2,4)")
