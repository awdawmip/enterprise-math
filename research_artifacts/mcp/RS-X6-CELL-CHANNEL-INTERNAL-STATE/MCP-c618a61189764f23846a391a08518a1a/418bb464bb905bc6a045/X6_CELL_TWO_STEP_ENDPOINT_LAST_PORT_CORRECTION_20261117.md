# X6 Cell: two-step signed-axis model and last-port observation (2026-11-17)

Task: RS-X6-CELL-CHANNEL-INTERNAL-STATE; author-scoped exploratory lemma, not native X6 admission or a physical channel theorem.

## Explicit model

Let E={+e_i,-e_i : i=1,...,6} be 12 formally distinct labelled steps in the free abelian group Z^6. A length-two history is (a,b) in E^2, with endpoint d=a+b. This model concerns only formally signed-axis paths. It does not identify relational PF-10 channels with spatial axes or assume a legal triadic event.

## Exact finite classification

There are 12^2=144 labelled histories. The possible endpoints and their fiber sizes are:

* d=0: one endpoint, 12 histories (a,-a).
* d=+/-2e_i: 12 endpoints, one history each (a,a).
* d=+/-e_i +/-e_j, i<j: 4*C(6,2)=60 endpoints, two histories each (a,b) and (b,a).

Hence 1+12+60=73 distinct endpoints and 12+12+120=144 histories. Both are exhaustive because every ordered pair of signed basis steps is either equal, opposite, or on distinct axes.

## Observation-dependent memory, corrected

If the observer retains ONLY d and must later reconstruct the ordered pair, the worst fiber contains 12 histories, so any fixed-width auxiliary code needs at least ceil(log2 12)=4 bits. Four bits suffice by encoding a fiber index. This is an information bound for exact history reconstruction, not for every possible future update rule.

If the observer may ALSO read the full signed final step b, then (d,b) is injective on histories: a=d-b. In that observer model the auxiliary memory lower bound is ZERO, not four bits. In particular the zero-endpoint 12-fold ambiguity disappears under the signed-last-step query. If only the last axis index i(b) is disclosed, then zero endpoint leaves exactly two sign histories, requiring one additional bit for reconstruction. Any claim of a universal four-bit lower bound with a freely available full signed last-port query would be incorrect.

For an update requiring only d, no additional history memory is necessary. For updates that inspect the last signed step, the endpoint quotient is not contextually sufficient: (e_1,e_2) and (e_2,e_1) have equal d but different last tags, so a future operation testing the last tag distinguishes them.

## Reproduction (Python 3, exact integer arithmetic)

```python
from collections import Counter, defaultdict
steps = [(i, s) for i in range(6) for s in (-1, 1)]
fibers = defaultdict(list)
for a in steps:
    for b in steps:
        d = [0] * 6
        d[a[0]] += a[1]
        d[b[0]] += b[1]
        fibers[tuple(d)].append((a, b))
assert len(fibers) == 73
assert Counter(map(len, fibers.values())) == {1:12, 2:60, 12:1}
assert sum(map(len, fibers.values())) == 144
assert len({(d, p[1]) for d, ps in fibers.items() for p in ps}) == 144
```

## Frontier

Exact toy-model result only. To infer a lower bound on native Cell internal state, specify the actual state quotient, permitted Port observations, legal transition relation, and future-context equivalence under P000/PF-10/native X6; do not transfer this toy 4-bit endpoint-only bound to a richer observer. Preserve spatial/relational channel distinction and BRC provenance.