# Six-label triple observer: exact integral repair and symmetry orbits

Date: 2026-11-07 (Asia/Taipei). Status: **AUTHOR_UNREVIEWED / NOT_ADMITTED**.
Provenance: new auxiliary calculation in the present RESEARCH_DRIVER automation run, extending the conversation's r59 certificate `em_triads_full_observer_certificate_r59.py`. Shared source context is disclosed. No independent Driver review, native Result, current Driver authority, or Working Truth is asserted. The task-scoped scientific pins and prior contributor history are unchanged.

## Exact auxiliary theorem

Let `V={1,...,6}`, `T=binom(V,3)` (20 triples), and `P=binom(V,2)` (15 pairs).
Define the integer pair-incidence map `W: Z^T -> Z^P` by
`(Wx)_e = sum_{t contains e} x_t`. For `Q subset T` let `E_Q x` be the
chosen triple-coordinate values.

1. `rank_Q W=15`, `rank_Z ker(W)=5`, and the Smith invariant factors of
   `W` are ten 1's, four 2's and one 6. Thus `W(Z^20)` has index 96 in
   `Z^15`.
2. Among all `binom(20,5)=15504` five-coordinate query sets, exactly
   5184 make `x |-> (Wx,E_Q x)` injective on `Z^20`. For each such
   `Q`, the augmented 20x20 integer matrix `[W;E_Q]` has determinant
   `+96` or `-96`; for the other 10320 sets it has determinant zero.
   Hence five integer-valued triple-coordinate queries suffice to recover
   any **feasible** integer-weighted triple state from its pair counts.
3. Five coordinate queries are necessary on the space of all nonnegative
   integral triple weights: with fewer than five, the joint map has a
   nonzero integral kernel vector `z`; the coordinatewise positive and
   negative parts of `z` are distinct nonnegative integer states with the
   same pair counts and queried coordinates.
4. The 5184 sufficient five-query sets form exactly 15 orbits under
   vertex relabeling `S6`: two orbits of size 720, nine of size 360,
   two of size 180 and two of size 72. The corresponding stabilizer sizes
   are 1, 2, 4 and 10, respectively.

The earlier r59 result about all **Boolean** triple subsets and minimum
five *Boolean* query bits remains distinct. Here the extended ambient
domain is `Z^20` or `N^20` and the five repairs are integer values.
The output lattice has index 96: arbitrary pair-count and query tuples
need not be realizable.

## Certificate and proof route

Compute the integer-rational-nullspace matrix `K` whose five columns
form a `Z`-basis of `ker_Z W`. The basis is integral and its free-coordinate
5x5 submatrix is the identity. For five-coordinate `Q`, full injectivity
is equivalent to `det(K_Q) != 0`. Exhaustive exact enumeration gives
`det(K_Q)=-1` in 2592 cases, `0` in 10320, and `+1` in 2592.
The absolute determinant of `[W;E_Q]` is 96 times `abs(det(K_Q))`,
using the integer image index from the Smith form. Finally, apply each
of the 720 vertex permutations to all 5184 sufficient query sets,
partitioning them into their actual orbits and checking orbit-stabilizer.

Reproducer (SymPy, exact integers, with invariants; this file embeds
the full minimal reproducer so it is independently reusable):

```python
from itertools import combinations, permutations
from collections import Counter
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
V = range(1, 7)
T = list(combinations(V, 3))
P = list(combinations(V, 2))
W = s.Matrix([[int(set(p).issubset(t)) for t in T] for p in P])
assert W.rank() == 15
K = s.Matrix.hstack(*W.nullspace())
assert K.shape == (20, 5) and all(v.q == 1 for v in K)
piv = set(W.rref()[1])
free = [i for i in range(20) if i not in piv]
assert K.extract(free, range(5)) == s.eye(5)
D = smith_normal_form(W, domain=ZZ)
assert Counter(int(D[i,i]) for i in range(15)) == {1:10, 2:4, 6:1}
hist, good = Counter(), set()
for q in combinations(range(20), 5):
    det = int(K.extract(q, range(5)).det())
    hist[det] += 1
    if det:
        good.add(q)
assert hist == {-1:2592, 0:10320, 1:2592}
assert abs(W.col_join(s.eye(20).extract(min(good),range(20))).det()) == 96
ti = {t:i for i,t in enumerate(T)}
actions = []
for perm in permutations(V):
    pm = dict(zip(V,perm))
    actions.append([ti[tuple(sorted(pm[x] for x in t))] for t in T])
remaining, sizes = set(good), Counter()
while remaining:
    q = min(remaining)
    orbit = {tuple(sorted(a[i] for i in q)) for a in actions}
    assert orbit <= remaining
    sizes[len(orbit)] += 1
    assert len(orbit) * sum(tuple(sorted(a[i] for i in q)) == q for a in actions) == 720
    remaining -= orbit
assert sizes == {720:2, 360:9, 180:2, 72:2}
assert sum(k*v for k,v in sizes.items()) == 5184
print('PASS', dict(hist), dict(sizes))
```

## Relation to Enterprise Math and precise remaining question

This is an auxiliary six-axis **label-incidence observer** certificate.
The native P000 domain has six spatial axes, heartbeat time separately
typed, and primitive triadic closure `E`. The remaining scientific
bridge is to specify which of these 20 labeled triples are legitimate
native `E` states, what their weights mean, and which future operations
the pair-count observer must preserve. Apply the joint-relation
preservation rule and the BRC observer/fiber test before using this
integer-incidence compression. Avoid opening a duplicate native task:
compare with current P000 native-contact/observer bridge publications.

Frozen Result `RR-AA38973D56330E59D315` (F7) and accepted
`RR-774CF0739BD6CD117CF6` (FCC) are unaffected. Formal review,
reference passes, synthesis, follow-up, Driver authority and Source
publication require their own currently authenticated pathway.

GitHub scientific-method snapshot:
`awdawmip/enterprise-math@302c04376d56c2299ce14c5f4578f6bba1a887b4`.
